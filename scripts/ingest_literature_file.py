# -*- coding: utf-8 -*-

import argparse
import json
import re
from pathlib import Path
from datetime import datetime

import pandas as pd


COLUMN_ALIASES = {
    "title": ["Title", "文献标题", "题名", "标题"],
    "abstract": ["Abstract", "摘要"],
    "year": ["Year", "年份", "出版年"],
    "doi": ["DOI", "doi"],
    "authors": ["Authors", "作者"],
    "source_title": ["Source title", "Source Title", "期刊", "来源出版物"],
}


def normalize_text(x):
    if pd.isna(x):
        return ""
    x = str(x).strip()
    return re.sub(r"\s+", " ", x)


def normalize_title(x):
    x = normalize_text(x).lower()
    x = re.sub(r"[^\w\s]", "", x)
    return re.sub(r"\s+", " ", x).strip()


def normalize_doi(x):
    x = normalize_text(x).lower()
    x = x.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return x.strip()


def find_input_file(path_arg):
    if path_arg:
        p = Path(path_arg)
        if p.exists():
            return p
        raise FileNotFoundError(f"找不到输入文件：{p}")

    candidates = []
    for ext in [".csv", ".xlsx", ".xls"]:
        candidates.extend(Path(".").glob(f"数据库{ext}"))

    if not candidates:
        raise FileNotFoundError("项目根目录没有找到 数据库.csv / 数据库.xlsx / 数据库.xls")

    return candidates[0]


def read_table(path):
    suffix = path.suffix.lower()

    if suffix == ".csv":
        last_error = None
        for enc in ["utf-8-sig", "utf-8", "gb18030"]:
            try:
                df = pd.read_csv(path, encoding=enc)
                return df, {"file_type": "csv", "encoding": enc}
            except UnicodeDecodeError as e:
                last_error = e
        raise RuntimeError(f"CSV 编码读取失败：{last_error}")

    if suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(path, sheet_name=0)
        return df, {"file_type": suffix.replace(".", ""), "sheet": 0}

    raise ValueError(f"不支持的文件格式：{suffix}")


def find_col(df, key):
    aliases = COLUMN_ALIASES[key]
    cols = list(df.columns)
    for a in aliases:
        if a in cols:
            return a
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=None, help="输入文件路径；不填则自动寻找根目录下的 数据库.csv/xlsx/xls")
    parser.add_argument("--outdir", default="literature/processed")
    args = parser.parse_args()

    input_path = find_input_file(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df, read_info = read_table(input_path)
    df.columns = [str(c).strip() for c in df.columns]

    colmap = {k: find_col(df, k) for k in COLUMN_ALIASES}

    missing = [k for k, v in colmap.items() if v is None]
    if missing:
        raise ValueError(
            f"缺少必要字段映射：{missing}\n"
            f"当前列名：{list(df.columns)}"
        )

    records = []
    seen = set()
    duplicate_count = 0
    missing_abstract_count = 0
    years = []

    for _, row in df.iterrows():
        title = normalize_text(row[colmap["title"]])
        abstract = normalize_text(row[colmap["abstract"]])
        year_raw = normalize_text(row[colmap["year"]])
        doi = normalize_doi(row[colmap["doi"]])
        authors = normalize_text(row[colmap["authors"]])
        source_title = normalize_text(row[colmap["source_title"]])

        if not title:
            continue

        if doi:
            key = f"doi:{doi}"
        else:
            key = f"title:{normalize_title(title)}"

        if key in seen:
            duplicate_count += 1
            continue
        seen.add(key)

        try:
            year = int(float(year_raw)) if year_raw else None
        except Exception:
            year = None

        if year is not None:
            years.append(year)

        missing_abstract = not bool(abstract)
        if missing_abstract:
            missing_abstract_count += 1

        records.append({
            "record_id": f"R{len(records) + 1:05d}",
            "title": title,
            "abstract": abstract,
            "year": year,
            "doi": doi,
            "authors": authors,
            "source_title": source_title,
            "missing_abstract": missing_abstract,
            "source_file": str(input_path),
        })

    out_csv = outdir / "records_dedup.csv"
    out_jsonl = outdir / "records_dedup.jsonl"
    out_report = outdir / "ingest_report.json"

    out_df = pd.DataFrame(records)
    out_df.to_csv(out_csv, index=False, encoding="utf-8-sig")

    with open(out_jsonl, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    report = {
        "input_file": str(input_path),
        "read_info": read_info,
        "raw_count": int(len(df)),
        "dedup_count": int(len(records)),
        "duplicate_count": int(duplicate_count),
        "missing_abstract_count": int(missing_abstract_count),
        "year_min": min(years) if years else None,
        "year_max": max(years) if years else None,
        "columns": list(df.columns),
        "column_mapping": colmap,
        "outputs": {
            "records_dedup_csv": str(out_csv),
            "records_dedup_jsonl": str(out_jsonl),
            "ingest_report": str(out_report),
        },
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    with open(out_report, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("Literature file ingest completed.")
    print(f"Input file: {input_path}")
    print(f"Read info: {read_info}")
    print(f"Raw count: {len(df)}")
    print(f"Dedup count: {len(records)}")
    print(f"Duplicate count: {duplicate_count}")
    print(f"Missing abstract count: {missing_abstract_count}")
    print(f"Year range: {report['year_min']} - {report['year_max']}")
    print(f"Output CSV: {out_csv}")
    print(f"Output JSONL: {out_jsonl}")
    print(f"Report: {out_report}")


if __name__ == "__main__":
    main()
