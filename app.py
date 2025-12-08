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

df1 = pd.read_csv('social_media_mental_health.csv')

st.header('Demographic Information')

s1 = st.number_input("What is the Participant's Age? (in years)", df1.age.min(), df.age.max(), step = 1, value = 30)
s2 = st.selectbox("What is your Gender?", df.gender.unique().tolist())
s3 = st.selectbox("Which Social Media Platform do you use?", df1.platform.unique().tolist())

st.header('Digital Habits & Interactions')
s4 = st.slider("What is your daily Screen Time in minutes?", df1.daily_screen_time_min.min(), df1.daily_screen_time_min.max(), value = df1.daily_screen_time_min.mean())
s5 = st.slider("What is your daily Social Media Time in minutes?", min_value = 0, max_value = 1440)

s6 = st.number_input("Negative Interactions Count", min_value=0, value=0)
s7= st.number_input("Positive Interactions Count", min_value=0, value=0)

st.header('Well Beings')

s8 = st.slider("How many hours do you sleep?", min_value = 0.0, max_value = 24.0, step=0.5, value = 7.0)
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
    'Healthy': """
        ### 🌟 Keep up the Great Work!
        Your digital habits seem balanced. Here is how to maintain this:
        * Routine: Continue prioritizing your sleep (7+ hours).
        * Movement: Keep your physical activity levels up.
        * Mindfulness: Share your healthy habits with friends who might be struggling!
        """,
        
        'Stressed': """
        ### ⚠️ Time to De-compress
        You are showing signs of high stress. Let's fix that:
        * Digital Detox: Try staying off social media for the next 24 hours.
        * Screen Limit: Set a timer on your phone to limit apps to 30 mins/day.
        * Sleep Priority: No screens 1 hour before bed.
        * Activity: Go for a 15-minute walk outside without your phone.
        """,
        
        'At_Risk': """
        ### 🚨 Immediate Action Recommended
        Your mental well-being requires attention right now.
        * Seek Support: Please reach out to a counselor, therapist, or a trusted family member immediately.
        * Strict Limits: Delete the most stressful social media app from your phone for one week.
        * Stop Scrolling: Avoid negative interactions online completely.
        * You are not alone: Help is available. Please talk to someone today.
        """
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
    












