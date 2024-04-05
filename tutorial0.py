import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
def main():
    

    

    st.title("True Meridian")

    # simple input field
    name = st.sidebar.text_input("inter your name", placeholder=  'Your name',)
    st.write(f"this is simpel app for, {name}!")
    st
    
    #checkbox
    gender = st.sidebar.radio("Select Gender", ("Male", "Female"))
    st.write(f"this is simpel app for, {gender}!")

    #selectbox 
    dropdownValue = ["value one", "value two", "value three"]
    dropdown = st.sidebar.selectbox("select value", dropdownValue)
    st.write(f"this is simpel app for, {dropdown}!")

    #testing checker
    state = st.sidebar.toggle("theme")
    st.write(f"on anf off", {state})

    if state:
        st.balloons()
    else:
        st.snow()

    st.title("pie chart")

    #data for pie chart
    labels = ['A', 'B', 'C', 'D', 'E']
    sizes = [15, 30, 45, 10, 32]

    fig, ax =plt.subplots()
    ax.pie(sizes, labels=labels, autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '')
    ax.axis('equal')
    st.pyplot(fig)


    
    # st.area_chart()
    st.spinner()
    st.toast("toast messagetest")
    st.button("submit", "info")
    
    slide = st.sidebar.slider("select")
    st.write(f"slider value", slide)

    sd = st.sidebar.progress("progress")
    st.write(f"slider value",sd)
if __name__ == "__main__":
    main()

 
