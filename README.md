🛒 Grocery Shop Sales Dashboard — Markdown Notes
1. Project Overview
This project is a Grocery Shop Sales Dashboard built using Python, Pandas, Streamlit, and CSS.

It helps users analyze grocery shop sales data by uploading a CSV file. The dashboard displays total sales, unique products, total quantity sold, and the most frequently used payment method.
2. Technologies Used
- Python: Main programming language.
- Pandas: Data analysis and calculations.
- Streamlit: Creates the interactive dashboard.
- CSS: Customizes colors, spacing, headings, and cards.
- CSV: Stores sales data.
3. Project Features
🏠 Home
- Displays total sales.
- Displays total unique products.
- Displays total quantity sold.
- Displays the most-used payment mode.
- Shows the complete sales dataset.
📊 Sales Analysis
Groups sales by product name and calculates total sales and units sold for each product.
📦 Products
Displays product names, categories, and total units sold.
💳 Payment Analysis
Displays the number of recorded transactions and total sales for each payment mode.
📂 CSV Upload
Allows users to upload a sales CSV file through the sidebar.

The application checks whether all required columns are available before displaying the dashboard.
4. Required CSV Columns
Column Name	Description
sale_id	Sale or transaction ID
date	Date of sale
product_name	Name of the product
category	Product category
quantity	Quantity sold
unit_price_inr	Price per unit
payment_mode	Payment method
total_amount_inr	Total sale amount
Example:
sale_id,date,product_name,category,quantity,unit_price_inr,payment_mode,total_amount_inr
SHOP001,16-02-2026,Coffee 100g,Food & Beverage,7,110,Credit Card,770
SHOP002,04-01-2026,Bread,Food & Beverage,5,30,Cash,150


5. Important Pandas Calculations
Total Sales
total_sale = df["total_amount_inr"].sum()



Adds the total sale amounts of all rows.
Total Products
total_Products = df["product_name"].nunique()



Counts the number of unique product names.
Total Quantity
total_Order = df["quantity"].sum()



Adds the quantity of all items sold.

Note: The variable name total_Order is misleading because it calculates total quantity, not the number of orders. A better name is total_quantity.
Most Used Payment Method
if not df.empty:    most_Payment = df["payment_mode"].value_counts().idxmax()else:    most_Payment = "N/A"



- value_counts() counts how frequently each payment mode appears.
- idxmax() returns the payment mode with the highest count.
- df.empty checks whether the dataset contains any rows.
6. Sales Analysis Code
sales = df.groupby("product_name").agg(    Total_Sales=("total_amount_inr", "sum"),    Units_Sold=("quantity", "sum")).reset_index()



Explanation:
- groupby() groups rows with the same product name.
- agg() performs calculations on each group.
- sum adds the sales amounts and quantities.
- reset_index() converts the product name into a regular column.
7. Products Analysis Code
products = df.groupby(    ["product_name", "category"]).agg(    Units_Sold=("quantity", "sum")).reset_index()



This groups the dataset by product name and category and calculates the total units sold for each group.

Note: This displays products found in sales records. It does not confirm whether products are currently in stock.
8. Payment Analysis Code
payments = df.groupby("payment_mode").agg(    Total_Transactions=("sale_id", "count"),    Total_Sales=("total_amount_inr", "sum")).reset_index()



This calculates the number of recorded sale rows and the total sales amount for each payment mode.

If one sale ID can appear multiple times, use "nunique" instead of "count" to count unique sale IDs.
9. CSS Styling
The dashboard uses CSS to customize its appearance.

Main colors:
- #F1F8E9 — Light green background.
- #8BC34A — Green heading.
- #EAE4F8 — Light purple card.
- #DCEEFF — Light blue card.
- #FCE8D5 — Light peach card.
CSS is used to style:
- Main heading.
- Sidebar background and menu.
- Welcome heading and caption.
- Dashboard metric cards.
- Card icons, values, and descriptions.
- CSV upload message.
Some CSS selectors depend on Streamlit's internal HTML structure and may need updates after a Streamlit upgrade.
10. How to Run the Project
First, install the required libraries:
pip install streamlit pandas


Save your Python code as app.py.

Run the project:
streamlit run app.py


The dashboard will open in your browser. Upload the required CSV file from the sidebar and select a menu option.
11. Project Folder Structure
grocery-shop-dashboard/
│
├── app.py
├── README.md
└── single_shop_sales_120_rows.csv


- app.py — Main Python application.
- README.md — Project documentation.
- single_shop_sales_120_rows.csv — Sample sales dataset.
When publishing on GitHub, use synthetic or sample data rather than private customer information.
12. Limitations
- The CSV must contain the required column names.
- Data types and invalid values are not fully validated.
- The dashboard does not currently contain graphs.
- There are no date or category filters.
- The products table does not track inventory.
- The payment analysis counts rows rather than necessarily counting unique transactions.
13. Future Improvements
- Add data validation and missing-value handling.
- Add date and category filters.
- Add graphs when needed.
- Improve error handling.
- Add a requirements.txt file.
- Deploy the dashboard online.
- Add automated tests.
14. Project Summary
The Grocery Shop Sales Dashboard is a beginner-friendly portfolio project that demonstrates Python programming, Pandas data analysis, CSV file handling, Streamlit dashboard development, and CSS customization.

It is a useful starting point for a Data Analytics or Data Science portfolio. Before presenting it as a professional business project, test it with different datasets and verify that all calculations are correct.
