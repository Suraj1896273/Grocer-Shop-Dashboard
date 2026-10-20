
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Grocery Shop Dashboard",
    page_icon="🛒",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>

/* Main Page Spacing */
[data-testid="stAppViewBlockContainer"] {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}

/* Streamlit Header */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* Full-width Heading Background */
.title-container {
    width: 100vw;
    background-color: #F1F8E9 !important;
    text-align: center;
    padding: 10px 0;
    margin-top: -118px !important;
    margin-left: calc(50% - 50vw) !important;
    box-sizing: border-box;
}

/* Sidebar Menu Spacing */
[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 30px !important;
}

/* Menu Item Size */
[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-size: 10px !important;
    padding: 14px 12px !important;
    min-height: 50px;
}

/* Main Heading */
.dashboard-title {
    color: #8BC34A !important;
    background-color: #F1F8E9 !important;
    font-size: 40px !important;
    font-weight: bold !important;
    text-align: center;
    margin: 0 !important;
    padding: 0 !important;
}

/* Welcome Heading */
h3.welcome-heading {
    color: green !important;
    font-size: 45px !important;
    font-weight: bold !important;
    margin-left: -55px !important;
}

/* Welcome Caption */
p.welcome-caption {
    font-size: 20px;
    color: black;
    margin-left: 5px !important;
    margin-top: -10px !important;
}

/* Sidebar Background */
[data-testid="stSidebar"] {
    background-color: #F1F8E9 !important;
}

/* Sidebar Top Spacing */
[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    padding-top: 0rem !important;
}

/* Sidebar Row */
.sidebar-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0;
}

/* Sidebar Emoji */
.sidebar-emoji {
    font-size: 55px !important;
    line-height: 1.2;
    margin-top: -90px !important;
    margin-left: -15px !important;
    padding: 0 !important;
}

/* Sidebar Text */
.sidebar-text {
    display: flex;
    flex-direction: column;
    gap: 3px;
}

/* Sidebar Title */
.sidebar-title {
    font-size: 25px !important;
    color: green !important;
    margin-top: -80px !important;
    padding: 0 !important;
    white-space: nowrap;
}

