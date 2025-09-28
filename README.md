# 🧾 Python Frameworks Assignment – CORD-19 Data Explorer

## 📌 Overview

This project is part of the **Python Frameworks Assignment**.  
The main goal is to practice **data analysis, visualization, and building a simple Streamlit application** using the `metadata.csv` file from the **CORD-19 dataset**.

I focused on:

- Loading and exploring a real-world dataset
- Cleaning missing or inconsistent data
- Creating meaningful visualizations
- Building an **interactive Streamlit web app**
- Documenting the workflow clearly

---

## 🎯 Learning Objectives

By completing this assignment, I learned to:

1. Load and explore data with **Pandas**
2. Apply basic data cleaning techniques
3. Generate clear, insightful visualizations with **Matplotlib & Seaborn**
4. Build a simple **Streamlit dashboard** with interactivity
5. Present data insights in a beginner-friendly manner

---

> ⚠️ **Important Note (Instructor):**  
> The dataset file **`metadata.csv`** is too large to upload directly to GitHub due to file size restrictions.  
> 👉 Before running this project, please **download and place `metadata.csv` manually** in the project root directory.
>
> You can obtain it from the official CORD-19 dataset:  
> [CORD-19 Metadata CSV (Download Link)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
>
> _(Extract the archive and copy `metadata.csv` into the project folder.)_
>
> ❌ Without this step, the **scripts and Streamlit app will not run successfully.**

## 📂 Project Structure

The project is intentionally flat (no nested folders) since there are minimal files:

Frameworks_Assignment/
│── metadata.csv # Raw dataset (input)
│── metadata_clean.csv # Cleaned dataset (auto-generated)
│── exploration.py # Data cleaning & visualization script
│── app.py # Streamlit app
│── README.md # This single documentation file
│── publications_by_year.png # Visualization (auto-generated)
│── top_journals.png # Visualization (auto-generated)
│── title_wordcloud.png # Visualization (auto-generated)

---

## ⚙️ Installation & Setup (Step by Step)

1️⃣ **Clone the repo** (or download ZIP & extract):

```bash
git clone https://github.com/Beltonmmata/Frameworks_Assignment.git
cd Frameworks_Assignment
```

2 **install dependancies**

```bash
pip install -r requirements.txt
```

3 **Data Exploration**

```bash
python exploration.py
```

3 **Streamlit Dashboard**

```bash
streamlit run app.py
```
