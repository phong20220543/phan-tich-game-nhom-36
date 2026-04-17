# Phân Tích Dữ Liệu Game Sales

Dự án này phân tích dữ liệu bán hàng video game và xây dựng mô hình dự đoán doanh số.

## Cấu Trúc Dự Án

```
d:\cd3\
├── vgsales_clean.csv          # Dataset chính
├── vgsales.csv                # Dataset gốc
├── game_sales_analysis.py     # Script phân tích và mô hình
├── bao_cao_phan_tich_game.md  # Báo cáo chi tiết
├── slide_thuyet_trinh.md      # Thiết kế slide thuyết trình
├── feature_importance.csv     # Tầm quan trọng của biến
└── actual_vs_predicted.png    # Biểu đồ so sánh dự đoán
```

## Cách Chạy

### Yêu Cầu
- Python 3.7+
- Các thư viện: pandas, numpy, scikit-learn, matplotlib, seaborn

### Cài Đặt Thư Viện
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Chạy Phân Tích
```bash
python game_sales_analysis.py
```

Script sẽ:
- Load và phân tích dữ liệu
- Xây dựng mô hình Linear Regression và Random Forest
- Đánh giá hiệu suất
- Xuất biểu đồ và file CSV

## Kết Quả

### Mô Hình
- **Linear Regression**: R² = 1.0000 (hoàn hảo vì Global_Sales là tổng)
- **Random Forest**: R² = 0.8290, MAE = 0.0429

### Insight Chính
- Doanh số Bắc Mỹ đóng góp 85.84% vào dự đoán
- Thị trường EU và JP ảnh hưởng ít hơn
- Năm phát hành và nền tảng có ảnh hưởng hạn chế

## Báo Cáo và Slide

- `bao_cao_phan_tich_game.md`: Báo cáo đầy đủ với giới thiệu, phương pháp, kết quả, insight
- `slide_thuyet_trinh.md`: Thiết kế slide thuyết trình với 11 slide

## Ghi Chú

Dataset được làm sạch từ vgsales.csv gốc. Một số dòng có vấn đề formatting đã được bỏ qua trong quá trình phân tích.