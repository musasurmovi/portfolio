import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read CSV file and return DataFrame
def read_csv(file):
    df = pd.read_csv(file)
    return df

# Function to display chart
def display_chart(df, x_column, y_column):
    # Plot chart
    sns.lineplot(data=df, x=x_column, y=y_column)
    plt.title('Line Chart')
    plt.xlabel('X Axis Label ID')
    plt.ylabel('Y Axis Label Age')

    # Show plot in modal
    st.pyplot()

# Main function to run the Streamlit app
def main():
    st.title('CSV Data Visualization')

    # File uploader
    file = st.file_uploader('Upload CSV', type=['csv'])

    # Button to plot chart
    if file is not None:
        df = read_csv(file)
        
        # Dropdowns to select columns for plotting
        x_column = st.selectbox("Select X-axis colum ID", df.columns)
        y_column = st.selectbox("Select Y-axis column Age", df.columns)

        # Check if button is clicked
        if st.button('Plot Chart'):
            # Display chart in modal
            st.markdown('<h2 style="text-align: center;">Chart</h2>', unsafe_allow_html=True)
            with st.expander("Chart Details", expanded=True):
                display_chart(df, x_column, y_column)

if __name__ == "__main__":
    main()
