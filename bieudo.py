import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\vgsales_clean.csv')

# Filter out sparse recent years
df = df[df['Year'] <= 2015]

# ── Palette & style ──────────────────────────────────────────────────────────
sns.set_theme(style="darkgrid", context="talk")
ACCENT   = "#7C3AED"
BG       = "#0F0F1A"
CARD     = "#1A1A2E"
TEXT     = "#E8E8F0"
GRID     = "#2A2A40"
PALETTE  = sns.color_palette("husl", 10)
GREEN    = "#10B981"
YELLOW   = "#F59E0B"

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 1 – Line chart: Global Sales by Year
# ─────────────────────────────────────────────────────────────────────────────
yearly = df.groupby('Year')['Global_Sales'].sum().reset_index()
yearly_genre = df.groupby(['Year', 'Genre'])['Global_Sales'].sum().reset_index()
top_genres = df.groupby('Genre')['Global_Sales'].sum().nlargest(5).index.tolist()

fig1, ax = plt.subplots(figsize=(14, 7))
fig1.patch.set_facecolor(BG)
ax.set_facecolor(CARD)
ax.tick_params(colors=TEXT)
for spine in ax.spines.values():
    spine.set_edgecolor(GRID)
ax.xaxis.label.set_color(TEXT); ax.yaxis.label.set_color(TEXT)
ax.title.set_color(TEXT)
ax.grid(color=GRID, linewidth=0.8)

# Shaded area + main line
ax.fill_between(yearly['Year'], yearly['Global_Sales'], alpha=0.15, color=ACCENT)
ax.plot(yearly['Year'], yearly['Global_Sales'],
        color=ACCENT, linewidth=3, marker='o', markersize=5, label='Total', zorder=5)

# Top-5 genre lines
palette_genre = sns.color_palette("husl", len(top_genres))
for i, genre in enumerate(top_genres):
    g = yearly_genre[yearly_genre['Genre'] == genre]
    ax.plot(g['Year'], g['Global_Sales'],
            linewidth=1.8, linestyle='--', marker='s', markersize=3,
            color=palette_genre[i], label=genre, alpha=0.85)

# Peak annotation
peak = yearly.loc[yearly['Global_Sales'].idxmax()]
ax.annotate(f"Dinh: {peak['Global_Sales']:.0f}M\n({int(peak['Year'])})",
            xy=(peak['Year'], peak['Global_Sales']),
            xytext=(peak['Year']+1.5, peak['Global_Sales']-50),
            arrowprops=dict(arrowstyle='->', color=TEXT, lw=1.5),
            color=TEXT, fontsize=11,
            bbox=dict(boxstyle='round,pad=0.3', fc=CARD, ec=ACCENT, lw=1.5))

ax.set_title('Doanh So Game Toan Cau Theo Nam (1980 - 2015)',
             fontsize=16, fontweight='bold', pad=18)
ax.set_xlabel('Nam', fontsize=13)
ax.set_ylabel('Doanh So (Trieu ban)', fontsize=13)
ax.set_xlim(yearly['Year'].min()-1, yearly['Year'].max()+1)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}M'))
legend = ax.legend(title='The loai', title_fontsize=11, fontsize=10,
                   facecolor=CARD, edgecolor=GRID, labelcolor=TEXT,
                   loc='upper left', framealpha=0.9)
legend.get_title().set_color(TEXT)

fig1.tight_layout()
fig1.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart1_line_yearly_sales.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 1 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 2 – Horizontal Bar chart: Doanh số theo Thể loại (Genre)
# ─────────────────────────────────────────────────────────────────────────────
genre_sales = (df.groupby('Genre')['Global_Sales'].sum()
                 .sort_values(ascending=True).tail(10))

fig2, ax = plt.subplots(figsize=(12, 7))
fig2.patch.set_facecolor(BG)
ax.set_facecolor(CARD)
for spine in ax.spines.values():
    spine.set_edgecolor(GRID)
ax.tick_params(colors=TEXT)
ax.xaxis.label.set_color(TEXT); ax.yaxis.label.set_color(TEXT)
ax.title.set_color(TEXT)
ax.grid(axis='x', color=GRID, linewidth=0.8)

colors = sns.color_palette("mako", len(genre_sales))[::-1]
bars = ax.barh(genre_sales.index, genre_sales.values,
               color=colors, edgecolor='none', height=0.65)

# Value labels
for bar, val in zip(bars, genre_sales.values):
    ax.text(val + 5, bar.get_y() + bar.get_height()/2,
            f'{val:.0f}M', va='center', ha='left', color=TEXT, fontsize=10)

ax.set_title('Tong Doanh So Theo The Loai Game (Top 10)',
             fontsize=16, fontweight='bold', pad=18)
ax.set_xlabel('Doanh So (Trieu ban)', fontsize=13)
ax.set_ylabel('The Loai', fontsize=13)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}M'))

