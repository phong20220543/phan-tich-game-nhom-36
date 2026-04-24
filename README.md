# Video Game Sales Analysis & Prediction

## 1. Giới thiệu
Dự án này thực hiện bài toán phân tích và dự đoán doanh số trò chơi điện tử từ bộ dữ liệu `vgsales.csv`. Đây là bài toán phân tích khám phá (EDA) và hồi quy với biến mục tiêu là `Global_Sales` (Doanh số toàn cầu). Mục tiêu của nhóm là xử lý dữ liệu thiếu, phân tích các xu hướng của thị trường game qua các năm, nền tảng, thể loại, trực quan hóa dữ liệu bằng các biểu đồ sinh động và xây dựng mô hình hồi quy tuyến tính cơ bản để dự đoán tổng doanh số theo năm.

## 2. Mục tiêu bài toán
- Xử lý dữ liệu thiếu trong tập dữ liệu gốc.
- Phân tích mối quan hệ giữa `Global_Sales` và các biến phân loại/thời gian (Năm, Nền tảng, Thể loại, Khu vực).
- Trực quan hóa dữ liệu bằng Line chart, Bar chart, Heatmap và Pie chart thông qua Matplotlib và Seaborn.
- Xây dựng mô hình hồi quy tuyến tính dự đoán tổng doanh số toàn cầu theo năm.
- Đánh giá mô hình bằng chỉ số $R^2$ Score.

## 3. Dataset sử dụng
- File dữ liệu gốc: `vgsales.csv`
- File dữ liệu đã làm sạch: `vgsales_clean.csv`
- Số dòng dữ liệu ban đầu: 16.598
- Số dòng dữ liệu sau làm sạch: 16.327
- Biến mục tiêu: `Global_Sales`

Một số đặc trưng quan trọng ảnh hưởng đến phân tích doanh số:
- `Year`: Năm phát hành.
- `Genre`: Thể loại game.
- `Platform`: Hệ máy (Nền tảng).
- `Publisher`: Nhà phát hành.
- Doanh số phân vùng: `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`.

## 4. Quy trình thực hiện
### Bước 1. Đọc và kiểm tra dữ liệu
Dữ liệu được đọc từ `vgsales.csv` bằng thư viện `pandas`. Tiến hành thống kê số lượng dòng, kiểm tra kiểu dữ liệu và đếm số lượng giá trị thiếu trong từng trường.

### Bước 2. Xử lý dữ liệu thiếu
Trong project, quy trình làm sạch được tập trung trong tệp `DataCleaning.py`:
- Thống kê phát hiện 271 dòng khuyết `Year` và 58 dòng khuyết `Publisher`.
- Tiến hành loại bỏ 271 dòng thiếu thông tin năm (`Year`) do đây là mốc thời gian cực kỳ quan trọng cho các chuỗi phân tích.
- Loại bỏ các dòng dữ liệu trùng lặp (nếu có).
- Chuyển đổi kiểu dữ liệu cột `Year` từ `float` sang `integer` để thống nhất chuẩn hiển thị số nguyên.
- Lưu dữ liệu sạch ra tệp `vgsales_clean.csv`.

### Bước 3. Phân tích mối quan hệ giữa doanh số và các yếu tố
Thông qua file `EDA.py`, project tiến hành phân tích sự biến động của `Global_Sales` theo đa chiều:
- Tính tổng doanh số và số lượng game phát hành theo từng năm.
- Thống kê doanh số theo Thể loại (Genre) và Hệ máy (Platform).
- Nhóm top các tựa game và nhà phát hành có doanh thu cao nhất lịch sử.

Kết quả nổi bật:
- Năm đỉnh cao của ngành game là 2008 với mức doanh số khoảng ~679 triệu bản.
- Action, Sports và Shooter là 3 thể loại dẫn đầu thị trường.
- PS2 là nền tảng thống trị lịch sử với hơn 1.255 triệu bản phần mềm được bán ra.

