import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️",
    layout="centered"
)

# ---------- Sample data ----------
recommendations = {
    "12347": [
        ("21212", 96),
        ("23307", 72),
        ("22630", 72),
        ("21982", 72),
        ("22629", 60)
    ],
    
}

# ---------- Title ----------
st.title("🛍️ Product Recommendation System")
st.subheader("Model 3: User-Based Collaborative Filtering")

customer_id = st.text_input(
    "Enter Customer ID",
    "12346"
)

k = st.slider(
    "Number of Similar Users (k)",
    2,
    10,
    5
)

top_n = st.slider(
    "Number of Product Recommendations",
    1,
    10,
    5
)

if st.button("🔍 Recommend Products"):

    if customer_id in recommendations:

        data = recommendations[customer_id][:top_n]

        df = pd.DataFrame(
            data,
            columns=[
                "StockCode",
                "Recommendation Score"
            ]
        )

        st.success(
            f"Top {top_n} Product Recommendations for Customer ID {customer_id}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.error("Customer ID not found.")
