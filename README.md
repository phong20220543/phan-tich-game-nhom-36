# Báo Cáo Phân Tích Dữ Liệu Doanh Số Game 

Dự án này tập trung vào quy trình phân tích, làm sạch dữ liệu, trực quan hóa và xây dựng mô hình dự đoán cơ bản dựa trên bộ dữ liệu doanh số ngành công nghiệp game toàn cầu.

## 1. Quá trình Làm sạch Dữ liệu (Data Cleaning)
Quá trình tiền xử lý được thực hiện thông qua tệp `DataCleaning.py`:
- **Tập dữ liệu gốc:** `vgsales.csv` với tổng cộng **16.598** dòng.
- **Các bước xử lý:**
  - Phát hiện **271** dòng bị khuyết (missing) dữ liệu ở trường `Year` và **58** dòng khuyết `Publisher`.
  - Đã tiến hành **loại bỏ 271 dòng thiếu thông tin năm (`Year`)** do đây là trường dữ liệu quan trọng cốt lõi phục vụ các phân tích theo chiều thời gian.
  - Kiểm tra và đảm bảo không có dòng dữ liệu nào bị trùng lặp (Duplicates = 0).
  - Chuyển đổi kiểu dữ liệu của cột `Year` từ `float` sang `integer` để thống nhất chuẩn hiển thị số nguyên cho năm.
- **Tập dữ liệu đầu ra:** `vgsales_clean.csv` với **16.327** dòng dữ liệu chuẩn xác, sẵn sàng cho pha phân tích.
- **Các trường dữ liệu (Columns):** 
  - `Rank` (int), `Name` (str), `Platform` (str), `Year` (int), `Genre` (str), `Publisher` (str).
  - Các trường doanh số: `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales` (tất cả đều là kiểu float tính theo đơn vị triệu bản).

## 2. Công cụ và Môi trường sử dụng
- **Ngôn ngữ lập trình:** Python 3.
- **Môi trường IDE:** PyCharm.
- **Quản lý môi trường:** Môi trường ảo (`.venv`).
- **Các thư viện (Libraries):**
  - **Pandas:** Đọc, làm sạch, và thao tác với dữ liệu tabular (Dataframe).
  - **Matplotlib & Seaborn:** Trực quan hóa dữ liệu (Visualization) để tạo các biểu đồ nâng cao, sắc nét, có bảng màu chuyên nghiệp.
  - **Numpy:** Hỗ trợ tính toán ma trận và xây dựng thuật toán Machine Learning.

## 3. Các Biểu đồ và Kết quả Phân tích (Visualization)
Được xử lý chính trong `bieudo.py` và `EDA.py`, nhóm đã vẽ 5 biểu đồ trực quan khai thác sâu các khía cạnh:
1. **Biểu đồ Đường (Line Chart):** *Doanh số game toàn cầu theo năm (1980 - 2015).* 
   - Số liệu nổi bật: Ngành game đạt đỉnh điểm về mặt doanh số đĩa cứng vào năm **2008** với mức kỷ lục đạt **~679 triệu bản** được bán ra trên toàn cầu.
2. **Biểu đồ Cột Ngang (Horizontal Bar Chart):** *Doanh số theo Thể loại (Genre).*
   - Số liệu nổi bật: Các thể loại thống trị thị trường một cách áp đảo là **Action** (hơn 1.700 triệu bản), **Sports** (hơn 1.300 triệu bản), và **Shooter** (hơn 1.000 triệu bản).
3. **Biểu đồ Cột Dọc (Vertical Bar Chart):** *Doanh số theo Nền tảng (Platform).*
   - Số liệu nổi bật: Hệ máy console có doanh số phần mềm bán ra cao nhất lịch sử là **PS2** (~1.255 triệu bản), theo sau bởi các cỗ máy như **X360**, **PS3**, **Wii** và **DS**.
4. **Biểu đồ Nhiệt (Heatmap):** *Tương quan Doanh số giữa Thể loại và Khu vực.*
   - Cho thấy rõ sức mua của từng khu vực phân hóa theo dòng game (Ví dụ: game Role-Playing cực thịnh ở Nhật Bản so với các nước phương Tây).
5. **Biểu đồ Tròn (Pie Chart):** *Thị phần doanh số theo Khu vực.*
   - Thống kê tỷ trọng tiêu thụ game toàn cầu: **Bắc Mỹ (49.3%)**, **Châu Âu (27.3%)**, **Nhật Bản (14.6%)**, và phần còn lại của thế giới (8.8%).

## 4. Mô hình Dự đoán (Modeling)
Dự án triển khai một mô hình **Hồi quy Tuyến tính (Simple Linear Regression)** được lập trình toán học thủ công bằng *Numpy* (không dùng thư viện ăn sẵn như `scikit-learn`):
- **Feature (Đặc trưng):** `Year` (Năm phát hành).
- **Target (Mục tiêu):** `Global_Sales` (Tổng doanh số toàn cầu).
- **Đánh giá:** Tính toán độ tin cậy $R^2$ score trực tiếp trên tập test (Test Set) sau khi tiến hành Train/Test Split với tỷ lệ 80/20.

## 5. Hướng dẫn Chạy Chương trình
Để chạy thử nghiệm các tiến trình, hãy mở Terminal (command prompt hoặc terminal của PyCharm) tại thư mục `BTL` và sử dụng môi trường ảo `.venv` có sẵn để chạy mã:

**Bước 1: Làm sạch dữ liệu (Data Cleaning)**
```bash
.\.venv\Scripts\python.exe DataCleaning.py
```
*(Đọc từ `vgsales.csv` và sinh ra file sạch `vgsales_clean.csv`)*

**Bước 2: Xuất các Biểu đồ (Visualization)**
```bash
.\.venv\Scripts\python.exe bieudo.py
```
*(Chương trình sẽ tự động vẽ và lưu 5 file ảnh biểu đồ có đuôi `.png` trực tiếp vào trong thư mục dự án)*

**Bước 3: Chạy Huấn luyện và Dự đoán bằng Linear Regression**
```bash
.\.venv\Scripts\python.exe main.py
```
*(Giao diện dòng lệnh sẽ in ra thông báo, bạn cần gõ số năm muốn dự đoán (ví dụ: `2026` hoặc `2030`), sau đó Enter để xem mức doanh số dự kiến và điểm số R² của mô hình).*
