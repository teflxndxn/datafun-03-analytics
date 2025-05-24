import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from utils_logger import logger  # Your custom logger configuration
import text  # Import the new text module


def fetch_csv_file(url: str, save_path: str):
    logger.info(f"Fetching CSV data from {url}")
    df = pd.read_csv(url)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    logger.info(f"Saved CSV to {save_path}")
    return df


def load_data(local_path: str = "data/ebola_country_timeseries.csv") -> pd.DataFrame:
    logger.info(f"Loading data from {local_path}")
    df = pd.read_csv(local_path)
    logger.info(f"Loaded data with shape {df.shape}")
    print(f"Columns in CSV: {list(df.columns)}")
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data to long format...")

    cases = df.melt(id_vars=["Date", "Day"],
                    value_vars=[col for col in df.columns if col.startswith("Cases_")],
                    var_name="type_country", value_name="Cases")

    deaths = df.melt(id_vars=["Date", "Day"],
                     value_vars=[col for col in df.columns if col.startswith("Deaths_")],
                     var_name="type_country", value_name="Deaths")

    cases["Country"] = cases["type_country"].str.replace("Cases_", "")
    deaths["Country"] = deaths["type_country"].str.replace("Deaths_", "")

    combined = pd.merge(cases[["Date", "Day", "Country", "Cases"]],
                        deaths[["Date", "Day", "Country", "Deaths"]],
                        on=["Date", "Day", "Country"],
                        how="outer")

    logger.info(f"Transformed data shape: {combined.shape}")
    return combined


def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Analyzing total Ebola cases and deaths by country...")
    summary = df.groupby("Country")[["Cases", "Deaths"]].max().reset_index()
    print(summary)

    os.makedirs("data", exist_ok=True)
    summary.to_csv("data/ebola_summary_by_country.csv", index=False)
    summary.to_excel("data/ebola_summary_by_country.xlsx", index=False)
    summary.to_json("data/ebola_summary_by_country.json", orient="records", indent=2)
    logger.info("Saved summary to CSV, Excel, and JSON formats.")

    return summary


def plot_cases_over_time(df: pd.DataFrame):
    logger.info("Plotting Ebola cases over time for top 5 affected countries...")
    try:
        df["Date"] = pd.to_datetime(df["Date"])
        top_countries = df.groupby("Country")["Cases"].max().nlargest(5).index
        df_top = df[df["Country"].isin(top_countries)]

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_top, x="Date", y="Cases", hue="Country", marker="o")
        plt.title("Ebola Cases Over Time - Top 5 Affected Countries")
        plt.xlabel("Date")
        plt.ylabel("Cases")
        plt.legend(title="Country")
        plt.tight_layout()
        plt.savefig("ebola_cases_over_time.png")
        plt.show()
        logger.info("Saved plot as ebola_cases_over_time.png")
    except Exception as e:
        logger.error(f"Plotting error: {e}")


def plot_cases_vs_deaths(summary_df: pd.DataFrame):
    logger.info("Plotting total cases vs deaths by country...")

    plt.figure(figsize=(10, 6))
    bar_width = 0.4
    x = range(len(summary_df))

    plt.bar(x, summary_df["Cases"], width=bar_width, label="Cases", color="skyblue")
    plt.bar([i + bar_width for i in x], summary_df["Deaths"], width=bar_width, label="Deaths", color="salmon")

    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.title("Total Ebola Cases vs Deaths by Country")
    plt.xticks([i + bar_width / 2 for i in x], summary_df["Country"], rotation=45)
    plt.legend()
    plt.tight_layout()

    output_path = "ebola_cases_vs_deaths.png"
    plt.savefig(output_path)
    logger.info(f"Saved plot as {output_path}")
    plt.show()
    plt.close()


def main():
    logger.info("Starting Ebola data project")

    url = "https://raw.githubusercontent.com/cmrivers/ebola/master/country_timeseries.csv"
    csv_path = "data/ebola_country_timeseries.csv"

    fetch_csv_file(url, csv_path)
    df = load_data(csv_path)
    df_transformed = transform_data(df)
    summary = analyze_data(df_transformed)

    plot_cases_over_time(df_transformed)
    plot_cases_vs_deaths(summary)

    text.write_project_notes()  # <-- Added call to write the text notes file

    logger.info("Ebola data project completed.")


if __name__ == "__main__":
    main()
