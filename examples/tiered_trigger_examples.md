# Tiered trigger examples

## LIGHT example

User asks:

```text
I have five rough topic ideas. Rank which two are worth checking further.
```

Expected mode: `LIGHT`

Run:

```text
intake → tiered-trigger-router → quick prior-art filter → quick novelty gate → compact brief
```

Do not run Advocate / Skeptic / Arbiter.

## STANDARD example

User asks:

```text
Can this topic become a publishable paper? Give me GO / NARROW / PIVOT / KILL.
```

Expected mode: `STANDARD`

Run:

```text
intake → context builder → prior-art → novelty → feasibility → collapse-test → arbiter → brief
```

Do not run multi-agent conflict unless a gate escalates.

## HIGH_RISK example

User asks:

```text
This may become my doctoral dissertation topic. I need a strict opposing review before I commit experiments.
```

Expected mode: `HIGH_RISK`

Run:

```text
STANDARD modules → relevant auditors → Advocate / Skeptic / Arbiter → final decision
```
