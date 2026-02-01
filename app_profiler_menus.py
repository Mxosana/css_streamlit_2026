import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Teenage Pregnancy Data – South Africa",
    layout="wide"
)

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    [
        "Researcher Profile",
        "Data Explorer",
        "Publications",
        "Contact"
    ],
)

# --------------------------------------------------
# Dummy Teenage Pregnancy Data (South Africa)
# --------------------------------------------------
province_data = pd.DataFrame({
    "Province": [
        "Eastern Cape", "Free State", "Gauteng",
        "KwaZulu-Natal", "Limpopo",
        "Mpumalanga", "Northern Cape",
        "North West", "Western Cape"
    ],
    "Teen Pregnancy Rate (%)": [17.5, 15.2, 14.1, 18.9, 19.4, 16.8, 14.9, 16.1, 12.3],
    "Reported Cases (2024)": [34000, 18000, 42000, 56000, 39000, 21000, 9000, 15000, 13000]
})

age_group_data = pd.DataFrame({
    "Age Group": ["10–13", "14–15", "16–17", "18–19"],
    "Number of Pregnancies": [1200, 9800, 42000, 61000]
})

yearly_trend_data = pd.DataFrame({
    "Year": [2019, 2020, 2021, 2022, 2023, 2024],
    "Total Teen Pregnancies": [98000, 105000, 112000, 109000, 101000, 98000]
})

# --------------------------------------------------
# Researcher Profile
# --------------------------------------------------
if menu == "Researcher Profile":
    st.title("Researcher Profile")

    st.write("**Name:** Mr Mxosana")
    st.write("**Field of Research:** Mathematics")
    st.write("**Institution:** University of Fort Hare")

    st.image(
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
        caption="South Africa (Pixabay)"
    )

# --------------------------------------------------
# Data Explorer
# --------------------------------------------------
elif menu == "Data Explorer":
    st.title("Teenage Pregnancy Data Explorer")
    st.sidebar.header("Dataset Selection")

    data_option = st.sidebar.selectbox(
        "Select dataset",
        [
            "By Province",
            "By Age Group",
            "Yearly Trends"
        ]
    )

    # ----- Province Data -----
    if data_option == "By Province":
        st.subheader("Teenage Pregnancy by Province")
        st.dataframe(province_data)

        rate_filter = st.slider(
            "Filter by Pregnancy Rate (%)",
            10.0, 25.0, (10.0, 25.0)
        )

        filtered_data = province_data[
            province_data["Teen Pregnancy Rate (%)"].between(
                rate_filter[0], rate_filter[1]
            )
        ]

        st.dataframe(filtered_data)
        st.bar_chart(
            province_data.set_index("Province")["Teen Pregnancy Rate (%)"]
        )

    # ----- Age Group Data -----
    elif data_option == "By Age Group":
        st.subheader("Teenage Pregnancy by Age Group")
        st.dataframe(age_group_data)

        st.bar_chart(
            age_group_data.set_index("Age Group")["Number of Pregnancies"]
        )

    # ----- Yearly Trends -----
    elif data_option == "Yearly Trends":
        st.subheader("Yearly Pregnancy Trends")
        st.dataframe(yearly_trend_data)

        st.line_chart(
            yearly_trend_data.set_index("Year")["Total Teen Pregnancies"]
        )

# --------------------------------------------------
# Publications
# --------------------------------------------------
elif menu == "Publications":
    st.title("Publications")

    uploaded_file = st.file_uploader(
        "Upload a CSV file",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        keyword = st.text_input("Filter by keyword")
        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.dataframe(filtered)

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            st.bar_chart(
                publications["Year"].value_counts().sort_index()
            )

# --------------------------------------------------
# Contact
# --------------------------------------------------
elif menu == "Contact":
    st.header("Contact Information")
    st.write("Email: **lwandilemxosana@gmail.com**")
