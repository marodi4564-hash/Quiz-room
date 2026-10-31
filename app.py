import streamlit as st
import random
import time

st.set_page_config(page_title="GK Quiz Arena", page_icon="🎯", layout="centered")

# Session State Initialization
if "room_code" not in st.session_state:
    st.session_state.room_code = None
if "is_host" not in st.session_state:
    st.session_state.is_host = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "players" not in st.session_state:
    st.session_state.players = []
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "scores" not in st.session_state:
    st.session_state.scores = {}

st.title("🎯 GK Quiz Arena - Live Room")

# --- LOGIN & ROOM SETUP ---
if not st.session_state.room_code:
    st.subheader("Join or Create a Quiz Room")
    username_input = st.text_input("अपना नाम दर्ज करें (Your Name):", value=st.session_state.username)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Create Room (Host)", use_container_width=True):
            if username_input.strip() == "":
                st.error("कृपया पहले अपना नाम दर्ज करें!")
            else:
                st.session_state.username = username_input
                st.session_state.room_code = str(random.randint(100000, 999999))
                st.session_state.is_host = True
                st.session_state.players = [username_input]
                st.session_state.scores[username_input] = 0
                st.rerun()
                
    with col2:
        room_input = st.text_input("रूम कोड दर्ज करें (Room Code)")
        if st.button("Join Room", use_container_width=True):
            if username_input.strip() == "" or room_input.strip() == "":
                st.error("नाम और रूम कोड दोनों भरना ज़रूरी है!")
            else:
                st.session_state.username = username_input
                st.session_state.room_code = room_input
                st.session_state.is_host = False
                if username_input not in st.session_state.players:
                    st.session_state.players.append(username_input)
                    st.session_state.scores[username_input] = 0
                st.rerun()

# --- LOBBY & GAMEPLAY ---
else:
    st.success(f"रूम कोड (Room Code): **{st.session_state.room_code}** | खिलाड़ी: **{st.session_state.username}**")
    
    # LOBBY
    if not st.session_state.quiz_started:
        st.info("⏳ LOBBY: दोस्तों के जुड़ने का इंतज़ार है...")
        st.write("**जुड़े हुए खिलाड़ी:**", ", ".join(st.session_state.players))
        
        if st.session_state.is_host:
            st.markdown("---")
            st.subheader("Host Controls")
            category = st.selectbox("क्विज़ टॉपिक चुनें:", ["Indian Polity", "Modern History", "Geography", "General Science"])
            
            if st.button("🚀 Start Quiz Now", type="primary", use_container_width=True):
                st.session_state.quiz_started = True
                st.rerun()
        else:
            st.warning("होस्ट के क्विज़ शुरू करने का इंतज़ार करें...")
            if st.button("🔄 रिफ्रेश करें (Refresh Lobby)"):
                st.rerun()
                
    # QUIZ ACTIVE SCREEN
    else:
        st.markdown("### ⚡ Live Quiz Started!")
        
        # Sample Questions based on category
        questions = [
            {
                "q": "भारत का संविधान कब लागू हुआ था?",
                "options": ["15 अगस्त 1947", "26 जनवरी 1950", "26 नवंबर 1949", "2 अक्टूबर 1950"],
                "answer": "26 जनवरी 1950"
            },
            {
                "q": "भारतीय राष्ट्रीय कांग्रेस की स्थापना किस वर्ष हुई थी?",
                "options": ["1885", "1905", "1920", "1942"],
                "answer": "1885"
            },
            {
                "q": "भारत की सबसे लंबी नदी कौन सी है?",
                "options": ["ब्रह्मपुत्र", "गंगा", "यमुना", "गोदावरी"],
                "answer": "गंगा"
            }
        ]
        
        # Simple loop for demo question
        for i, q_data in enumerate(questions):
            st.write(f"**प्रश्न {i+1}: {q_data['q']}**")
            ans = st.radio(f"विकल्प चुनें (Q{i+1}):", q_data["options"], key=f"q_{i}")
            
            if st.button(f"उत्तर सबमिट करें (Q{i+1})", key=f"btn_{i}"):
                if ans == q_data["answer"]:
                    st.success("✅ सही जवाब! (+1 अंक)")
                    st.session_state.scores[st.session_state.username] += 1
                else:
                    st.error(f"❌ गलत जवाब! सही उत्तर था: {q_data['answer']}")
                    
        st.markdown("---")
        st.subheader("🏆 लाइव स्कोरबोर्ड (Live Scoreboard)")
        for p, s in st.session_state.scores.items():
            st.write(f"- **{p}**: {s} अंक")
            
        if st.button("🔄 गेम रीसेट करें"):
            st.session_state.quiz_started = False
            st.rerun()

