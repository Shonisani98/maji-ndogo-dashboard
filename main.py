import streamlit as st
import pandas as pd

# --- Load Data ---
data = pd.read_csv("data/water_access.csv")

# --- Layout ---
st.title("💧 Water Access Dashboard")
st.write("Explore household water access data by region and gain insights.")

st.header("📊 Dataset Overview")
st.dataframe(data.head())

# --- Interactive Filters ---
st.header("🔍 Filter by Region")
region = st.selectbox("Choose a region:", data["region"].unique())
filtered = data[data["region"] == region]
st.write(f"Data for {region}:")
st.dataframe(filtered)

# --- Visual Trends ---
st.header("📈 Visual Trends")

# Bar chart of households with water access by region
st.subheader("Households With Water Access")
st.bar_chart(data.set_index("region")["households_with_water"])

# Line chart example (if you have a 'year' column)
if "year" in data.columns:
    st.subheader("Trend Over Time")
    st.line_chart(data.groupby("year")["households_with_water"].sum())

# --- Insights ---
st.header("💡 Key Insights")
total_households = data["households_with_water"].sum() + data["households_without_water"].sum()
with_water = data["households_with_water"].sum()
without_water = data["households_without_water"].sum()
percent_with = round((with_water / total_households) * 100, 2)

st.metric("Total Households Surveyed", total_households)
st.metric("Households With Water Access", with_water)
st.metric("Households Without Water Access", without_water)
st.metric("Percentage With Water Access", f"{percent_with}%")


# Sidebar content
st.sidebar.title("Navigation")
st.sidebar.write("Choose an option below:")
option = st.sidebar.selectbox("Menu", ["Home", "About", "Download"])

# Main content
st.title("My Streamlit App")

if option == "Home":
    st.write("Welcome to the Home page!")

elif option == "About":
    st.write("This is a demo app with a sidebar and download button.")

elif option == "Download":
    st.write("Click below to download a sample file.")

    # Example file content
    sample_text = "Hello, this is a sample file.\nYou can customize this content."

    # Download button
    st.download_button(
        label="Download Sample File",
        data=sample_text,
        file_name="sample.txt",
        mime="text/plain"
    )
