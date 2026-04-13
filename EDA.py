from pathlib import Path

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


DATA_FILE = "vgsales_clean.csv"
OUTPUT_DIR = Path("eda_outputs")


def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df["Year"] = df["Year"].astype(int)
    return df


def setup_theme() -> None:
    sns.set_theme(style="whitegrid", context="talk")


def prepare_chart_data(data: pd.Series, x_name: str, y_name: str) -> pd.DataFrame:
    chart_data = data.reset_index()
    chart_data.columns = [x_name, y_name]
    return chart_data


def draw_bar_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
    color: str,
    top_n: int | None = None,
) -> None:
    plot_data = data.head(top_n) if top_n else data
    chart_data = prepare_chart_data(plot_data, xlabel, ylabel)

    plt.figure(figsize=(14, 7))
    ax = sns.barplot(data=chart_data, x=xlabel, y=ylabel, color=color)
    ax.set_title(title, fontsize=18, weight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)

    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", padding=3, fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.show()
    plt.close()


def draw_line_chart(
    data: pd.Series,
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
    color: str,
) -> None:
    chart_data = prepare_chart_data(data, xlabel, ylabel)

    plt.figure(figsize=(14, 7))
    ax = sns.lineplot(data=chart_data, x=xlabel, y=ylabel, marker="o", linewidth=3, color=color)
    ax.set_title(title, fontsize=18, weight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.show()
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    setup_theme()
    df = load_data(DATA_FILE)

    top_10_games: pd.DataFrame = df.nlargest(10, "Global_Sales")[["Name", "Platform", "Genre", "Global_Sales"]]
    sales_by_year: pd.Series = df.groupby("Year")["Global_Sales"].sum().sort_index()
    sales_by_genre: pd.Series = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
    sales_by_platform: pd.Series = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
    top_publishers: pd.Series = (
        df.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head(10)
    )
    game_count_by_year: pd.Series = df.groupby("Year").size().sort_index()

    print("\nTOP 10 GAME BAN CHAY NHAT")
    print(top_10_games.to_string(index=False))

    print("\nDOANH SO THEO NAM")
    print(sales_by_year.round(2).to_string())

    print("\nDOANH SO THEO THE LOAI")
    print(sales_by_genre.round(2).to_string())

    print("\nDOANH SO THEO PLATFORM")
    print(sales_by_platform.round(2).to_string())

    print("\nTOP PUBLISHER")
    print(top_publishers.round(2).to_string())

    print("\nSO LUONG GAME THEO NAM")
    print(game_count_by_year.to_string())

    top_10_games.to_csv(OUTPUT_DIR / "top_10_games.csv", index=False)
    prepare_chart_data(sales_by_year, "Year", "Global_Sales").to_csv(OUTPUT_DIR / "sales_by_year.csv", index=False)
    prepare_chart_data(sales_by_genre, "Genre", "Global_Sales").to_csv(OUTPUT_DIR / "sales_by_genre.csv", index=False)
    prepare_chart_data(sales_by_platform, "Platform", "Global_Sales").to_csv(
        OUTPUT_DIR / "sales_by_platform.csv", index=False
    )
    prepare_chart_data(top_publishers, "Publisher", "Global_Sales").to_csv(
        OUTPUT_DIR / "top_publishers.csv", index=False
    )
    prepare_chart_data(game_count_by_year, "Year", "Game_Count").to_csv(
        OUTPUT_DIR / "game_count_by_year.csv", index=False
    )

    draw_bar_chart(
        data=top_10_games.set_index("Name")["Global_Sales"],
        title="Top 10 Game Ban Chay Nhat",
        xlabel="Ten game",
        ylabel="Doanh so toan cau (trieu ban)",
        filename="top_10_games.png",
        color="#4c72b0",
    )
    draw_line_chart(
        data=sales_by_year,
        title="Doanh So Game Theo Nam",
        xlabel="Nam",
        ylabel="Tong doanh so toan cau (trieu ban)",
        filename="sales_by_year.png",
        color="#dd8452",
    )
    draw_bar_chart(
        data=sales_by_genre,
        title="Doanh So Theo The Loai",
        xlabel="The loai",
        ylabel="Tong doanh so toan cau (trieu ban)",
        filename="sales_by_genre.png",
        color="#55a868",
    )
    draw_bar_chart(
        data=sales_by_platform,
        title="Top 15 Platform Theo Doanh So",
        xlabel="Platform",
        ylabel="Tong doanh so toan cau (trieu ban)",
        filename="sales_by_platform.png",
        color="#c44e52",
        top_n=15,
    )
    draw_bar_chart(
        data=top_publishers,
        title="Top Publisher Theo Doanh So",
        xlabel="Publisher",
        ylabel="Tong doanh so toan cau (trieu ban)",
        filename="top_publishers.png",
        color="#8172b2",
    )
    draw_line_chart(
        data=game_count_by_year,
        title="So Luong Game Theo Nam",
        xlabel="Nam",
        ylabel="So luong game",
        filename="game_count_by_year.png",
        color="#937860",
    )

    print(f"\nDa luu bang tong hop va bieu do vao thu muc: {OUTPUT_DIR.resolve()}")
    print("Bieu do se hien truc tiep ra man hinh khi chay file.")


if __name__ == "__main__":
    main()
