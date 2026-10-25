# Credit Scoring — AI Thinking Starter Pack
# Bộ khung tư duy AI cho bài toán đánh giá rủi ro tín dụng

[Tiếng Việt](#tiếng-việt) · [English](#english)

## Tiếng Việt

Tôi tạo repository này như một **bộ khung học tập để phân rã bài toán AI trong tín dụng**: từ mục tiêu và dữ liệu đầu vào đến mô hình, cách đánh giá và giao diện thử nghiệm.

- **Bối cảnh:** hỗ trợ nghiên cứu khả năng dự báo kết quả bất lợi của khoản vay từ dữ liệu bảng.
- **Input dự kiến:** thuộc tính khoản vay/khách hàng và nhãn lịch sử có thời điểm xác định.
- **Output dự kiến:** xác suất rủi ro, điểm số minh họa, báo cáo đánh giá và giao diện Streamlit.
- **Phương pháp:** Logistic Regression baseline, thử mô hình cây, chọn ngưỡng, theo dõi phân bố và thay đổi dữ liệu.
- **Ràng buộc:** thông tin cần có trước thời điểm xét vay; xử lý dữ liệu thiếu, imbalance, calibration và khả năng giải thích.

### Các thành phần tôi đã chuẩn bị

- `app.py` — bộ khung giao diện Streamlit.
- `config.yaml`, `requirements.txt` — cấu hình và môi trường.
- `report.md`, `slides_outline.md`, `self_eval.csv` — đề cương báo cáo, thuyết trình và tự đánh giá.

**Hướng tiếp tục:** bổ sung phần train/inference hoàn chỉnh, dữ liệu mẫu và test pipeline để nối thiết kế với mã chạy. Các đường dẫn `src/train.py`, `src/infer.py` xuất hiện trong bản hướng dẫn cũ thuộc phần dự kiến triển khai, hiện chưa nằm trong repository.

Tôi có một **notebook thực nghiệm tín dụng đã chạy và lưu kết quả** ở repository [Credit Risk Modeling](https://github.com/hoangtm3979/credit).

## English

This repository is my **problem-decomposition and project-planning exercise** for credit-risk AI. It covers data/label design, baseline models, threshold decisions, evaluation, and a possible Streamlit presentation.

Current files include a Streamlit-oriented scaffold, configuration, dependencies, a report outline and presentation/self-assessment templates. The next stage is implementing the training/inference modules with reproducible data and tests.

For an executed Logistic Regression vs LightGBM notebook, see my [Credit Risk Modeling repository](https://github.com/hoangtm3979/credit).

*Learning scaffold and design notes.*
