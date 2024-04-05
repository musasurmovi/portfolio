import streamlit as st
import pandas as pd
import numpy as np
def main():
    # Set the title of the app
    st.title("My First Streamlit App")

    # Add some text to the app
    st.write("Welcome to my Streamlit app!")

    # Add a sidebar
    st.sidebar.title("Sidebar")
    st.sidebar.write("This is a sidebar")

    # Add a checkbox to the sidebar
    option = st.sidebar.checkbox("Show/hide sidebar")
    if not option:
        st.sidebar.text("Sidebar is hidden")
    
    # Add a selectbox to the main app
    selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", selected_option)

    # Add a slider to the main app
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write("Slider value:", slider_value)
   # Set the title of the app
    st.title("Simple Chart Example")

    # Generate some example data
    data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10)
    })

    # Display the data
    st.write("Example Data:")
    st.write(data)

    # Create a line chart
    st.line_chart(data.set_index('x'))
if __name__ == "__main__":
    main()