/* Sidebar Subtitle */
.sales-subtitle {
    font-size: 17px !important;
    color: black !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Sidebar Menu */
.sidebar-menu {
    font-size: 30px !important;
    color: green;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Upload Message Background */
.upload_msg {
    background-color: white !important;
    color: black !important;
    padding: 12px;
    border-radius: 5px;
}

/* Alert Text */
[data-testid="stAlert"] p {
    color: black !important;
}

/* Common Card CSS */
.metric-total-sale,
.metric-total-products,
.metric-total-order,
.metric-most_payment_method {
    position: relative;
    width: 200px;
    height: 120px;
    border-radius: 5px !important;
    padding: 12px !important;
    box-sizing: border-box;
    overflow: hidden;
}

/* Total Sales Card */
.metric-total-sale {
    background-color: #F1F8E9 !important;
    border: 2px solid #F1F8E9 !important;
}

/* Total Products Card */
.metric-total-products {
    background-color: #EAE4F8 !important;
    border: 2px solid #EAE4F8 !important;
}

/* Total Quantity Card */
.metric-total-order {
    background-color: #DCEEFF !important;
    border: 2px solid #DCEEFF !important;
}

/* Payment Method Card */
.metric-most_payment_method {
    background-color: #FCE8D5 !important;
    border: 2px solid #FCE8D5 !important;
}

/* Card Logos */
.metric-sale-card-emoji,
.metric-total-products-card-emoji,
.metric-total-order-card-emoji,
.metric-most_payment_method-emoji {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 18px;
}

/* Card Headings */
.metric-total-sale p1,
.metric-total-products p1,
.metric-total-order p1,
.metric-most_payment_method p1 {
    display: block;
    color: black;
    font-size: 16px;
    margin: 0 !important;
    padding-left: 25px !important;
    text-align: left;
    white-space: nowrap;
}

/* Card Values */
.metric-total-sale h2,
.metric-total-products h2,
.metric-total-order h2,
.metric-most_payment_method h2 {
    color: black;
    font-size: 25px;
    margin: 0 !important;
    padding: 0 !important;
    position: absolute;
    top: 50%;
    left: 10px;
    right: 10px;
    transform: translateY(-50%);
    text-align: center;
    white-space: nowrap;
}

/* Card Descriptions */
.metric-total-sale p2,
.metric-total-products p2,
.metric-total-order p2,
.metric-most_payment_method p2 {
    display: block;
    color: black;
    font-size: 12px !important;
    position: absolute;
    bottom: 8px;
    left: 5px;
    right: 5px;
    margin: 0 !important;
    padding: 0 !important;
    text-align: center;
    white-space: nowrap;
}

</style>
""", unsafe_allow_html=True)


# Main Page Heading
st.markdown("""
<div class="title-container">
    <h2 class="dashboard-title">
        🥦 Grocery Shop Dashboard
    </h2>
</div>

<h3 class="welcome-heading">
    🍱 Welcome to Grocery Shop!
</h3>

<p class="welcome-caption">
    Here you can view your shop sales data, summary details.
</p>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.markdown("""
    <div class="sidebar-row">
        <span class="sidebar-emoji">🛒</span>
        <div class="sidebar-text">
            <span class="sidebar-title">Grocery Shop</span>
            <span class="sales-subtitle">
                Sales Analysis Dashboard
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar Menu
    st.markdown("""
        <p class="sidebar-menu">📋 Menu</p>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Select Menu",
        [
            "🏠 Home",
            "📊 Sales Analysis",
            "📦 Products",
            "💳 Payment Analysis",
        ],
        label_visibility="collapsed"
    )

    # Upload CSV
    file = st.file_uploader(
        "Upload Sales CSV",
        type=["csv"]
    )


# Check CSV File
if file is None:
    st.markdown("""
        <div class="upload_msg">
            📂 Please upload your sales CSV file.
        </div>
    """, unsafe_allow_html=True)

    st.stop()


# Read CSV
try:
    df = pd.read_csv(file)
except Exception:
    st.error("Unable to read CSV file. Please upload a valid CSV.")
    st.stop()


# Required Columns
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


# Check Missing Columns
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


# Calculate Dashboard Values
total_sale = df["total_amount_inr"].sum()

total_Products = df["product_name"].nunique()

# Total quantity of items sold
total_Order = df["quantity"].sum()

# Most Used Payment Method
if not df.empty:
    most_Payment = df["payment_mode"].value_counts().idxmax()
else:
    most_Payment = "N/A"


# HOME PAGE
if menu == "🏠 Home":

    crd1, crd2, crd3, crd4 = st.columns(4)

    # Total Sales Card
    with crd1:
        st.markdown(f"""
            <div class="metric-total-sale">
                <span class="metric-sale-card-emoji">🛒</span>
                <p1>Total Sales</p1>
                <h2>₹{total_sale:,.2f}</h2>
                <p2>Total amount of all orders</p2>
            </div>
        """, unsafe_allow_html=True)

    # Total Products Card
    with crd2:
        st.markdown(f"""
            <div class="metric-total-products">
                <span class="metric-total-products-card-emoji">📦</span>
                <p1>Total Products</p1>
                <h2>{total_Products:,.0f}</h2>
                <p2>Unique products sold</p2>
            </div>
        """, unsafe_allow_html=True)

    # Total Quantity Card
    with crd3:
        st.markdown(f"""
            <div class="metric-total-order">
                <span class="metric-total-order-card-emoji">🛍️</span>
                <p1>Total Quantity</p1>
                <h2>{total_Order:,.0f}</h2>
                <p2>Total items sold</p2>
            </div>
        """, unsafe_allow_html=True)

    # Most Used Payment Method
    with crd4:
        st.markdown(f"""
            <div class="metric-most_payment_method">
                <span class="metric-most_payment_method-emoji">💳</span>
                <p1>Top Payment Mode</p1>
                <h2>{most_Payment}</h2>
                <p2>Most used payment mode</p2>
            </div>
        """, unsafe_allow_html=True)

    # Display Dataset
    st.subheader("📋 Grocery Shop Sales Dataset")
    st.dataframe(df, use_container_width=True)


# SALES ANALYSIS PAGE
elif menu == "📊 Sales Analysis":

    st.subheader("📊 Sales Analysis")

    sales = df.groupby("product_name").agg(
        Total_Sales=("total_amount_inr", "sum"),
        Units_Sold=("quantity", "sum")
    ).reset_index()

    st.dataframe(sales, use_container_width=True)


# PRODUCTS PAGE
elif menu == "📦 Products":

    st.subheader("📦 Available Products")

    products = df.groupby(
        ["product_name", "category"]
    ).agg(
        Units_Sold=("quantity", "sum")
    ).reset_index()

    st.dataframe(products, use_container_width=True)


# PAYMENT ANALYSIS PAGE
elif menu == "💳 Payment Analysis":

    st.subheader("💳 Payment Analysis")

    payments = df.groupby("payment_mode").agg(
        Total_Transactions=("sale_id", "count"),
        Total_Sales=("total_amount_inr", "sum")
    ).reset_index()

    st.dataframe(payments, use_container_width=True)
