import streamlit as st
import joblib, pandas as pd, json, os

st.set_page_config(page_title="Credit Scoring (Fintech & Banking)", layout="wide")

st.title("Credit Scoring Demo — Fintech & Banking")
st.caption("Upload a CSV of borrower features. The model will output default probability and approve/reject.")

model_path = st.text_input("Model artifact path", value="artifacts/model.joblib")

pipe = None
if os.path.exists(model_path):
    try:
        pipe = joblib.load(model_path)
        st.success("Loaded model artifact.")
    except Exception as e:
        st.error(f"Failed to load model: {e}")
else:
    st.warning("Model path does not exist. Train a model first.")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

threshold = st.slider("Decision threshold (probability of default)", 0.1, 0.9, 0.7, 0.01)

if st.button("Score") and uploaded is not None and pipe is not None:
    df = pd.read_csv(uploaded)
    try:
        p = pipe.predict_proba(df)[:,1]
    except Exception:
        s = pipe.decision_function(df)
        import numpy as np
        p = (s - s.min())/(s.max()-s.min()+1e-9)

    import numpy as np
    decision = np.where(p >= threshold, "REJECT", "APPROVE")
    out = df.copy()
    out["prob_default"] = p
    out["decision"] = decision
    st.subheader("Preview")
    st.dataframe(out.head(30))
    st.download_button("Download results CSV", data=out.to_csv(index=False), file_name="predictions.csv")

st.markdown("---")
st.markdown("**Note:** This demo expects columns consistent with your training schema. Edit `config.yaml` and retrain if needed.")
