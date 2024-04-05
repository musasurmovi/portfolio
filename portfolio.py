import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(layout = "wide")
image = Image.open("assets\profile.PNG")  

# st.write("##")
# st.subheader("This is Musa :wave:")
# st.title("True Meridain")
# st.title("My portfolio website")
# st.write("This is test description for learnig streamlit app using python script")
# st.write("http://www.google.com")
# st.write("___")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation = 'horizontal'
    )

  

if selected == 'About':
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("MUSA BALTI")
            st.write(" I am a seasoned software developer with over four years of experience, transitioning my focus to frontend development. With a strong foundation in JavaScript, TypeScript, React, and Angular, I bring a wealth of expertise to crafting dynamic and user-centric interfaces. Leveraging my extensive experience, I am committed to delivering high-quality software solutions that meet and exceed user expectations")
        with  col2:
            st.title("Education")
            st.write("I hold a Bachelor's degree in Computer Science from FAST-NUCES, providing a solid foundation in software engineering principles and computer science fundamentals. My education at FAST-NUCES has equipped me with the necessary skills and knowledge to excel in the field of technology.")
        with  col3:
            st.title("Worked History")
            st.write(" I'm a Software Frontend Developer at True Meridian, where I specialize in crafting intuitive user interfaces. Working alongside a dynamic team, I contribute to innovative solutions tailored to meet client requirements and drive user engagement. My role allows me to leverage my expertise to deliver impactful software solutions.")

if selected == 'Projects':
    with st.container():
        st.write("https://muslimandquran.com/")            
        st.write("https://www.thepickvault.com/")            
            

if selected == 'Contact':
    
    contact_form = """
    <form action="https://formsubmit.co/musa.surmovi@email.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
    </form>
    """
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form,unsafe_allow_html = True)
    with right_col:
        st.image(image)

       
    