fig2.tight_layout()
fig2.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart2_bar_genre_sales.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 2 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 3 – Bar chart: Doanh số theo Platform (Top 15)
# ─────────────────────────────────────────────────────────────────────────────
platform_sales = (df.groupby('Platform')['Global_Sales'].sum()
                    .sort_values(ascending=False).head(15))

fig3, ax = plt.subplots(figsize=(14, 7))
fig3.patch.set_facecolor(BG)
ax.set_facecolor(CARD)
for spine in ax.spines.values():
    spine.set_edgecolor(GRID)
ax.tick_params(colors=TEXT, axis='both')
ax.xaxis.label.set_color(TEXT); ax.yaxis.label.set_color(TEXT)
ax.title.set_color(TEXT)
ax.grid(axis='y', color=GRID, linewidth=0.8)

colors3 = sns.color_palette("rocket_r", len(platform_sales))
bars3 = ax.bar(platform_sales.index, platform_sales.values,
               color=colors3, edgecolor='none', width=0.7)

# Gradient highlight for #1
bars3[0].set_edgecolor(ACCENT)
bars3[0].set_linewidth(2.5)

# Value labels
for bar, val in zip(bars3, platform_sales.values):
    ax.text(bar.get_x() + bar.get_width()/2, val + 5,
            f'{val:.0f}M', ha='center', va='bottom', color=TEXT, fontsize=9.5)

ax.set_title('Tong Doanh So Theo Nen Tang (Platform) - Top 15',
             fontsize=16, fontweight='bold', pad=18)
ax.set_xlabel('Nen Tang', fontsize=13)
ax.set_ylabel('Doanh So (Trieu ban)', fontsize=13)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}M'))

fig3.tight_layout()
fig3.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart3_bar_platform_sales.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 3 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 4 – Heatmap: Genre vs Region Sales
# ─────────────────────────────────────────────────────────────────────────────
regions = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
region_labels = ['Bac My', 'Chau Au', 'Nhat Ban', 'Khac']
top10_genres = df.groupby('Genre')['Global_Sales'].sum().nlargest(10).index

heat_data = df[df['Genre'].isin(top10_genres)].groupby('Genre')[regions].sum()
heat_data.columns = region_labels
heat_data = heat_data.loc[df.groupby('Genre')['Global_Sales'].sum().nlargest(10).index]

fig4, ax = plt.subplots(figsize=(10, 7))
fig4.patch.set_facecolor(BG)
ax.set_facecolor(CARD)
ax.title.set_color(TEXT)

sns.heatmap(heat_data, ax=ax, annot=True, fmt='.0f', cmap='magma',
            linewidths=0.5, linecolor=GRID,
            annot_kws={'size': 11, 'color': 'white'},
            cbar_kws={'label': 'Trieu ban'})

ax.set_title('Doanh So Theo The Loai & Khu Vuc',
             fontsize=15, fontweight='bold', pad=18, color=TEXT)
ax.set_xlabel('Khu Vuc', fontsize=12, color=TEXT)
ax.set_ylabel('The Loai', fontsize=12, color=TEXT)
ax.tick_params(colors=TEXT)

cbar = ax.collections[0].colorbar
cbar.ax.tick_params(colors=TEXT)
cbar.ax.yaxis.label.set_color(TEXT)

fig4.tight_layout()
fig4.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart4_heatmap_genre_region.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 4 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 5 – Pie Chart: Thi phan doanh so theo khu vuc
# ─────────────────────────────────────────────────────────────────────────────
region_totals = {
    'Bac My':   df['NA_Sales'].sum(),
    'Chau Au':  df['EU_Sales'].sum(),
    'Nhat Ban': df['JP_Sales'].sum(),
    'Khac':     df['Other_Sales'].sum(),
}

fig5, ax = plt.subplots(figsize=(9, 7))
fig5.patch.set_facecolor(BG)
ax.set_facecolor(BG)

colors_pie = sns.color_palette("husl", len(region_totals))
wedges, texts, autotexts = ax.pie(
    region_totals.values(),
    labels=region_totals.keys(),
    autopct='%1.1f%%',
    colors=colors_pie,
    startangle=140,
    pctdistance=0.78,
    wedgeprops=dict(edgecolor=BG, linewidth=2.5),
    explode=(0.05, 0.05, 0.05, 0.05)
)

for text in texts:
    text.set_color(TEXT)
    text.set_fontsize(13)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

ax.set_title('Thi Phan Doanh So Theo Khu Vuc',
             fontsize=16, fontweight='bold', pad=20, color=TEXT)

fig5.tight_layout()
fig5.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart5_pie_region.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 5 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 6 – Doanh so tang manh giai doan 2000–2010
# ─────────────────────────────────────────────────────────────────────────────
df_focus = df[(df['Year'] >= 2000) & (df['Year'] <= 2010)]
yearly6 = df_focus.groupby('Year')['Global_Sales'].sum().reset_index()
yearly6['Growth'] = yearly6['Global_Sales'].pct_change() * 100

