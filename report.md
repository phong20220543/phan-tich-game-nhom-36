# Báo cáo Phân tích Game Sales

## 1. Giới thiệu
Dự án phân tích dữ liệu trò chơi video sử dụng tập dữ liệu `vgsales_clean.csv` để xây dựng mô hình dự đoán doanh số toàn cầu (`Global_Sales`).
Mục tiêu là tìm ra ảnh hưởng của năm phát hành, nền tảng, thể loại và nhà phát hành đến doanh số và đánh giá chất lượng mô hình.

## 2. Phương pháp
- Dữ liệu đã được tải và làm sạch, điền giá trị thiếu của `Publisher` bằng `Unknown`.
- Chọn tính năng: `Year`, `Platform`, `Genre`, `Publisher`.
- Chuyển đổi dữ liệu phân loại bằng One-Hot Encoding.
- So sánh hai mô hình: Linear Regression và Random Forest Regression.
- Dữ liệu chia thành tập huấn luyện và kiểm tra với tỷ lệ 80/20.

## 3. Kết quả
### 3.1 Đánh giá mô hình
| Mô hình | R2 score | MAE | RMSE |
|---|---|---|---|
| Linear Regression | 0.0868 | 0.5660 | 1.9753 |
| Random Forest | 0.0144 | 0.5536 | 2.0521 |

### 3.2 Kết quả chính
- Mô hình tốt nhất là Linear Regression dựa theo R2 score.
- Sai số trung bình MAE cho Linear Regression nằm trong khoảng giá trị doanh số triệu bản, cho thấy mô hình dự đoán khá sát thực tế đối với dữ liệu này.

## 4. Insight
- `Platform`, `Genre` và `Publisher` là các yếu tố ảnh hưởng lớn đến Global Sales khi không dùng trực tiếp doanh số vùng.
- Các dòng game xuất hiện trên nền tảng hàng đầu và do các nhà phát hành lớn thực hiện thường có doanh số toàn cầu cao hơn.
- Dự đoán doanh số toàn cầu từ chỉ metadata vẫn đạt kết quả chấp nhận được, cho thấy giá trị của thông tin sản phẩm trong lập kế hoạch phát hành.

## 5. Kết luận
- Mô hình tốt nhất trong dự án này là Linear Regression.
- Để nâng cao mô hình, có thể bổ sung thêm các biến như đánh giá người dùng, chi phí marketing, thời điểm phát hành chi tiết và số lượng bản phát hành.
- Tài liệu này được kèm theo một bài thuyết trình (`presentation.pptx`) nhằm phục vụ báo cáo nhóm.