### Bước 4. Trực quan hóa
Script `bieudo.py` sinh ra các biểu đồ chuyên nghiệp (sử dụng Seaborn):
- `chart1_line_yearly_sales.png`: Line chart sự biến động doanh số toàn cầu theo từng năm.
- `chart2_bar_genre_sales.png`: Bar chart nằm ngang thể hiện tổng doanh số các thể loại.
- `chart3_bar_platform_sales.png`: Bar chart dọc cho top nền tảng bán chạy nhất.
- `chart4_heatmap_genre_region.png`: Heatmap tương quan sức mua giữa các thể loại và các vùng lãnh thổ (Bắc Mỹ, Châu Âu, Nhật Bản...).
- `chart5_pie_region.png`: Pie chart hiển thị thị phần doanh số theo khu vực.

### Bước 5. Xây dựng mô hình
Mô hình được sử dụng là **Simple Linear Regression** (Hồi quy tuyến tính đơn biến) được lập trình thủ công hoàn toàn bằng `Numpy` trong file `model.py` (không dùng scikit-learn).
Pipeline huấn luyện gồm:
- Load dữ liệu và chia train/test theo tỷ lệ `80/20`.
- Sử dụng biến `Year` (Năm phát hành) làm feature đầu vào.
- Sử dụng `Global_Sales` làm biến mục tiêu (target).
- Huấn luyện mô hình (tính toán `slope` và `intercept` bằng công thức toán học ma trận).
- Viết hàm `predict` để dự đoán doanh số cho một năm bất kỳ.

### Bước 6. Đánh giá mô hình
Kết quả mô hình được đánh giá trên tập test bằng hệ số xác định $R^2$ Score thông qua hàm `score()`.
- Chức năng đánh giá được gọi thông qua script `main.py`.
- Mặc dù dữ liệu doanh số qua các năm có độ biến động rất mạnh (không hoàn toàn tuyến tính), mô hình cơ bản cung cấp một đường xu hướng gốc để hình dung đà tăng/giảm của thị trường qua thời gian dài.

## 5. Giải thích chi tiết các file trong project
### File dữ liệu
- `vgsales.csv`: Bộ dữ liệu gốc ban đầu chứa hơn 16.598 tựa game.
- `vgsales_clean.csv`: Dữ liệu đã được tiền xử lý và loại bỏ các dòng bị khuyết năm phát hành.
- `eda_outputs/`: Thư mục chứa các file `.csv` trích xuất dạng bảng tổng hợp từ quá trình thống kê phân tích (top 10 games, doanh số theo nền tảng/thể loại, v.v.).

### File mã nguồn
- `DataCleaning.py`: Script tiền xử lý dữ liệu, kiểm tra null, ép kiểu và sinh file sạch.
- `EDA.py`: Chứa các hàm gom nhóm, phân tích thống kê, in ra console và xuất bảng số liệu ra thư mục output.
- `bieudo.py`: Chứa mã nguồn để thiết lập style, màu sắc và vẽ 5 biểu đồ trực quan chính của dự án, sau đó lưu thành các file hình ảnh `.png`.
- `model.py`: Chứa logic thuật toán `SimpleLinearRegression` bao gồm fit, predict, score; cùng với các hàm load data và train test split từ đầu.
- `main.py`: Entrypoint của phần Modeling. Chạy file này để nhập năm cần dự đoán từ bàn phím và in ra kết quả mô hình.

### File kết quả (Hình ảnh biểu đồ)
- `chart1_line_yearly_sales.png`
- `chart2_bar_genre_sales.png`
- `chart3_bar_platform_sales.png`
- `chart4_heatmap_genre_region.png`
- `chart5_pie_region.png`

