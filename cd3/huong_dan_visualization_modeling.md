# Hướng Dẫn Visualization và Modeling

## 4. Visualization (Bắt buộc)

### Các biểu đồ bắt buộc:

#### 1. Line Chart - Doanh số theo năm
- Hiển thị xu hướng doanh số toàn cầu qua các năm
- Hỗ trợ phát hiện sự thay đổi thị trường theo thời gian
- Đặc điểm: tăng/giảm doanh số, điểm cao nhất/thấp nhất

#### 2. Bar Chart - Doanh số theo thể loại (Genre)
- So sánh doanh số giữa các thể loại game khác nhau
- Xác định thể loại có doanh số cao nhất
- Hỗ trợ quyết định đầu tư sản phẩm mới

#### 3. Bar Chart - Doanh số theo nền tảng (Platform)
- Phân tích hiệu suất các nền tảng chính (PS2, DS, Wii, PS3, v.v.)
- Top 10 nền tảng có doanh số cao nhất
- Giúp xác định nền tảng quan trọng nhất

### Nâng cao (Advanced):

#### 1. Biểu độ đẹp bằng Seaborn
- **Heatmap tương quan (Correlation Matrix)**: Hiển thị mối quan hệ giữa các biến số
  - Sử dụng colormap 'coolwarm' hoặc 'RdBu_r'
  - Có giá trị tương quan và ranh giới các ô

#### 2. (Optional) Pie Chart
- Tỷ lệ phần trăm doanh số theo thể loại
- Giúp thấy rõ thị phần của từng thể loại

## 5. Modeling - Phiên bản đơn giản (+1 đến +2 điểm)

### Mục tiêu
Xây dựng mô hình dự đoán đơn giản sử dụng **Linear Regression** với feature **Year**.

### Các bước:

#### 5.1 Chọn Feature (Lựa chọn đặc trưng)
```python
X = df[['Year']]  # Chỉ sử dụng Năm
y = df['Global_Sales']  # Target: Doanh số toàn cầu
```

#### 5.2 Train Linear Regression (Huấn luyện mô hình)
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
```
- Mô hình sẽ tìm ra đường thẳng tốt nhất để dự đoán doanh số dựa trên năm
- Output: Hệ số (coefficient) và hằng số (intercept)

#### 5.3 Predict (Dự đoán)
```python
y_pred = model.predict(X)
```
- Sử dụng mô hình đã huấn luyện để dự đoán doanh số

#### 5.4 In Score (Đánh giá hiệu suất)
Sử dụng các chỉ số:
- **MAE** (Mean Absolute Error): Sai số tuyệt đối trung bình
- **RMSE** (Root Mean Squared Error): Căn bậc hai sai số bình phương trung bình  
- **R²** (Coefficient of Determination): Độ phù hợp của mô hình (0-1, càng cao càng tốt)

### Ví dụ Output:
```
==================================================
Linear Regression (Feature: Year)
==================================================
  MAE  (Mean Absolute Error):      0.5234
  RMSE (Root Mean Squared Error):  0.7621
  R²   (Coefficient of Determination): 0.6543
==================================================
```

### Lợi ích của việc bổ sung mục này
- **+1 đến +2 điểm** trong đánh giá
- Cho thấy khả năng xây dựng và đánh giá mô hình machine learning
- Minh họa quy trình ML cơ bản: chọn feature → huấn luyện → dự đoán → đánh giá

### Kết quả tạo ra
- `visualizations_combined.png`: Tập hợp 4 biểu đồ chính
- `pie_chart_genre.png`: Biểu đồ tròn thể loại (optional)
- `actual_vs_predicted_simple.png`: Biểu đồ so sánh dự đoán thực tế

---

**Lưu ý**: Đây là phiên bản đơn giản của modeling. Phiên bản hoàn chỉnh sử dụng nhiều feature hơn và các mô hình phức tạp hơn (Random Forest, SVM, v.v.) được cài đặt trong `game_sales_analysis.py`.
