import streamlit as st
import random

def web_portalfolio():
    # Page configs
    #st.set_page_config(page_title="bavithra's  Portfolio")
    
    st.title("hi my name is bavithra ")
    

    


    # Sidebar navigation
    selected = st.sidebar.radio(
        "Select a Section", ["Education", "Contact", "Guessing Game"]
    )

    # Education Section
    if selected == "Education":
        with st.container():
            st.subheader("1 Year AI&DS Program")
            st.title("KGISL Institute Of Technology, Saravanampatti,coimbatore")
            st.title("About the programme")
            st.write("""
                Bachelor of Engineering in Artificial Intelligence and Data Science 
                (B.Tech.AI&DS) is an undergraduate degree program that focuses on the interdisciplinary field 
                of artificial intelligence (AI) and data science (DS). It is designed to provide students with
                a strong foundation in AI and DS technologies, along with the necessary programming, statistical,
                and mathematical skills to develop intelligent data-driven solutions for real time 

                This program prepares students to work on real-world AI problems and to advance their careers in 
                data science and AI engineering.
            """)
            st.write("_")

    # Contact Section
    elif selected == "Contact":
        with st.container():
            st.subheader("Get in Touch")
            

            st.write("*KGISL Institute of Technology*")
            st.write("Saravanampatti, Coimbatore")
            st.write("Phone: +91 8940292344")
            st.write("Email: info@kgkite.ac.in")
            st.write("Home adders:1/54,anna nagar ariyalur-621704")
            st.write("_")
        # Guessing Game Section
    elif selected == "Guessing Game":
        with st.container():
            st.subheader("Number Guessing Game")
            st.write("_")

            # Game setup
            if 'target_number' not in st.session_state:
                st.session_state.target_number = random.randint(1, 10)
                st.session_state.attempts = 0

            # Input for user's guess
            guess = st.number_input("Enter your guess from 1 to 10:", step=1, min_value=1, max_value=10)
            if st.button("Check Guess"):
                st.session_state.attempts += 1
                if guess < st.session_state.target_number:
                    st.warning("Try a higher number!")
                elif guess > st.session_state.target_number:
                    st.warning("Try a lower number!")
                else:
                    st.success(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
                    # Reset the game
                    st.session_state.target_number = random.randint(1, 10)
                    st.session_state.attempts = 0

            st.write("_")
                # Guessing Game Section
    elif selected == "Guessing Game":
        with st.container():
            st.subheader("Number Guessing Game")
            st.write("_")

            # Game setup
            if 'target_number' not in st.session_state:
                st.session_state.target_number = random.randint(1, 10)
                st.session_state.attempts = 0

            # Input for user's guess
            guess = st.number_input("Enter your guess from 1 to 10:", step=1, min_value=1, max_value=10)
            if st.button("Check Guess"):
                st.session_state.attempts += 1
                if guess < st.session_state.target_number:
                    st.warning("Try a higher number!")
                elif guess > st.session_state.target_number:
                    st.warning("Try a lower number!")
                else:
                    st.success(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
                    # Reset the game
                    st.session_state.target_number = random.randint(1, 10)
                    st.session_state.attempts = 0

            st.write("__")
            st.write("To reset the game, reload the page or keep guessing until you succeed.")

if __name__ == "__main__":
    web_portalfolio()
           