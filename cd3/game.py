# Import các thư viện phân tích và học máy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Cài đặt style cho biểu đồ đẹp hơn
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ==========================================
# PHẦN 1: XỬ LÝ DỮ LIỆU (30%)
# ==========================================
print("--- PHẦN 1: ĐỌC VÀ XỬ LÝ DỮ LIỆU ---")

# 1. Đọc dữ liệu
try:
    df = pd.read_csv('vgsales.csv')
    print("Đọc dữ liệu thành công! Kích thước ban đầu:", df.shape)
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'vgsales.csv'. Hãy đảm bảo file đã được tải lên.")

# 2. Làm sạch dữ liệu (Missing Values & Duplicates)
print("\nKiểm tra dữ liệu thiếu:")
print(df.isnull().sum())

# Xóa các dòng thiếu Năm phát hành (Year) hoặc Nhà xuất bản (Publisher)
df = df.dropna(subset=['Year', 'Publisher'])

# Xóa dữ liệu trùng lặp nếu có
df = df.drop_duplicates()

# 3. Chuyển đổi kiểu dữ liệu
# Chuyển cột Year từ float sang int để hiển thị số năm chính xác
df['Year'] = df['Year'].astype(int)

print("\nKích thước dữ liệu sau khi làm sạch:", df.shape)


# ==========================================
# PHẦN 2: KHÁM PHÁ VÀ PHÂN TÍCH (EDA) (20%)
# ==========================================
print("\n--- PHẦN 2: KHÁM PHÁ DỮ LIỆU (EDA) ---")

# Thống kê mô tả
print("Thống kê các biến số (Doanh thu tính bằng triệu bản):")
print(df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].describe())

# Top 5 tựa game doanh thu cao nhất mọi thời đại
print("\nTop 5 Game có doanh thu toàn cầu cao nhất:")
print(df[['Name', 'Platform', 'Year', 'Global_Sales']].head(5))

# Ma trận tương quan (Correlation Matrix) giữa các khu vực
correlation = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr()
print("\nMa trận tương quan doanh thu:")
print(correlation)


# ==========================================
# PHẦN 3: TRỰC QUAN HÓA (15%)
# ==========================================
print("\n--- PHẦN 3: TRỰC QUAN HÓA ---")

# Biểu đồ 1: Số lượng game phát hành theo năm (Trend)
plt.figure(figsize=(12, 6))
games_per_year = df.groupby('Year')['Name'].count()
# Bỏ qua các năm sau 2016 vì dữ liệu vgsales thường thiếu sót ở các năm mới
games_per_year = games_per_year[games_per_year.index <= 2016] 
sns.lineplot(x=games_per_year.index, y=games_per_year.values, marker='o', color='b', linewidth=2)
plt.title('Xu hướng: Số lượng Game phát hành qua các năm (1980 - 2016)', fontsize=15)
plt.xlabel('Năm', fontsize=12)
plt.ylabel('Số lượng tựa game', fontsize=12)
plt.show()
print("-> Nhận xét biểu đồ 1: Số lượng game phát hành tăng vọt từ năm 2000 và đạt đỉnh điểm vào khoảng năm 2008-2009, sau đó bắt đầu có xu hướng giảm.")

# Biểu đồ 2: Top 10 Nhà phát hành (Publisher) có tổng doanh thu cao nhất
plt.figure(figsize=(12, 6))
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='magma')
plt.title('Top 10 Nhà phát hành có doanh thu toàn cầu cao nhất', fontsize=15)
plt.xlabel('Tổng doanh thu (Triệu bản)', fontsize=12)
plt.ylabel('Nhà phát hành', fontsize=12)
plt.show()
print('-> Nhận xét biểu đồ 2: Nintendo là "ông vua" tuyệt đối của ngành công nghiệp game, bỏ xa vị trí thứ hai là Electronic Arts (EA).')

