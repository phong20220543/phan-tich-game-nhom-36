import pandas as pd

# =========================
# 1. Đọc dữ liệu
# =========================
df = pd.read_csv("vgsales_cleaned.csv")

# =========================
# 2. Kiểm tra dữ liệu
# =========================
print("INFO:")
print(df.info())

print("\nMISSING VALUES:")
print(df.isnull().sum())

# =========================
# 3. Phân tích theo năm
# =========================
sales_by_year = df.groupby('year')['global_sales'].sum().reset_index()

# Loại năm lỗi (year = 0 nếu có)
sales_by_year = sales_by_year[sales_by_year['year'] > 0]

print("\n=== SALES BY YEAR ===")
print(sales_by_year.head(10))
print("Max year sales:", sales_by_year['global_sales'].max())
print("Min year sales:", sales_by_year['global_sales'].min())

# =========================
# 4. Phân tích theo Genre
# =========================
sales_by_genre = (
    df.groupby('genre')['global_sales']
    .sum()
    .reset_index()
    .sort_values(by='global_sales', ascending=False)
)

print("\n=== SALES BY GENRE ===")
print(sales_by_genre)

# Top 3 thể loại
top3_genre = sales_by_genre.head(3)

# =========================
# 5. Phân tích theo Platform
# =========================
sales_by_platform = (
    df.groupby('platform')['global_sales']
    .sum()
    .reset_index()
    .sort_values(by='global_sales', ascending=False)
)

print("\n=== SALES BY PLATFORM ===")
print(sales_by_platform.head(10))

# Top 5 platform
top5_platform = sales_by_platform.head(5)

# =========================
# 6. Top game bán chạy
# =========================
top_games = (
    df[['name', 'platform', 'year', 'genre', 'global_sales']]
    .sort_values(by='global_sales', ascending=False)
    .head(10)
)

print("\n=== TOP 10 GAMES ===")
print(top_games)

# =========================
# 7. Correlation Analysis
# =========================
correlation = df[
    ['na_sales', 'eu_sales', 'jp_sales', 'other_sales', 'global_sales']
].corr()

print("\n=== CORRELATION MATRIX ===")
print(correlation)

# =========================
# 8. Insight nhanh (in ra)
# =========================
print("\n=== QUICK INSIGHTS ===")

print(f"- Thể loại bán chạy nhất: {top3_genre.iloc[0]['genre']}")
print(f"- Platform bán chạy nhất: {top5_platform.iloc[0]['platform']}")
print(f"- Game bán chạy nhất: {top_games.iloc[0]['name']}")

# =========================
# 9. Lưu kết quả ra file
# =========================
sales_by_year.to_csv("sales_by_year.csv", index=False)
sales_by_genre.to_csv("sales_by_genre.csv", index=False)
sales_by_platform.to_csv("sales_by_platform.csv", index=False)
top_games.to_csv("top_games.csv", index=False)
correlation.to_csv("correlation.csv")

print("\nĐã lưu toàn bộ kết quả ra file CSV!")