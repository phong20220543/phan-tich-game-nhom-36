# Thiết Kế Slide Thuyết Trình: Phân Tích Dữ Liệu Game Sales

## Slide 1: Trang Bìa
- Tiêu đề: Phân Tích Dữ Liệu Bán Hàng Video Game
- Tên tác giả: [Tên của bạn]
- Ngày: [Ngày hiện tại]
- Logo hoặc hình ảnh game

## Slide 2: Mục Lục
- Giới thiệu
- Phương pháp
- Kết quả
- Insight
- Kết luận

## Slide 3: Giới Thiệu Dataset
- Nguồn: Dataset vgsales_clean.csv
- Kích thước: 16,206 game
- Thời gian: 1980 - 2020
- Các biến chính:
  - Rank, Name, Platform, Year, Genre, Publisher
  - NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
- Biểu đồ: Phân bố game theo năm phát hành

## Slide 4: Phương Pháp Phân Tích
- Chuẩn bị dữ liệu:
  - Xử lý missing values
  - Encode categorical variables
  - Train/Test split (80/20)
- Mô hình sử dụng:
  - Linear Regression
  - Random Forest Regressor
- Metrics đánh giá: MAE, RMSE, R²

## Slide 5: Kết Quả - Thống Kê Cơ Bản
- Top 5 nền tảng: PS2, DS, PS3, Wii, X360
- Top 5 thể loại: Action, Sports, Misc, Role-Playing, Shooter
- Top 5 nhà phát hành: Nintendo, Electronic Arts, Activision, Sony, Ubisoft
- Biểu đồ: Doanh số theo khu vực

## Slide 6: Kết Quả - Hiệu Suất Mô Hình
- Bảng so sánh:
  | Model | MAE | RMSE | R² |
  |-------|-----|------|----|
  | Linear Regression | 0.0029 | 0.0052 | 1.0000 |
  | Random Forest | 0.0429 | 0.8592 | 0.8290 |
- Giải thích: Linear Regression hoàn hảo vì Global_Sales = sum các sales khu vực

## Slide 7: Tầm Quan Trọng Biến
- Biểu đồ cột: Feature Importance
  - NA_Sales: 85.84%
  - EU_Sales: 9.87%
  - JP_Sales: 3.02%
  - Other_Sales: 0.80%
  - Các biến khác < 1%

## Slide 8: Insight Chính
1. Thị trường Bắc Mỹ quan trọng nhất
2. Doanh số khu vực quyết định doanh số toàn cầu
3. Năm phát hành và nền tảng ảnh hưởng hạn chế
4. Cần localization cho thị trường Nhật

## Slide 9: Dự Đoán và Ứng Dụng
- Mô hình có thể dự đoán doanh số game mới
- Hỗ trợ quyết định đầu tư và marketing
- Xác định xu hướng thị trường
- Biểu đồ: Actual vs Predicted (Random Forest)

## Slide 10: Kết Luận
- Random Forest là mô hình phù hợp cho dự đoán
- Tập trung vào thị trường Bắc Mỹ
- Cân nhắc yếu tố văn hóa địa phương
- Câu hỏi & thảo luận

## Slide 11: Cảm Ơn
- Cảm ơn quý vị đã lắng nghe
- Q&A
- Liên hệ: [Thông tin liên hệ]