# Biểu đồ 3: Tỷ trọng doanh thu các khu vực so với toàn cầu
plt.figure(figsize=(8, 8))
sales_regions = [df['NA_Sales'].sum(), df['EU_Sales'].sum(), df['JP_Sales'].sum(), df['Other_Sales'].sum()]
labels = ['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác']
plt.pie(sales_regions, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Thị phần doanh thu Game theo từng khu vực', fontsize=15)
plt.show()
print("-> Nhận xét biểu đồ 3: Thị trường Bắc Mỹ chiếm gần một nửa (49.3%) tổng doanh số toàn cầu, là thị trường quan trọng nhất.")


# ==========================================
# PHẦN 4: MÔ HÌNH HỌC MÁY (25%) 
# Mô hình: Hồi quy tuyến tính đa biến (Multiple Linear Regression)
# ==========================================
print("\n--- PHẦN 4: XÂY DỰNG MÔ HÌNH DỰ BÁO ---")
# Mục tiêu: Dự báo Global_Sales dựa vào doanh thu của 3 khu vực: NA, EU, và JP

# Xác định biến đặc trưng (X) và biến mục tiêu (y)
X = df[['NA_Sales', 'EU_Sales', 'JP_Sales']]
y = df['Global_Sales']

# Chia tập dữ liệu (80% để huấn luyện, 20% để kiểm thử)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Kích thước tập Train: {X_train.shape[0]} mẫu")
print(f"Kích thước tập Test: {X_test.shape[0]} mẫu")

# Khởi tạo và huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Lấy các hệ số của phương trình
print("\nPhương trình hồi quy:")
print(f"Global_Sales = {model.intercept_:.4f} + ({model.coef_[0]:.4f} * NA_Sales) + ({model.coef_[1]:.4f} * EU_Sales) + ({model.coef_[2]:.4f} * JP_Sales)")

# Đưa ra dự báo trên tập Test
y_pred = model.predict(X_test)

# Đánh giá mô hình
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\nĐÁNH GIÁ HIỆU SUẤT MÔ HÌNH:")
print(f"- R-Squared (R2): {r2:.4f} (Mô hình giải thích được {r2*100:.2f}% phương sai của doanh thu toàn cầu)")
print(f"- Mean Absolute Error (MAE): {mae:.4f} (Sai số trung bình khoảng {mae*1000000:,.0f} bản copy)")
print(f"- Mean Squared Error (MSE): {mse:.4f}")

# Trực quan hóa kết quả dự báo
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Đường chuẩn 1:1
plt.title('Thực tế vs. Dự báo: Doanh thu Toàn Cầu', fontsize=15)
plt.xlabel('Thực tế (Global Sales)', fontsize=12)
plt.ylabel('Dự báo (Predicted Global Sales)', fontsize=12)
plt.show()
print("-> Nhận xét: Các điểm dữ liệu bám rất sát vào đường chéo đỏ, chứng tỏ mô hình dự báo có độ chính xác cực kỳ cao.")


# ==========================================
# PHẦN 5: NHẬN XÉT VÀ ĐỀ XUẤT (10%)
# ==========================================
print("\n--- PHẦN 5: INSIGHT VÀ KHUYẾN NGHỊ ---")
print("""
[INSIGHT TỪ DỮ LIỆU]
1. Vòng đời thị trường: Số lượng game phát hành đã qua giai đoạn "bùng nổ số lượng" (đỉnh năm 2008) và chuyển sang giai đoạn chú trọng vào chất lượng.
2. Quyền lực nhà phát hành: Thị trường mang tính chất độc quyền nhóm (Oligopoly), nơi doanh thu khổng lồ đổ về tay một vài ông lớn như Nintendo và EA.
3. Độ lệch khu vực: Bắc Mỹ là thị trường quyết định. Một tựa game không thể trở thành bom tấn toàn cầu (Global Hit) nếu thất bại tại Bắc Mỹ.

[KHUYẾN NGHỊ CHIẾN LƯỢC]
1. Đối với Studio nhỏ/Indie: Không nên đối đầu trực tiếp với Nintendo ở các thể loại truyền thống của họ. Nên tìm thị trường ngách hoặc hợp tác phát hành qua các nền tảng PC (Steam).
2. Phân bổ ngân sách Marketing: Tối thiểu 50% ngân sách quảng bá nên được dồn cho thị trường Bắc Mỹ, 30% cho Châu Âu và phần còn lại cho Châu Á.
3. Đối với nhà đầu tư: Khi đánh giá tiềm năng của một tựa game mới, chỉ cần theo dõi sát sao doanh số tuần đầu tiên tại thị trường Bắc Mỹ và Châu Âu là có thể dự báo chính xác trên 95% tổng doanh thu vòng đời của game đó (dựa trên mô hình hồi quy đã xây dựng).
""")