fig6, ax1 = plt.subplots(figsize=(14, 7))
fig6.patch.set_facecolor(BG)
ax1.set_facecolor(CARD)
for spine in ax1.spines.values():
    spine.set_edgecolor(GRID)
ax1.tick_params(colors=TEXT)
ax1.xaxis.label.set_color(TEXT)
ax1.yaxis.label.set_color(TEXT)
ax1.title.set_color(TEXT)
ax1.grid(color=GRID, linewidth=0.8, zorder=0)

# Vung to mau nen giai doan tang manh
ax1.axvspan(2004, 2008, alpha=0.08, color=GREEN, label='Giai doan tang manh')

# Cot bar doanh so
bars6 = ax1.bar(yearly6['Year'], yearly6['Global_Sales'],
                color=ACCENT, alpha=0.75, width=0.5,
                edgecolor='none', zorder=2, label='Doanh so (trieu ban)')

# To vang cho nam dinh (2008)
peak_idx = yearly6['Global_Sales'].idxmax()
bars6[peak_idx].set_color(YELLOW)
bars6[peak_idx].set_alpha(1.0)

# Value labels tren moi cot
for bar, val in zip(bars6, yearly6['Global_Sales']):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 8,
             f'{val:.0f}M', ha='center', va='bottom',
             color=TEXT, fontsize=10, fontweight='bold')

# Truc phu ben phai: % tang truong
ax2 = ax1.twinx()
ax2.set_facecolor(CARD)
ax2.tick_params(colors=TEXT)
ax2.yaxis.label.set_color(GREEN)
for spine in ax2.spines.values():
    spine.set_edgecolor(GRID)

ax2.plot(yearly6['Year'], yearly6['Growth'],
         color=GREEN, linewidth=2.5, marker='o',
         markersize=7, zorder=5, label='Tang truong (%)')

ax2.fill_between(yearly6['Year'], yearly6['Growth'], 0,
                 where=(yearly6['Growth'] >= 0),
                 alpha=0.15, color=GREEN)
ax2.fill_between(yearly6['Year'], yearly6['Growth'], 0,
                 where=(yearly6['Growth'] < 0),
                 alpha=0.15, color='red')

# Label % tang truong
for x, y in zip(yearly6['Year'], yearly6['Growth']):
    if pd.notna(y):
        color = GREEN if y >= 0 else 'tomato'
        ax2.text(x, y + 1.5, f'{y:+.1f}%',
                 ha='center', va='bottom', color=color,
                 fontsize=9, fontweight='bold')

ax2.axhline(0, color=GRID, linewidth=1, linestyle='--')
ax2.set_ylabel('Tang Truong (%)', fontsize=12)

# Annotations su kien quan trong
events = {
    2001: ('PS2\ndom thi truong', -60),
    2005: ('Xbox 360\nra mat',    -60),
    2006: ('Wii &\nPS3 ra mat',  -80),
    2008: ('DINH CAO\n679M ban',  30),
}
for year, (label, offset) in events.items():
    row = yearly6[yearly6['Year'] == year]
    if not row.empty:
        val = row['Global_Sales'].values[0]
        ax1.annotate(label,
                     xy=(year, val),
                     xytext=(year, val + offset),
                     ha='center', color=TEXT, fontsize=9,
                     arrowprops=dict(arrowstyle='->', color=TEXT, lw=1.2),
                     bbox=dict(boxstyle='round,pad=0.3', fc=CARD, ec=ACCENT, lw=1.2))

ax1.set_title('Doanh So Game Toan Cau Tang Manh Giai Doan 2000 - 2010',
              fontsize=16, fontweight='bold', pad=18, color=TEXT)
ax1.set_xlabel('Nam', fontsize=13)
ax1.set_ylabel('Doanh So (Trieu ban)', fontsize=13)
ax1.set_xticks(yearly6['Year'])
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:.0f}M'))
ax1.set_ylim(0, 800)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
legend6 = ax1.legend(lines1 + lines2, labels1 + labels2,
                     facecolor=CARD, edgecolor=GRID,
                     labelcolor=TEXT, fontsize=10,
                     loc='upper left', framealpha=0.9)

fig6.tight_layout()
fig6.savefig(r'C:\Users\Admin\PycharmProjects\Phantichgame_36\chart6_2000_2010.png',
             dpi=150, bbox_inches='tight', facecolor=BG)
print("Chart 6 saved.")

# ─────────────────────────────────────────────────────────────────────────────
# Hien thi tat ca bieu do
# ─────────────────────────────────────────────────────────────────────────────
print("\nTat ca bieu do da duoc xuat thanh cong!")
plt.show()