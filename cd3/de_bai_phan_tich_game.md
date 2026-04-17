# Đề Bài Phân Tích Game

## 1. Mô tả chi tiết bài toán

Bài toán yêu cầu phân tích dữ liệu bán hàng của video game và xây dựng mô hình dự đoán doanh số toàn cầu (`Global_Sales`).
Dữ liệu gồm các thông tin chính về game như:
- `Name`: Tên game
- `Platform`: Nền tảng phát hành
- `Year`: Năm phát hành
- `Genre`: Thể loại game
- `Publisher`: Nhà phát hành
- `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`: Doanh số theo khu vực
- `Global_Sales`: Doanh số toàn cầu

Mục tiêu:
- Dự đoán `Global_Sales` dựa trên các đặc trưng có sẵn
- Đánh giá hiệu suất mô hình
- Phân tích biến quan trọng ảnh hưởng đến doanh số

## 2. Chọn Dataset cho bài toán

Dataset sử dụng trong bài là "Video Game Sales" lấy từ nguồn Kaggle.
Dữ liệu gốc nằm trong file `vgsales.csv`, sau đó được làm sạch để tạo thành file `vgsales_clean.csv`.

Nguồn tham khảo:
- Kaggle: Video Game Sales
- Có thể sử dụng thêm nguồn dữ liệu khác từ UCI hoặc Kaggle nếu muốn mở rộng bài toán.

## 3. Làm sạch Dataset

Các bước tiền xử lý dữ liệu:
1. Đọc dữ liệu từ file `vgsales_clean.csv`.
2. Chuẩn hoá tên cột, loại bỏ khoảng trắng và ký tự không cần thiết.
3. Loại bỏ các dòng trùng lặp.
4. Chuyển đổi các cột số (`Year`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales`) sang kiểu số.
5. Loại bỏ các dòng có giá trị thiếu trong các cột quan trọng.
6. Lọc năm phát hành hợp lệ (`Year >= 1950`).
7. Loại bỏ các giá trị doanh số âm hoặc không hợp lệ.

## 4. Yêu cầu thực hiện

- Viết script Python `game_sales_analysis.py` để:
  - Đọc và làm sạch dữ liệu
  - Mã hóa biến phân loại
  - Chuẩn hoá dữ liệu
  - Xây dựng và đánh giá mô hình
  - Xuất file kết quả và biểu đồ

- Tạo báo cáo phân tích gồm:
  - Mục tiêu bài toán
  - Dataset sử dụng
  - Phương pháp làm sạch dữ liệu
  - Kết quả mô hình và phân tích biến

## 5. File liên quan

- `game_sales_analysis.py`: Script phân tích
- `vgsales_clean.csv`: Dataset chính sau khi làm sạch
- `vgsales.csv`: Dataset gốc
- `bao_cao_phan_tich_game.md`: Báo cáo chi tiết
- `de_bai_phan_tich_game.md`: Đề bài phân tích game
