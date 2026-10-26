# Sample Data

This folder intentionally contains **no real logs**. Real telemetry from your lab belongs in Splunk,
not in Git (it may contain hostnames, usernames and IP addresses).

To test SPL **logic** before the lab is built, generate clearly-synthetic events:

```bash
python3 scripts/generate-synthetic-events.py --out sample-data
```

This writes `synthetic_*.log` files (git-ignored). Every line includes `synthetic=true`.

## Ingesting synthetic data safely

1. Create a separate test index, e.g. `lab_synthetic`.
2. Settings → Add Data → Upload, choose a file, sourcetype `kv` or "Automatic", index `lab_synthetic`.
3. Run the detection SPL with `index=lab_synthetic` substituted for the real index.

Synthetic results only show that a query's logic runs against fabricated, simplified events.
They are **not** evidence of real detection performance, and must never be described as such.
