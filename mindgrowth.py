import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="🔥 Ignite My Passion! 💡", page_icon="🌟", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        * { font-family: 'Poppins', sans-serif; }
        body { background-color: #f4f7fc; color: #333; }
        .title { 
            font-size: 50px; 
            font-weight: bold; 
            text-align: center; 
            background: linear-gradient(90deg, #6A11CB, #3f51b5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px; 
            animation: fadeIn 2s ease-in-out; 
        }
        .subheader { 
            font-size: 26px; 
            font-weight: 600; 
            text-align: center; 
            color: #3f51b5;
            margin-bottom: 15px; 
            border-bottom: 3px solid #6A11CB; 
            padding-bottom: 10px; 
            animation: slideIn 1.5s ease-in-out; 
        }
        .quote-box, .success-box { 
            border-radius: 15px; 
            padding: 18px; 
            text-align: center; 
            font-weight: bold; 
            margin-bottom: 20px; 
            animation: fadeIn 2s ease-in-out; 
        }
        .quote-box { 
            background-color: #fffae5; 
            border-left: 8px solid #ff9800; 
            color: #444; 
        }
        .success-box { 
            background-color: #e5ffe5; 
            border-left: 8px solid #2e7d32; 
            color: #1b5e20; 
        }
        .footer { 
            font-size: 18px; 
            color: white; 
            text-align: center; 
            padding: 20px;
            margin-top: 30px; 
            background: linear-gradient(90deg, #6A11CB, #3f51b5);
            border-radius: 10px; 
            font-weight: bold; 
            animation: fadeIn 2s ease-in-out; 
        }
        .stButton>button { 
            background: linear-gradient(90deg, #6A11CB, #3f51b5);
            color: white; 
            font-size: 18px; 
            font-weight: bold; 
            border: none; 
            border-radius: 5px; 
            padding: 10px 20px; 
            cursor: pointer; 
            transition: transform 0.3s ease; 
            margin-top: 10px; /* Added margin to move buttons down */
        }
        .stButton>button:hover { 
            transform: scale(1.1); 
        }
        @keyframes fadeIn { 
            from { opacity: 0; } 
            to { opacity: 1; } 
        }
        @keyframes slideIn { 
            from { transform: translateX(-100%); } 
            to { transform: translateX(0); } 
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'> 🔥 Ignite My Passion! 💡</h1>", unsafe_allow_html=True)
#🔥 Unstoppable Mindset: Fuel Your Greatness! 🚀
quotes = [
    "Believe in yourself, take on your challenges, and dig deep within to conquer fears. — Chantal Sutherland",
    "Your only limit is your mind. Push beyond, and success is inevitable! — Unknown",
    "Small daily improvements are the key to staggering long-term results. — Robin Sharma",
    "Success is getting up one more time than you fall. Keep rising! — Vince Lombardi",
    "Doubt kills more dreams than failure ever will. Take the leap! — Suzy Kassem",
    "Discipline is the bridge between goals and accomplishments. Stay consistent! — Jim Rohn",
    "Greatness is not in never falling, but in rising every time we fall. — Confucius",
    "You are stronger than you think. Keep pushing forward! — Unknown",
    "What you get by achieving your goals is not as important as what you become by achieving them. — Zig Ziglar",
    "Make today so amazing that yesterday gets jealous! — Unknown"
]
st.markdown("<h2 class='subheader'>💡 Motivations </h2>", unsafe_allow_html=True)

#  "Empower me!" button
st.write("")  
if st.button("✨ Empower Me!"):
    st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# top priority
st.markdown("<h2 class='subheader'>💪 Take Charge of Your Journey</h2>", unsafe_allow_html=True)
goal = st.text_input("What is your top priority?")
if goal:
    st.success(f"🚀 Goal Set: *{goal}*. Stay determined and make progress every day!")


challenges = [
    "Expand your knowledge—learn something new and share it!",
"Break boundaries—embrace a new challenge today!",
"Take 15 minutes to reflect on your journey and growth.",
"Cultivate gratitude—list three things that made you smile today!",
"Clear your space, clear your mind—organize and refresh!"
]
st.markdown("<h2 class='subheader'>🚀 Maximize Your Efficiency</h2>", unsafe_allow_html=True)


st.write("")  
if st.button("🚀 Take on a Task!"):
    st.info(f"💡 *Challenge:* {random.choice(challenges)}")

st.markdown("<h2 class='subheader'>✨ Unlock Inner Wisdom</h2>", unsafe_allow_html=True)
reflection = st.text_area("What's something you want to reflect on?:")
if reflection:
    st.success(f"💡 *Insightful Reflection:* {reflection}")


st.markdown("<h2 class='subheader'>🏅 Embrace Your Achievements</h2>", unsafe_allow_html=True)
achievement = st.text_input("Share a recent win:")
if achievement:
    st.markdown(f"<div class='success-box'>🎉 winer : {achievement}</div>", unsafe_allow_html=True)


st.markdown("<h2 class='subheader'>📈 Elevate Your Knowledge</h2>", unsafe_allow_html=True)
quiz_question = "How frequently do you step outside your comfort zone?"
quiz_answers = ["Hardly ever", "Occasionally" , "Regularly", "All the time"]
quiz_choice = st.radio(quiz_question, quiz_answers)
if st.button("Submit "):
    feedback = {
        "Hardly ever": "Growth starts with small steps—take one today!",
    "Occasionally": "You're on the right track! Keep challenging yourself.",
    "Regularly": "Great job! Consistency is key to continuous improvement.",
    "All the time": "Amazing! Your dedication to growth is truly inspiring!"}
    st.success(feedback[quiz_choice])


st.markdown("<h2 class='subheader'>🌟  Achievements </h2>", unsafe_allow_html=True)
if "success_wall" not in st.session_state:
    st.session_state.success_wall = []
success_message = st.text_input("Share Your Achievement:")
if st.button("win"):
    if success_message:
        st.session_state.success_wall.append(success_message)
        st.success("🎉 Your achievement has been shared!")

if st.session_state.success_wall:
    for story in st.session_state.success_wall:
        st.markdown(f"<div class='success-box'>{story}</div>", unsafe_allow_html=True)


st.markdown("<h2 class='subheader'>🚀 Keep Your Momentum Going</h2>", unsafe_allow_html=True)
reminders = [
"Each step you take brings you closer to greatness. Keep going! 🚀"
"Your dedication today shapes your success tomorrow! 🌟"
"Consistency fuels progress—show up and shine! 💪"
"Every setback is a setup for a comeback. Keep striving! 🔥"
"Great achievements require time and perseverance. Stay the course! ⏳"
]
if st.button("⏰ Boost My Motivation!"):
    st.success(random.choice(reminders))

# Footer
st.markdown("""
<div class='footer'>
🚀Embrace your journey every challenge faced, every effort made, and every lesson learned brings you closer to greatness! 🌟🔥❤️🌟<br>
<strong>Created by Ayesha Rana</strong>
</div>
""", unsafe_allow_html=True)












