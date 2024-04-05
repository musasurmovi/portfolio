import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Set the backend explicitly
plt.switch_backend('Agg')

def main():
     # Set the title of the app
    st.title("True Meridian Streamlit Test App")

    # First side menu
    st.sidebar.title("Menu 1")
    option1 = st.sidebar.radio("Select option", ["Option 1A", "Option 1B", "Option 1C"])

    # Second side menu
    st.sidebar.title("Menu 2")
    option2 = st.sidebar.checkbox("Enable Option 2")

    # Third side menu
    st.sidebar.title("Menu 3")
    option3 = st.sidebar.slider("Select value", 0, 10, 5)

    # Main content
    st.write("Selected Option from Menu 1:", option1)
    st.write("Option 2 Enabled:", option2)
    st.write("Selected Value from Menu 3:", option3)

     # Set the title of the app
    st.title(" Chart Selection and CSV Import")

    # Side menu for chart selection
    st.sidebar.title("Chart Selection")
    chart_option = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart"])

    # Side menu for CSV import
    st.sidebar.title("CSV Import")
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file is not None:
        st.sidebar.write("File uploaded successfully!")
        # Load the CSV file
        df = pd.read_csv(uploaded_file)
        # Display the DataFrame
        st.write("CSV Data:")
        st.write(df)

       # Display selected chart based on user choice
        if chart_option == "Line Chart":
            # Select columns for the line chart
            y_column = st.selectbox("Select column for y-axis", df.columns)
            st.write("Line Chart:")
            st.line_chart(df[y_column])  # Plot the selected column
        elif chart_option == "Bar Chart":
            # Select columns for the bar chart
            y_column = st.selectbox("Select column for y-axis", df.columns)
            st.write("Bar Chart:")
            st.bar_chart(df[y_column])  # Plot the selected column

            

if __name__ == "__main__":
    main()