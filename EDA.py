# ==========================================
# CodeAlpha Task 2 - Exploratory Data Analysis (EDA)
# Quotes Dataset
# ==========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("quotes_dataset.csv")   

# ==========================================
# Basic Dataset Information
# ==========================================

print("\n" + "="*50)
print("FIRST 5 ROWS")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("DATASET INFORMATION")
print("="*50)
print(df.info())

print("\n" + "="*50)
print("DATASET SHAPE")
print("="*50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n" + "="*50)
print("COLUMN NAMES")
print("="*50)
print(df.columns.tolist())

# ==========================================
# Missing Values & Duplicates
# ==========================================

print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

print("\n" + "="*50)
print("DUPLICATE RECORDS")
print("="*50)
print(df.duplicated().sum())

# ==========================================
# Unique Values Analysis
# ==========================================

print("\n" + "="*50)
print("UNIQUE AUTHORS")
print("="*50)
print(df["Author"].nunique())

print("\n" + "="*50)
print("UNIQUE TAGS")
print("="*50)
print(df["Tags"].nunique())

# ==========================================
# Quote Length Analysis
# ==========================================

df["Quote_Length"] = df["Quote"].astype(str).apply(len)

print("\n" + "="*50)
print("QUOTE LENGTH STATISTICS")
print("="*50)
print(df["Quote_Length"].describe())

# ==========================================
# Top 10 Authors
# ==========================================

top_authors = df["Author"].value_counts().head(10)

print("\n" + "="*50)
print("TOP 10 AUTHORS")
print("="*50)
print(top_authors)

# ==========================================
# Top 10 Tags
# ==========================================

top_tags = df["Tags"].value_counts().head(10)

print("\n" + "="*50)
print("TOP 10 TAGS")
print("="*50)
print(top_tags)

# ==========================================
# Visualization Settings
# ==========================================

sns.set_style("whitegrid")

# ==========================================
# 1. Quote Length Distribution
# ==========================================

plt.figure(figsize=(10, 5))
sns.histplot(df["Quote_Length"], bins=30, kde=True)
plt.title("Distribution of Quote Length")
plt.xlabel("Quote Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ==========================================
# 2. Top 10 Authors
# ==========================================

plt.figure(figsize=(12, 6))
top_authors.plot(kind="bar")
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# 3. Top 10 Tags
# ==========================================

plt.figure(figsize=(12, 6))
top_tags.plot(kind="bar")
plt.title("Top 10 Tags")
plt.xlabel("Tags")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# 4. Quote Length Outlier Analysis
# ==========================================

plt.figure(figsize=(10, 4))
sns.boxplot(x=df["Quote_Length"])
plt.title("Quote Length Outlier Analysis")
plt.tight_layout()
plt.show()

# ==========================================
# Save Summary Report
# ==========================================

df.describe(include="all").to_csv("EDA_Summary_Report.csv")

# ==========================================
# Key Insights
# ==========================================

print("\n" + "="*50)
print("KEY INSIGHTS")
print("="*50)

print(f"Total Quotes: {len(df)}")
print(f"Unique Authors: {df['Author'].nunique()}")
print(f"Unique Tags: {df['Tags'].nunique()}")

print("\nMost Frequent Author:")
print(df["Author"].value_counts().head(1))

print("\nMost Frequent Tag:")
print(df["Tags"].value_counts().head(1))

print("\nEDA Completed Successfully!")
print("Summary report saved as 'EDA_Summary_Report.csv'")