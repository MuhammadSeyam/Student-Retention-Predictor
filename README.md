# Student Retention Predictor

## Overview
This project analyzes student data to understand factors affecting student retention and performance. Using feature engineering and exploratory analysis, the project provides insights on student academic progress, financial needs, and completion rates. The final goal is to create a dataset ready for predictive modeling of student retention.

---

## Repository Structure

The repository contains the following files:

1. **1_Preprocessing.ipynb**  
   - The main Jupyter Notebook.  
   - Handles data cleaning, preprocessing, and feature engineering.  
   - Calculates new metrics like GPA, completion rates, financial ratios, and total earned hours.  

2. **Columns_Dictionary.ipynb**  
   - A reference notebook containing a dictionary describing each column.  
   - Explains the purpose of columns like `STUDENT IDENTIFIER`, `Major_Category`, `Need_Coverage_Ratio`, and academic metrics.  
   - Useful for understanding dataset structure and for analysis.  

3. **Student.xlsx**  
   - The raw student dataset used for preprocessing and analysis.  
   - Contains demographic, academic, and financial information.  

4. **Student_Done.csv**  
   - The processed and feature-engineered dataset exported from the main notebook.  
   - Includes calculated columns and ready-to-use metrics for analysis and visualization.  

---

## Key Features

- **Data Cleaning**: Handles missing values, inconsistent records, and outliers.  
- **Feature Engineering**: Calculates GPA, completion rates, net cost, financial difficulty, and major categories.  
- **Descriptive Insights**: Prepares metrics and ratios for visualization and analysis.  
- **Ready for Power BI**: The processed dataset can be directly used for dashboards and reporting.  

---

## Recommended Visualizations (Power BI)

- **Cards**: Key metrics like total students, total financial need, average GPA.  
- **Stacked Bar Charts**: Pass/Fail/Incomplete counts by major or term.  
- **Line Charts**: Trend of GPA or financial difficulty over terms.  
- **Clustered Column Charts**: Comparison of financial ratios or net costs by major or housing status.  
- **Pie/Donut Charts**: Distribution of students by major or in-state status.  
- **Tables/Matrices**: Detailed view of student-level or major-level metrics.  
- **Scatter Charts**: Analyze correlations between GPA and financial metrics.  
- **Funnel Charts**: Show student progression through attempted hours, earned hours, and retention.  

---

## How to Use

1. Open `1_Preprocessing.ipynb` in Jupyter Notebook or JupyterLab.  
2. Run all cells to process the raw dataset `Student.xlsx`.  
3. The processed dataset will be saved as `Student_Done.csv`.  
4. Use `Student_Done.csv` for analysis in Power BI or other visualization tools.  

---

## Notes

- The project is intended for educational and analytical purposes.  
- The dataset contains sensitive academic and financial data, so handle it responsibly.  

---

## Author

**Muhammad Seyam**  
- GitHub: [MuhammadSeyam](https://github.com/MuhammadSeyam)
