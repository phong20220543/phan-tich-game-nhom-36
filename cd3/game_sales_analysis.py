import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load data with proper parsing
df = pd.read_csv('vgsales_clean.csv', sep=',', quotechar='"', engine='python', on_bad_lines='skip')

# Clean column names and strip whitespace
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Basic cleaning
print("Data shape before cleaning:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values before cleaning:\n", df.isnull().sum())

# Drop duplicate rows
initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"Dropped {initial_rows - df.shape[0]} duplicate rows.")

# Convert numeric columns to proper dtypes
numeric_columns = ['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove invalid or missing numeric values
df = df.dropna(subset=numeric_columns + ['Platform', 'Genre', 'Publisher'])

# Remove rows with invalid years or negative sales values
df = df[df['Year'] >= 1950]
df = df[(df['NA_Sales'] >= 0) & (df['EU_Sales'] >= 0) & (df['JP_Sales'] >= 0) & (df['Other_Sales'] >= 0) & (df['Global_Sales'] >= 0)]

print("Data shape after cleaning:", df.shape)
print("Missing values after cleaning:\n", df.isnull().sum())

# Basic EDA
print("Data shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)
print("Missing values:\n", df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()

# Encode categorical variables
le_platform = LabelEncoder()
le_genre = LabelEncoder()
le_publisher = LabelEncoder()

df['Platform_encoded'] = le_platform.fit_transform(df['Platform'])
df['Genre_encoded'] = le_genre.fit_transform(df['Genre'])
df['Publisher_encoded'] = le_publisher.fit_transform(df['Publisher'])

# Features and target
features = ['Year', 'Platform_encoded', 'Genre_encoded', 'Publisher_encoded', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
X = df[features]
y = df['Global_Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)

# Model 2: Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Evaluation
def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    print(f"\n{model_name} Evaluation:")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²: {r2:.4f}")
    return mae, rmse, r2

lr_metrics = evaluate_model(y_test, lr_pred, "Linear Regression")
rf_metrics = evaluate_model(y_test, rf_pred, "Random Forest")

# Feature importance for Random Forest
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("\nFeature Importance (Random Forest):")
print(feature_importance)

# ============================================
# 4. VISUALIZATION (Bắt buộc)
# ============================================
print("\n" + "="*50)
print("4. VISUALIZATION")
print("="*50)

# Set style for seaborn
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 12)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Line chart: Doanh số theo năm
sales_by_year = df.groupby('Year')['Global_Sales'].sum().reset_index()
axes[0, 0].plot(sales_by_year['Year'], sales_by_year['Global_Sales'], marker='o', linewidth=2, color='#2E86AB')
axes[0, 0].set_xlabel('Năm', fontsize=12)
axes[0, 0].set_ylabel('Doanh số toàn cầu (triệu USD)', fontsize=12)
axes[0, 0].set_title('Doanh số theo năm', fontsize=14, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# 2. Bar chart: Doanh số theo thể loại
sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
axes[0, 1].bar(sales_by_genre.index, sales_by_genre.values, color='#A23B72')
axes[0, 1].set_xlabel('Thể loại', fontsize=12)
axes[0, 1].set_ylabel('Doanh số toàn cầu (triệu USD)', fontsize=12)
axes[0, 1].set_title('Doanh số theo thể loại', fontsize=14, fontweight='bold')
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Bar chart: Doanh số theo nền tảng (Top 10)
sales_by_platform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
axes[1, 0].barh(sales_by_platform.index, sales_by_platform.values, color='#F18F01')
axes[1, 0].set_xlabel('Doanh số toàn cầu (triệu USD)', fontsize=12)
axes[1, 0].set_ylabel('Nền tảng', fontsize=12)
axes[1, 0].set_title('Doanh số theo nền tảng (Top 10)', fontsize=14, fontweight='bold')

# 4. Seaborn heatmap: Biểu độ đẹp - Correlation (Nâng cao)
numeric_df = df[['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[1, 1], 
            cbar_kws={'label': 'Correlation'}, linewidths=0.5)
axes[1, 1].set_title('Ma trận tương quan (Biểu độ Seaborn)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations_combined.png', dpi=300, bbox_inches='tight')
print("✓ Lưu biểu đồ: visualizations_combined.png")
plt.show()

# Optional: Pie chart
fig_pie, ax_pie = plt.subplots(figsize=(10, 8))
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
colors = sns.color_palette("husl", len(genre_sales))
ax_pie.pie(genre_sales.values, labels=genre_sales.index, autopct='%1.1f%%', colors=colors, startangle=90)
ax_pie.set_title('Tỷ lệ doanh số theo thể loại', fontsize=14, fontweight='bold')
plt.savefig('pie_chart_genre.png', dpi=300, bbox_inches='tight')
print("✓ Lưu biểu đồ: pie_chart_genre.png")
plt.show()

# ============================================
# 5. MODELING - Phiên bản đơn giản (+1 đến +2 điểm)
# ============================================
print("\n" + "="*50)
print("5. MODELING - Phiên bản đơn giản (Linear Regression với Feature: Year)")
print("="*50)

# 5.1 Chọn feature: Year
print("\n5.1 Chọn Feature: Year")
X_simple = df[['Year']].values
y_simple = df['Global_Sales'].values
print(f"Feature: Year")
print(f"Target: Global_Sales")
print(f"Số dòng dữ liệu: {len(X_simple)}")

# 5.2 Train Linear Regression (Phiên bản đơn giản)
print("\n5.2 Train Linear Regression Model")
lr_simple = LinearRegression()
lr_simple.fit(X_simple, y_simple)
print(f"✓ Model đã được huấn luyện")
print(f"  Coefficient (Hệ số): {lr_simple.coef_[0]:.6f}")
print(f"  Intercept (Hằng số): {lr_simple.intercept_:.6f}")

# 5.3 Predict
print("\n5.3 Predict trên toàn bộ dữ liệu")
y_pred_simple = lr_simple.predict(X_simple)
print(f"✓ Dự đoán hoàn tất")
print(f"  Số dự đoán: {len(y_pred_simple)}")

# 5.4 In score (Đánh giá mô hình)
print("\n5.4 In Score - Đánh giá mô hình")
mae_simple = mean_absolute_error(y_simple, y_pred_simple)
rmse_simple = np.sqrt(mean_squared_error(y_simple, y_pred_simple))
r2_simple = r2_score(y_simple, y_pred_simple)

print(f"\n{'='*50}")
print(f"Linear Regression (Feature: Year)")
print(f"{'='*50}")
print(f"  MAE  (Mean Absolute Error):  {mae_simple:.4f}")
print(f"  RMSE (Root Mean Squared Error): {rmse_simple:.4f}")
print(f"  R²   (Coefficient of Determination): {r2_simple:.4f}")
print(f"{'='*50}")

# Visualization: Actual vs Predicted
fig_pred, ax_pred = plt.subplots(figsize=(10, 6))
ax_pred.scatter(df['Year'], y_simple, alpha=0.5, label='Actual', color='blue')
ax_pred.plot(df['Year'], y_pred_simple, 'r-', linewidth=2, label='Predicted')
ax_pred.set_xlabel('Năm (Year)', fontsize=12)
ax_pred.set_ylabel('Doanh số toàn cầu (Global Sales)', fontsize=12)
ax_pred.set_title('Linear Regression: Actual vs Predicted (Feature: Year)', fontsize=14, fontweight='bold')
ax_pred.legend(fontsize=11)
ax_pred.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('actual_vs_predicted_simple.png', dpi=300, bbox_inches='tight')
print("\n✓ Lưu biểu đồ: actual_vs_predicted_simple.png")
plt.show()

print("\n" + "="*50)
print("Hoàn tất! (Có phần 5.Modeling = +1 đến +2 điểm)")
print("="*50)

# Visualization

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=rf_pred)
plt.xlabel('Actual Global Sales')
plt.ylabel('Predicted Global Sales')
plt.title('Actual vs Predicted Global Sales (Random Forest)')
plt.savefig('actual_vs_predicted.png')
plt.show()

# Save results
results = {
    'Linear Regression': lr_metrics,
    'Random Forest': rf_metrics
}

# Save feature importance
feature_importance.to_csv('feature_importance.csv', index=False)