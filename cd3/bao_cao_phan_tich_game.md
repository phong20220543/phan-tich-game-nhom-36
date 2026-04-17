# Báo Cáo Phân Tích Dữ Liệu Game Sales

## Giới Thiệu

Báo cáo này phân tích dữ liệu bán hàng video game từ dataset vgsales_clean.csv. Dataset chứa thông tin về hơn 16,000 game, bao gồm tên, nền tảng, năm phát hành, thể loại, nhà phát hành và doanh số bán hàng ở các khu vực khác nhau (NA, EU, JP, Other) và toàn cầu.

Mục tiêu của báo cáo là xây dựng mô hình dự đoán doanh số bán hàng toàn cầu dựa trên các yếu tố khác, đánh giá hiệu suất mô hình, và rút ra những insight hữu ích cho ngành công nghiệp game.

## Phương Pháp

### Thu thập và Chuẩn bị Dữ liệu
- Dataset: vgsales_clean.csv với 16,206 hàng và 11 cột
- Các biến: Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
- Xử lý dữ liệu:
  - Loại bỏ giá trị thiếu (không có trong dataset này)
  - Mã hóa biến phân loại (Platform, Genre, Publisher) bằng LabelEncoder
  - Chia dữ liệu thành tập train (80%) và test (20%)

### Mô Hình Dự Đoán
Sử dụng hai mô hình:
1. **Linear Regression**: Mô hình tuyến tính đơn giản
2. **Random Forest Regressor**: Mô hình ensemble với 100 cây quyết định

Biến đầu vào: Year, Platform_encoded, Genre_encoded, Publisher_encoded, NA_Sales, EU_Sales, JP_Sales, Other_Sales
Biến mục tiêu: Global_Sales

### Đánh Giá Mô Hình
Sử dụng các metrics:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

## Kết Quả

### Thống Kê Cơ Bản
- Tổng số game: 16,206
- Năm phát hành: 1980 - 2020
- Các nền tảng phổ biến: PS2, DS, PS3, Wii, X360
- Thể loại phổ biến: Action, Sports, Misc, Role-Playing, Shooter

### Hiệu Suất Mô Hình

#### Linear Regression
- MAE: 0.0029
- RMSE: 0.0052
- R²: 1.0000

#### Random Forest
- MAE: 0.0429
- RMSE: 0.8592
- R²: 0.8290

### Tầm Quan Trọng của Biến (Random Forest)
1. NA_Sales: 85.84%
2. EU_Sales: 9.87%
3. JP_Sales: 3.02%
4. Other_Sales: 0.80%
5. Year: 0.16%
6. Platform_encoded: 0.15%
7. Genre_encoded: 0.11%
8. Publisher_encoded: 0.05%

## Insight

1. **Doanh số Bắc Mỹ đóng vai trò quan trọng nhất** trong việc dự đoán doanh số toàn cầu, cho thấy thị trường game Mỹ là động lực chính.

2. **Linear Regression cho kết quả hoàn hảo** vì Global_Sales là tổng của các sales khu vực, tạo ra mối quan hệ tuyến tính hoàn hảo.

3. **Random Forest cung cấp cái nhìn thực tế hơn** với R² = 0.83, cho thấy các yếu tố khác như năm phát hành và nền tảng cũng ảnh hưởng.

4. **Thị trường Nhật Bản có ảnh hưởng nhỏ hơn** so với NA và EU, có thể do sự khác biệt văn hóa và sở thích game.

5. **Năm phát hành và nhà phát hành có ảnh hưởng hạn chế**, cho thấy doanh số phụ thuộc nhiều hơn vào hiệu suất bán hàng khu vực.

6. **Khuyến nghị**: Tập trung vào thị trường Bắc Mỹ để tối đa hóa doanh số toàn cầu. Cân nhắc localization cho thị trường Nhật Bản để tăng doanh số.

## Kết Luận

Mô hình Random Forest cung cấp dự đoán đáng tin cậy cho doanh số game toàn cầu với độ chính xác cao. Các insight từ phân tích có thể giúp nhà phát triển game và nhà phát hành đưa ra quyết định chiến lược tốt hơn.