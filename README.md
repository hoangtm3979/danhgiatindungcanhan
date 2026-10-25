# Credit Scoring — AI Thinking Starter Pack / Bộ khung tư duy AI cho chấm điểm tín dụng

[English](#english) · [Tiếng Việt](#tiếng-việt)

> **Repository status: educational scaffold / bộ khung học tập.** This repository is **not a complete, runnable model-training project** in its current checked state. A separate executed notebook is available at [`hoangtm3979/credit`](https://github.com/hoangtm3979/credit).

## English

**Context:** Educational exercise in decomposing a credit-risk prediction problem into data, labels, ML training, decision thresholds, interpretation, and operational monitoring.

- **Problem:** estimate loan default/adverse outcome probability while considering temporal leakage, data imbalance, calibration, and fairness.
- **Planned input:** structured loan/applicant records and a clearly specified outcome label.
- **Planned output:** risk probability, decision-support score, evaluation report, and a user-facing demonstration.
- **Approach described in documentation:** data preparation, Logistic Regression baseline, candidate tree ensembles, threshold and PSI evaluation.
- **Constraint:** no real lending decision, official bureau score, or demonstrated model performance is established by this repository alone.

### What is actually checked into this repo

- `app.py`: a Streamlit-oriented demonstration scaffold.
- `config.yaml`: configuration examples.
- `requirements.txt`: dependency listing.
- `report.md`: explicitly a **draft outline with TODOs**, not an experiment-verified paper.
- `slides_outline.md`, `self_eval.csv`: presentation and self-assessment templates.

**Correction to the former README:** it referred to `src/train.py`, `src/infer.py` and `assets/sample_input.json`, but those paths do **not** exist in the current root listing. The original Quickstart therefore cannot be treated as executable without completing the missing implementation.

## Tiếng Việt

**Bối cảnh:** Bài thực hành tư duy AI về đánh giá rủi ro tín dụng cá nhân. Mục đích là phân rã một vấn đề fintech thành các khâu có thể kiểm chứng.

- **Input dự kiến:** bảng khoản vay, đặc trưng khách hàng và nhãn được định nghĩa đúng thời điểm.
- **Output dự kiến:** xác suất rủi ro, điểm số hỗ trợ quyết định, báo cáo đánh giá và giao diện mẫu.
- **Phương pháp đề xuất:** chuẩn hóa dữ liệu, Logistic Regression làm baseline, boosted trees, tối ưu threshold, theo dõi PSI/drift.
- **Kết quả có thể xác nhận:** bộ khung mã/tài liệu đang có trong repository; **chưa có model benchmark hoàn chỉnh hoặc triển khai production được chứng minh tại đây**.
- **Vấn đề cần hoàn tất:** mã train/inference riêng, dữ liệu mẫu được phép chia sẻ, test pipeline, tính tái lập và loại bỏ TODO.

**Liên hệ công việc:** Notebook thực nghiệm đã lưu output ở repository [`credit`](https://github.com/hoangtm3979/credit); hai repository cần được hợp nhất hoặc phân định rõ vai trò trước khi đưa lên CV như một dự án hoàn chỉnh.

_Last reviewed: 2026-10-25._