## 6. Cấu trúc thư mục thực tế
```text
BTL/
|-- .venv/
|-- vgsales.csv
|-- vgsales_clean.csv
|-- DataCleaning.py
|-- EDA.py
|-- bieudo.py
|-- model.py
|-- main.py
|-- README.md
|-- eda_outputs/
|   |-- game_count_by_year.csv
|   |-- sales_by_genre.csv
|   |-- sales_by_platform.csv
|   |-- sales_by_year.csv
|   |-- top_10_games.csv
|   `-- top_publishers.csv
|-- chart1_line_yearly_sales.png
|-- chart2_bar_genre_sales.png
|-- chart3_bar_platform_sales.png
|-- chart4_heatmap_genre_region.png
`-- chart5_pie_region.png
```

## 7. Cách chạy chương trình
### Cài đặt thư viện
Nếu không dùng môi trường ảo đi kèm, bạn có thể thiết lập bằng cách:
```bash
pip install pandas numpy matplotlib seaborn
```

### Bước 1: Làm sạch dữ liệu
```bash
python DataCleaning.py
```
*(Đọc từ `vgsales.csv` và sinh ra file sạch `vgsales_clean.csv`)*

### Bước 2: Thống kê số liệu & Xuất Biểu đồ
```bash
python EDA.py
python bieudo.py
```
*(Sẽ in ra các thống kê ở màn hình, đồng thời lưu 5 file ảnh biểu đồ `.png`)*

### Bước 3: Huấn luyện và Dự đoán
```bash
python main.py
```
*(Nhập năm bạn muốn dự đoán, ví dụ: 2026, chương trình sẽ in ra dự đoán tổng doanh số và điểm R² của mô hình).*

## 8. Kết luận
Project đã hoàn thành các yêu cầu chính:
- Có quy trình xử lý dữ liệu thiếu và chuẩn hóa bài bản.
- Có phân tích sự ảnh hưởng, biến động của doanh số với các yếu tố như năm, thể loại, nền tảng.
- Có trực quan hóa bằng hệ thống đa dạng các biểu đồ sinh động (Seaborn nâng cao).
- Có xây dựng mô hình dự đoán từ đầu.
- Có đánh giá mô hình khách quan qua độ chính xác R^2.

## 9. Thành viên nhóm 36
- Nguyễn Viết Phong (20220543)
- Phân tích dữ liệu (EDA)  Thực hiện phân tích tương quan (Correlation Analysis).

Nhiệm vụ:

Phân tích doanh số theo năm
Phân tích doanh số theo thể loại (Genre)
Phân tích doanh số theo nền tảng (Platform)
Tìm top game bán chạy nhất
Tổng hợp kết quả phân tích

👉 Kết quả: Bảng số liệu + nhận xét ban đầu
- Hoàng Quang Hợp (20220589)
- Data Cleaning & Chuẩn bị dữ liệu

Nhiệm vụ:

Thu thập và tải dataset từ Kaggle
Đọc và kiểm tra dữ liệu ban đầu
Xử lý dữ liệu thiếu (missing values)
Chuyển đổi kiểu dữ liệu (Year → int)
Loại bỏ dữ liệu trùng lặp
Xuất file dữ liệu đã làm sạch

👉 Kết quả: Dataset sạch (vgsales_clean.csv)

- Hoàng Mậu Phong(20220535)
- Trực quan hóa dữ liệu (Visualization)

Nhiệm vụ:

Vẽ biểu đồ:
Line chart (doanh số theo năm)
Bar chart (thể loại, platform)
Làm biểu đồ đẹp, dễ hiểu
(Optional) Sử dụng seaborn để nâng cao
Xuất hình ảnh biểu đồ để đưa vào báo cáo

👉 Kết quả: Hình ảnh biểu đồ (PNG)

- Hà Thị Thanh Tâm(20220551)
- Đánh giá mô hình (accuracy hoặc score)
Viết báo cáo tổng hợp:
Giới thiệu
Phương pháp
Kết quả
Insight

👉 Kết quả: File PDF + Slide

