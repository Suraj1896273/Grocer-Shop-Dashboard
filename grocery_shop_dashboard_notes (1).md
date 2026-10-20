# Grocery Shop Sales Dashboard — Project Notes

## 1. Project Overview

**Project name:** Grocery Shop Sales Dashboard  
**Purpose:** Analyze grocery shop sales data using Python, Pandas, and Streamlit.  
**Interface:** Streamlit web dashboard with a light-green theme.  
**Charts:** Not included in the current version.

The dashboard allows a user to upload a CSV file and view sales summaries, product-wise sales, available products, and payment-method analysis.

## 2. Technologies Used

- **Python** — application logic
- **Pandas** — reading, grouping, and analyzing CSV data
- **Streamlit** — dashboard UI, file upload, navigation, and tables
- **HTML/CSS** — custom headings, sidebar styling, and summary cards
- **CSV** — sales data input format

## 3. Current Features

### CSV Upload
- Accepts CSV files through `st.file_uploader()`.
- Shows a prompt when no file has been uploaded.
- Attempts to read the uploaded file using `pd.read_csv()`.
- Displays an error if the CSV cannot be read.

### Required-Column Validation
The dashboard expects these columns:

| Column | Purpose |
|---|---|
| `sale_id` | Sale/transaction identifier |
| `date` | Sale date |
| `product_name` | Product name |
| `category` | Product category |
| `quantity` | Quantity sold |
| `unit_price_inr` | Unit price in INR |
| `payment_mode` | Payment method |
| `total_amount_inr` | Total amount for a sale row |

The code compares the required column names with `df.columns`. If any are missing, it displays the missing names and stops execution. If all required columns exist, it continues without showing a success message.

```python
required_columns = [
    "sale_id",
    "date",
    "product_name",
    "category",
    "quantity",
    "unit_price_inr",
    "payment_mode",
    "total_amount_inr"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error(
        f"Missing columns in CSV file: {', '.join(missing_columns)}"
    )
    st.write("Available columns:", list(df.columns))
    st.stop()
```

### Home Page
Displays four summary cards:

1. **Total Sales** — sum of `total_amount_inr`
2. **Total Products** — number of unique `product_name` values
3. **Total Quantity** — sum of `quantity`
4. **Top Payment Mode** — most frequent value in `payment_mode`

The Home page also displays the uploaded dataset in a table.

### Sales Analysis
Groups the data by `product_name` and calculates:
- `Total_Sales`: sum of `total_amount_inr`
- `Units_Sold`: sum of `quantity`

### Products
Groups by `product_name` and `category`, then calculates total `Units_Sold`.

### Payment Analysis
Groups by `payment_mode` and calculates:
- `Total_Transactions`: count of `sale_id` rows
- `Total_Sales`: sum of `total_amount_inr`

## 4. Important Calculation Notes

### Total Quantity is Not Total Orders
The current code uses:

```python
total_Order = df["quantity"].sum()
```

This calculates the **total number of items sold**, not the number of orders. The card label should therefore be `Total Quantity` (or `Total Items Sold`).

If `sale_id` represents a unique order ID, a possible order count is:

```python
total_orders = df["sale_id"].nunique()
```

Confirm the meaning of `sale_id` in the dataset before using this as the order count.

### Top Payment Mode
The code uses `value_counts().idxmax()` to find the most frequent payment mode:

```python
if not df.empty:
    most_Payment = df["payment_mode"].value_counts().idxmax()
else:
    most_Payment = "N/A"
```

This identifies the most common payment-mode value by row count. It does not identify the payment mode with the highest sales amount.

## 5. Styling Notes

The current design uses:
- Light-green background: `#F1F8E9`
- Green heading color: `#8BC34A`
- Light-purple Total Products card: `#EAE4F8`
- Light-blue Total Quantity card: `#DCEEFF`
- Light-orange Payment Mode card: `#FCE8D5`

The CSS styles the title band, welcome heading, sidebar, navigation labels, upload prompt, and four summary cards.

**Maintenance tip:** CSS selectors that depend on Streamlit's internal attributes (such as `data-testid`) and large negative margins may need adjustment when Streamlit versions or layouts change. Test the dashboard after upgrading Streamlit or changing screen sizes.

## 6. What to Improve Before Calling It Professional

### Data Quality and Validation
- Check that numeric columns such as `quantity`, `unit_price_inr`, and `total_amount_inr` contain valid numeric values.
- Handle missing values and duplicate records.
- Validate the date format.
- Decide how to handle zero or negative quantities and amounts.
- Check for blank product names and payment modes.

### Dashboard Usability
- Add filters for date range, category, product, and payment mode.
- Make the layout usable on different screen sizes.
- Use consistent labels and formatting.
- Keep the upload and validation messages clear.

### Performance and Reliability
- Consider `@st.cache_data` if repeated CSV processing becomes slow.
- Test with an empty CSV, missing columns, invalid numeric values, and a larger dataset.
- Avoid displaying sensitive customer or transaction information in a public demo.

### Project Presentation
- Add a clear `README.md`.
- Include a small sample CSV dataset with non-sensitive or synthetic data.
- Add screenshots of the dashboard.
- Document setup and run commands.
- Explain the calculations and assumptions.
- Optionally deploy the app so reviewers can try it.

## 7. Suggested Project Structure

```text
grocery-shop-dashboard/
├── app.py
├── data/
│   └── sample_sales.csv
├── screenshots/
│   └── dashboard.png
├── requirements.txt
└── README.md
```

Example `requirements.txt`:

```text
streamlit
pandas
```

Run locally with:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 8. Portfolio Readiness Checklist

- [ ] The dashboard runs without errors.
- [ ] Required-column validation works.
- [ ] Invalid and missing data are handled.
- [ ] Summary calculations are correct.
- [ ] Each sidebar page works.
- [ ] Labels accurately describe the calculations.
- [ ] The layout is checked at different screen sizes.
- [ ] README and setup instructions are included.
- [ ] Sample data and screenshots are included.
- [ ] The project is uploaded to GitHub.
- [ ] The project can be explained clearly in an interview.

## 9. How to Describe This Project

> Built a Grocery Shop Sales Dashboard using Python, Pandas, and Streamlit. Implemented CSV upload, required-column validation, sales summary cards, product-wise sales analysis, product availability summaries, and payment-method analysis.

Only claim features that are actually implemented. Add data cleaning, filters, testing, or deployment to this description after you build and verify them.
