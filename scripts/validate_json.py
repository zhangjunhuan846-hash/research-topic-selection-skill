#!/usr/bin/env python3
"""Validate a JSON file against a JSON schema.

Requires: pip install jsonschema
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('json_file')
    ap.add_argument('schema_file')
    args = ap.parse_args()

    try:
        import jsonschema
    except ImportError:
        print('Missing dependency: jsonschema. Install with: pip install jsonschema', file=sys.stderr)
        sys.exit(2)

    data = json.loads(Path(args.json_file).read_text(encoding='utf-8'))
    schema = json.loads(Path(args.schema_file).read_text(encoding='utf-8'))
    jsonschema.validate(data, schema)
    print(f'OK: {args.json_file} validates against {args.schema_file}')


if __name__ == '__main__':
    main()
