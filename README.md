# Invoice Leak Detector

Finds synthetic invoice leakage and duplicate patterns.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m invoice_leak_detector.cli --input data/sample_invoices.json
```

## Test

```bash
python3 -m unittest discover tests
```
