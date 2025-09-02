# Ứng dụng AI trong Đánh giá Điểm Tín dụng Cá nhân (Fintech & Banking)

> Báo cáo 30–40 trang — **bản thảo soạn sẵn** để chuyển sang Word/PDF. Thay các phần `TODO` bằng nội dung/biểu đồ thực nghiệm của bạn.

**Nhóm:** …
**Môn học:** Tư duy Trí tuệ Nhân tạo (AI Thinking)
**Ngày:** 2025-09-02

---

## 1. Tóm tắt điều hành (Executive Summary)
- Bài toán: dự đoán rủi ro tín dụng (default) của cá nhân để hỗ trợ quyết định cho vay/hạn mức.
- Dữ liệu: tập ~1.8M khoản vay nhiều năm (ví dụ kiểu LendingClub) với đặc trưng nhân khẩu, thu nhập, lịch sử tín dụng, mục đích vay, v.v.
- Cách tiếp cận: mô hình tabular (Logistic/XGBoost/LightGBM) + kiểm định ổn định/PSI; mở rộng RAG để tra cứu chính sách & giải thích.
- Kết quả chính: **TODO** (AUC, PR-AUC, KS, PSI, các đồ thị ROC/PR).
- Tác động xã hội–đạo đức: minh bạch, công bằng, quyền riêng tư; đề xuất cơ chế giám sát.

> Gợi ý: Tóm tắt 8–10 dòng, 1 hình pipeline.

---

## 2. Giới thiệu & bối cảnh
- Khác biệt Fintech vs Banking (nguồn dữ liệu, quy định, tốc độ ra quyết định, rủi ro).
- Lợi ích của credit scoring dựa trên AI: mở rộng tài chính toàn diện, giảm nợ xấu, tự động hóa quy trình.
- Mục tiêu báo cáo và phạm vi.

---

## 3. Phân tích bài toán (AI Thinking)
### 3.1 Người dùng & mục tiêu
- Người dùng: bộ phận thẩm định tín dụng; hệ thống phê duyệt tự động; khách hàng cá nhân (nhận phản hồi/khuyến nghị).
- Mục tiêu AI: ước lượng xác suất vỡ nợ (PD) và quyết định approve/reject theo ngưỡng.

### 3.2 Decomposition (phân rã)
1) Thu nhận & làm sạch dữ liệu → 2) Biểu diễn đặc trưng → 3) Huấn luyện & tinh chỉnh → 4) Đánh giá, hiệu chỉnh ngưỡng → 5) Explainability & RAG → 6) Giám sát & drift.

### 3.3 Representation
- Numeric: chuẩn hóa/robust scale, xử lý ngoại lai.
- Categorical: one-hot hoặc **embedding** nếu cardinality cao.
- Time-based: snapshot/rolling aggregates (30/90/365 ngày).

### 3.4 Search & Optimization
- Tối ưu siêu tham số; tối ưu **threshold** theo mục tiêu kinh doanh (profit/loss).

### 3.5 Ethics & Constraints
- Quy tắc pháp lý (tuổi tối thiểu, blacklist…) → *hard rules*.
- Fairness: kiểm tra TPR/FPR theo nhóm, disparate impact.
- Privacy: tối thiểu hóa dữ liệu nhạy cảm; ghi nhận consent; audit logs.

---

## 4. Dữ liệu
### 4.1 Nguồn & mô tả
- Tập dữ liệu ~1.8M bản ghi nhiều năm → phù hợp phân tách train (2014–2018) / test (2019–2020) để đo **PSI**.
- Thuộc tính chính: nhân khẩu, khoản vay, lịch sử tín dụng, hành vi.
- Biến mục tiêu: `default` (1 = vỡ nợ).

### 4.2 Chất lượng dữ liệu
- Thiếu giá trị, nhất quán mã hóa, outliers, leakage.
- **TODO**: Bảng miêu tả cột, tỷ lệ thiếu, phân phối mục tiêu.

### 4.3 Rủi ro dữ liệu
- Proxy bias (địa lý/thu nhập).
- Drift theo chu kỳ kinh tế.

---

## 5. Kiến trúc mô hình & Pipeline
### 5.1 Sơ đồ tổng thể
```mermaid
flowchart LR
A[Raw data] --> B[ETL & Feature Store]
B --> C[Train: Tabular ML]
C --> D[Model artifacts]
D --> E[Inference API/UI]
B --> F[(Vector DB: Policies/Docs)]
E --> G[LLM (RAG) for explanations]
G --> H[User-facing reasons & tips]
```
### 5.2 Lựa chọn mô hình
- **Baseline:** Logistic Regression (minh bạch).
- **Nâng cao:** LightGBM/XGBoost (histogram); fallback scikit-learn GBDT.
- **Explainability:** SHAP (global & local) — nếu tài nguyên cho phép.

### 5.3 Đặc tả I/O
- Input: bảng đặc trưng tabular; tùy chọn văn bản/policy cho RAG.
- Output: `prob_default`, quyết định (approve/reject), lý do chính (top features) và gợi ý cải thiện.

### 5.4 Lý do chọn kiến trúc
- Tree-based histogram hiệu quả cho tabular lớn.
- RAG tách bạch phần “giải thích theo chính sách” khỏi mô hình chấm điểm.

---

## 6. Thử nghiệm & Kết quả
### 6.1 Thiết kế thí nghiệm
- Split thời gian: train 2014–2018, test 2019–2020.
- So sánh: Logistic vs LightGBM vs (tuỳ chọn) XGBoost.
- Hạ tầng: seed cố định; downcasting dtype; sampling nếu thiếu RAM.

### 6.2 Chỉ số đánh giá
- AUC-ROC, PR-AUC, KS-statistic, Brier score (calibration), PSI.
- Business: lợi nhuận/kỳ vọng tổn thất theo threshold.

### 6.3 Kết quả
- **TODO**: Bảng tổng hợp và biểu đồ ROC/PR/Calibration.
- **TODO**: Bảng PSI theo đặc trưng/nhóm thời gian.

### 6.4 Explainability
- **TODO**: SHAP summary (global) + force plot (local case).

---

## 7. Triển khai demo
- `src/train.py` → tạo `artifacts/model.joblib`.
- `src/infer.py` → dự đoán file JSON/CSV.
- `app.py` (Streamlit) → upload CSV, xem `prob_default` + quyết định.

---

## 8. Đánh giá & Tư duy phản biện
### 8.1 Ưu/nhược điểm
- Ưu: hiệu quả, mở rộng, có explainability.
- Nhược: rủi ro drift, bias, yêu cầu giám sát.

### 8.2 Công bằng & Đạo đức
- Thử nghiệm fairness theo nhóm.
- Cơ chế khiếu nại & xem xét thủ công.
- Chính sách dữ liệu tối thiểu & bảo mật.

### 8.3 Hạn chế & Cải tiến
- Thêm calibration + reject inference.
- Feature store và monitoring (PSI/CSI theo tuần).

---

## 9. Kết luận
- Tóm tắt kết quả & khuyến nghị triển khai.

---

## Phụ lục
- Cấu hình, lược đồ dữ liệu, mã lệnh, tham số, chi tiết PSI.
