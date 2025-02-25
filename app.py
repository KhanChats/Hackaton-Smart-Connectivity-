import streamlit as st
import pandas as pd
import numpy as np

# Generate sample CSV data
data = {
    "Timestamp": pd.date_range(start="2025-02-26 10:00", periods=10, freq="H"),
    "Temperature (°C)": np.random.uniform(15, 30, 10),
    "Humidity (%)": np.random.uniform(30, 80, 10),
    "Light Intensity (lux)": np.random.uniform(100, 1000, 10),
    "Air Quality (ppm)": np.random.uniform(10, 150, 10),
}

# Create DataFrame and save as CSV
df = pd.DataFrame(data)
csv_file = "sensor_test_data.csv"
df.to_csv(csv_file, index=False)

# Streamlit App Layout
st.title("Хакатон Умна Свързаност - Дашборд")
st.header("Тестови данни от сензори")

# Display CSV Data
st.dataframe(df)

# File Download Option
st.download_button(
    label="Изтегли CSV файла",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="sensor_test_data.csv",
    mime="text/csv",
)

st.sidebar.header("Филтриране на данни")
selected_time = st.sidebar.selectbox(
    "Избери време", df["Timestamp"].astype(str).unique()
)

# Filter and display selected data details
filtered_df = df[df["Timestamp"].astype(str) == selected_time]
st.write("### Данни за избраното време")
st.table(filtered_df)
