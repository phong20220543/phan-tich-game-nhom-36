import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv("vgsales.csv")

# 2. Xem thông tin tổng quan
print("Thông tin dữ liệu:")
print(df.info())
print("\nDữ liệu mẫu:")
print(df.head())

# 3. Xóa dữ liệu trùng lặp
df = df.drop_duplicates()

# 4. Xử lý giá trị thiếu
# - Year: thay bằng median
df['Year'] = df['Year'].fillna(df['Year'].median())

# - Publisher: thay bằng 'Unknown'
df['Publisher'] = df['Publisher'].fillna('Unknown')

# 5. Ép kiểu dữ liệu
df['Year'] = df['Year'].astype(int)

# 6. Chuẩn hóa tên cột
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 7. Kiểm tra lại dữ liệu sau khi clean
print("\nSau khi làm sạch:")
print(df.info())

# 8. Kiểm tra outliers (ví dụ Global Sales > 50 triệu)
outliers = df[df['global_sales'] > 50]
print("\nOutliers:")
print(outliers)

# 9. Lưu file đã clean
df.to_csv("vgsales_cleaned.csv", index=False)

print("\nĐã lưu file vgsales_cleaned.csv")