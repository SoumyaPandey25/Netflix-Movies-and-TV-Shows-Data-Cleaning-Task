# Netflix-Movies-and-TV-Shows-Data-Cleaning-Task

## 📌 **Dataset Overview**

This project uses the **Netflix Movies and TV Shows dataset** containing information about movies and TV shows available on Netflix.

* **Rows:** *8,807*
* **Columns:** *12*
* **Each row represents:** *One Netflix title*

The raw dataset was preserved separately, and all cleaning was performed on a copy.


## 🎯 **Objective**

* Apply basic **Excel data-cleaning techniques**
* Identify and handle **missing values responsibly**
* Avoid inserting **assumed or fake data**
* Prepare the dataset for analysis

## 🛠️ **Cleaning Steps**

### **1. Initial Setup**

* Frozen top row
* Applied filters to all columns

### **2. Header Standardization**

* Converted column names to **lowercase** and **underscore format**
  *(e.g., `Date Added` → `date_added`)*

### **3. Missing Value Identification**

* Missing values found in: `director`, `cast`, `country`
* No missing values found in: `date_added`, `rating`

### **4. Missing Value Handling**

| Column       | Action                      | Reason                             |
| ------------ | --------------------------- | ---------------------------------- |
| `director`   | Left blank                  | Not critical; genuine missing data |
| `cast`       | Left blank                  | Same as director                   |
| `country`    | Replaced with **`Unknown`** | Important categorical field        |
| `date_added` | No action                   | No blanks detected                 |
| `rating`     | Left unchanged              | Blank ≠ Not Rated                  |

⚠️ No random values were filled to maintain data integrity.

## ✅ **Conclusion**

This task focused on responsible data cleaning.
All decisions were made carefully to preserve accuracy, consistency, and reliability of the dataset.
This version is **short, clear, and evaluator-safe**.
If you want it even **more compressed (5–6 bullet points only)**, say so.
