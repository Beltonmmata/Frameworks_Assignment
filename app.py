import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

RAW_PATH = "metadata.csv"
CLEAN_PATH = "metadata_clean.csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CLEAN_PATH, low_memory=False)
    except FileNotFoundError:
        df = pd.read_csv(RAW_PATH, dtype=str, low_memory=False)
        df["publish_time"] = pd.to_datetime(df.get("publish_time"), errors="coerce")
        df["year"] = df["publish_time"].dt.year
        df = df.dropna(subset=["title", "publish_time"])
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research metadata")

min_year = int(df["year"].min())
max_year = int(df["year"].max())
year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))
top_n = st.slider("Top N Journals", 5, 30, 10)

filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications per year
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index.astype(int).astype(str), year_counts.values)
plt.xticks(rotation=45)
st.pyplot(fig)

# Top journals
st.subheader(f"Top {top_n} Journals")
top_journals = filtered["journal"].fillna("Unknown").value_counts().head(top_n)
fig, ax = plt.subplots()
top_journals.sort_values().plot(kind="barh", ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
text = " ".join(filtered["title"].dropna().astype(str).values)
if text.strip():
    wc = WordCloud(width=800, height=400, max_words=200).generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# Sample data
st.subheader("Sample Data")
st.dataframe(filtered[["title", "publish_time", "journal"]].head(100))
