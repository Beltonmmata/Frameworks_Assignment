import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

RAW_PATH = "metadata.csv"
CLEAN_PATH = "metadata_clean.csv"

def load_data():
    return pd.read_csv(RAW_PATH, dtype=str, low_memory=False)

def clean_data(df):
    df = df.copy()
    df["publish_time"] = pd.to_datetime(df.get("publish_time"), errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["abstract"] = df.get("abstract", "").fillna("")
    df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))
    df = df.dropna(subset=["title", "publish_time"])
    return df

def make_plots(df):
    # Publications per year
    year_counts = df["year"].value_counts().sort_index()
    plt.bar(year_counts.index.astype(int).astype(str), year_counts.values)
    plt.title("Publications by Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("publications_by_year.png")
    plt.close()

    # Top journals
    top_journals = df["journal"].fillna("Unknown").value_counts().head(15)
    top_journals.sort_values().plot(kind="barh", figsize=(8,6))
    plt.title("Top 15 Journals")
    plt.tight_layout()
    plt.savefig("top_journals.png")
    plt.close()

    # Word cloud of titles
    text = " ".join(df["title"].dropna().astype(str).values)
    if text.strip():
        wc = WordCloud(width=1600, height=800, max_words=200).generate(text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout()
        plt.savefig("title_wordcloud.png")
        plt.close()

def main():
    print("Loading data...")
    df = load_data()
    print("Initial shape:", df.shape)
    df = clean_data(df)
    print("Cleaned shape:", df.shape)
    df.to_csv(CLEAN_PATH, index=False)
    print(f"Cleaned data saved to {CLEAN_PATH}")
    make_plots(df)
    print("Plots saved: publications_by_year.png, top_journals.png, title_wordcloud.png")

if __name__ == "__main__":  
    main()
