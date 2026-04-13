import pandas as pd

# 1. Load dữ liệu
df = pd.read_csv("vgsales.csv")

print("Số dòng ban đầu:", len(df))

# 2. Kiểm tra giá trị thiếu (missing)
print("\nGiá trị thiếu:")
print(df.isnull().sum())

# 3. Xóa các dòng bị thiếu Year
df = df.dropna(subset=['Year'])

print("\nSau khi xóa dòng thiếu Year:", len(df))

# 4. Chuyển kiểu dữ liệu Year từ float → int
df['Year'] = df['Year'].astype(int)

print("\nKiểu dữ liệu sau khi chuyển:")
print(df.dtypes)

# 5. Kiểm tra dữ liệu trùng lặp
duplicate_count = df.duplicated().sum()
print("\nSố dòng bị trùng:", duplicate_count)

# 6. Xóa dòng trùng
df = df.drop_duplicates()

print("Sau khi xóa trùng:", len(df))

# 7. Kiểm tra lại dữ liệu sạch
print("\nThông tin dataset:")
print(df.info())

# 8. Lưu file sạch (optional)
df.to_csv("vgsales_clean.csv", index=False)

print("\n✅ Data Cleaning hoàn tất!")