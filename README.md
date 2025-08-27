# KPI Drift Monitor
Monitor **% negative mentions** and **average stars** weekly and flag >1σ deviations from an 8‑week baseline.
## Run
```bash
pip install -r requirements.txt
python src/detect_drift.py
python src/plot_kpis.py
```
