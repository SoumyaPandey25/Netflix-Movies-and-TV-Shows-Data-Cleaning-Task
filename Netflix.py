import pandas as pd
import numpy as np

#load dataset
df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())

# Raw
df.to_excel("Raw_Data.xlsx", index=False)

#Missing values
# Fill missing director & cast with 'Unknown'
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')

# Drop rows where title is missing
df = df.dropna(subset=['title'])

#Remove Duplicates
df = df.drop_duplicates(subset=['title'])

#clean columns
text_cols = ['type', 'title', 'director', 'country', 'rating', 'listed_in']

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

#fix data
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

#add data quality
df['Data_Quality_Notes'] = "Cleaned: Missing values handled, duplicates removed"

#saving cleaning dataset
df.to_excel("Cleaned_dataset.xlsx", index=False)
df.to_csv("cleaned_dataset.csv", index=False)


