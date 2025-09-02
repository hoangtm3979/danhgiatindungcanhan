# Credit Scoring (Fintech & Banking) — Starter Pack

**Date:** 2025-09-02

This pack gives you:
- End-to-end ML pipeline scripts (`src/train.py`, `src/infer.py`, `app.py`)
- Ready-to-edit report outline (`report.md`, ~35 pages worth of content when moved to Word)
- Slide outline for 20–25 slides (`slides_outline.md`)
- Self-evaluation table (`self_eval.csv`)
- Config file (`config.yaml`) and requirements (`requirements.txt`)

It is designed to scale to a ~1.8M-row credit dataset (e.g., LendingClub-style).

## Quickstart

```bash
# 1) Python 3.11 recommended (3.13 may cause some libs to be unavailable)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

# 2) Train (edit config.yaml paths first)
python src/train.py --config config.yaml

# 3) Local inference demo
python src/infer.py --model_path artifacts/model.joblib --input_json assets/sample_input.json

# 4) Run Streamlit UI
streamlit run app.py --server.port 8502
```

## Files
- `src/train.py`: chunked CSV reader, downcasting dtypes, feature pipeline, train baseline + boosted model (falls back gracefully).
- `src/infer.py`: load artifact, run prediction for a single JSON or CSV batch.
- `app.py`: simple Streamlit app to upload CSV and score; shows top features (global) if available.
- `config.yaml`: dataset paths, column lists, target, split keys, model params.
- `report.md`: full report outline (copy to Word, then export to PDF).
- `slides_outline.md`: slide-by-slide bullet outline.
- `self_eval.csv`: “Bảng tự đánh giá AI Thinking” template (fill scores 1–5).
- `requirements.txt`: conservative set of libs; works even if XGBoost/LightGBM not present (fallback to scikit-learn).

## Tips for 1.8M rows
- Use `dtype_map` + `category` to shrink memory; prefer LightGBM (histogram) for speed; or XGBoost with `tree_method=hist`.
- If RAM < 32GB, train on balanced subsample first, then full train with selected features.
- Use time-based split (e.g., train 2014–2018, test 2019–2020) to evaluate stability (PSI).
- Persist `ColumnTransformer` and the model as artifacts (joblib).

