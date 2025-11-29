import streamlit as st 
import pickle
import os

st.title('Social Media Mental Health Classification')

logo_path = 'parami.jpg'
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width = 150)

st.sidebar.markdown('**Student Name:** Khant Razar Kyaw')
st.sidebar.markdown('**Student ID:** PIUS20230009')
st.sidebar.markdown('**Project Name:** Mid-Term Machine Learning Web Project')

def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

st.header('Demographic Information')

s1 = st.number_input("What is the Participant's Age? (in years)", min_value = 0, max_value = 120, step = 1, value = 30)
s2 = st.selectbox("What is your Gender?", ['Male', 'Female', 'Other'])
s3 = st.selectbox("Which Social Media Platform do you use?", ['Facebook', 'TikTok', 'YouTube', 'WhatsApp', 'Snapchat', 'Instagram','Twitter'])

st.header('Digital Habits & Interactions')
s4 = st.slider("What is your daily Screen Time in minutes?", min_value = 0, max_value = 1500)
s5 = st.slider("What is your daily Social Media Time in minutes?", min_value = 0, max_value = 1500)

s6 = st.number_input("Negative Interactions Count", min_value=0, value=0)
s7= st.number_input("Positive Interactions Count", min_value=0, value=0)

st.header('Well Beings')

s8 = st.slider("How many hours do you sleep?", min_value = 0.0, max_value = 12.0, step=0.5, value = 7.0)
s9 = st.number_input("How many minutes do you do physical activties?", min_value=0, value=30)
    
s10 = st.slider("How do you rate your Anxiety Level from 0 to 10?", min_value = 0, max_value = 10, step = 1)
s11 = st.slider("How do you rate your Stress Level from 0 to 10?", min_value = 0, max_value = 10, step = 1)
s12 = st.slider("How do you rate your Mood Level from 0 to 10?", min_value = 0, max_value = 10, step = 1)

# for categorical variables
gender_dict = {'Female' : 0, 'Male' : 1, 'Other': 2}
platform_dict = {"Facebook": 0, "Instagram": 1, "Snapchat": 2, "TikTok": 3, "Twitter": 4, "WhatsApp": 5, "YouTube": 6}

gender_code = gender_dict.get(s2)
platform_code = platform_dict.get(s3)

# create images for target
status_images = {
    'Healthy': 'healthy.jpg',   
    'Stressed': 'stressed.jpg',
    'At_Risk': 'at_risk.jpg'}

# create guidelines
guidelines = {
    'Healthy': "Great job! Keep maintaining your balanced digital habits and healthy lifestyle.",
    'Stressed': "Consider taking a break from social media. Try to get more sleep and reduce screen time.",
    'At_Risk': "Please prioritize your well-being. Reach out to a professional or a trusted friend, and limit social media use significantly."
}


# create an user-input dataframe
if st.button("Predict Your Mental State"):
    input_arr = [[s1, gender_code, platform_code, s4, s5, s6, s7, s8, s9, s10, s11, s12]]
    model = load_model()
    result = model.predict(input_arr)
    target_names = ['At_Risk', 'Healthy', 'Stressed']
    final_result = target_names[result[0]]
    st.success(f"Your Mental State is {final_result}")

    if final_result in status_images and os.path.exists(status_images[final_result]):
        st.image(status_images[final_result], width=400)

    # Display Guidelines
    st.markdown("### 📋 Guidelines:")
    if final_result in guidelines:
        st.info(guidelines[final_result])
    








