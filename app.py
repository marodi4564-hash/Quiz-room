import streamlit as st
import random

st.set_page_config(page_title="GK Quiz Arena", page_icon="🎯", layout="centered")

st.markdown(
    """
    <style>
    :root {
        --bg-dark: #101827;
        --panel: rgba(17, 24, 39, 0.8);
        --panel-strong: rgba(15, 23, 42, 0.96);
        --border: rgba(148, 163, 184, 0.2);
        --text: #e2e8f0;
        --muted: #cbd5e1;
        --primary: #7c3aed;
        --primary-2: #22c55e;
        --accent: #f59e0b;
        --danger: #ef4444;
        --success: #10b981;
        --shadow: rgba(15, 23, 42, 0.45);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #111827 35%, #1e293b 100%);
        color: var(--text);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    .app-header {
        background: linear-gradient(120deg, rgba(124,58,237,0.25), rgba(34,197,94,0.18));
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 1.5rem 1.6rem;
        box-shadow: 0 18px 40px var(--shadow);
        margin-bottom: 1.5rem;
    }

    .app-header h1 {
        margin: 0;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: 0.02em;
    }

    .app-header p {
        margin: 0.4rem 0 0 0;
        color: var(--muted);
        font-size: 1rem;
    }

    .glass-card {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1.2rem 1.2rem 1.1rem;
        box-shadow: 0 10px 28px rgba(15, 23, 42, 0.32);
        margin-bottom: 1rem;
    }

    .pill {
        display: inline-block;
        background: rgba(124,58,237,0.18);
        border: 1px solid rgba(167, 139, 250, 0.4);
        border-radius: 999px;
        color: #ddd6fe;
        padding: 0.35rem 0.8rem;
        margin-bottom: 0.7rem;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .player-list {
        background: rgba(15, 118, 110, 0.12);
        border: 1px solid rgba(45, 212, 191, 0.24);
        border-radius: 14px;
        padding: 0.8rem 1rem;
        color: #d1fae5;
        line-height: 1.8;
    }

    .score-box {
        background: rgba(2, 6, 23, 0.5);
        border: 1px solid rgba(148, 163, 184, 0.22);
        border-radius: 14px;
        padding: 0.7rem 0.9rem;
        margin: 0.35rem 0;
    }

    .score-box strong { color: #f8fafc; }

    .question-card {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(96, 165, 250, 0.28);
        border-left: 6px solid #60a5fa;
        border-radius: 18px;
        padding: 1rem 1rem 0.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 6px 18px rgba(59, 130, 246, 0.12);
    }

    .question-card h4 {
        margin: 0 0 0.9rem;
        font-size: 1.2rem;
        color: #f8fafc;
    }

    .stRadio > div {
        background: rgba(15, 23, 42, 0.7);
        border-radius: 12px;
        padding: 0.3rem 0.4rem;
        border: 1px solid rgba(148, 163, 184, 0.18);
    }

    .stButton > button {
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: 0.02em;
        border: none;
        background: linear-gradient(135deg, #8b5cf6, #6d28d9);
        color: white;
        padding: 0.7rem 1rem;
        transition: 0.2s ease;
        box-shadow: 0 12px 22px rgba(124, 58, 237, 0.22);
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 24px rgba(124, 58, 237, 0.28);
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #22c55e, #16a34a);
        box-shadow: 0 12px 22px rgba(34, 197, 94, 0.22);
    }

    .stSuccess {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        border-radius: 12px;
        color: #d1fae5;
    }

    .stError {
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        color: #fee2e2;
    }

    .stWarning {
        background: rgba(245, 158, 11, 0.11);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 12px;
        color: #fef3c7;
    }

    .stInfo {
        background: rgba(59, 130, 246, 0.10);
        border: 1px solid rgba(96, 165, 250, 0.28);
        border-radius: 12px;
        color: #dbeafe;
    }

    input, textarea, select {
        border-radius: 10px !important;
        border: 1px solid rgba(148, 163, 184, 0.25) !important;
        background: rgba(15, 23, 42, 0.85) !important;
        color: #f8fafc !important;
    }

    label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }

    .small-note {
        color: var(--muted);
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state initialization
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
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Indian Polity"


def get_questions(category):
    quiz_bank = {
        "Indian Polity": [
            {
                "q": "भारत का संविधान कब लागू हुआ था?",
                "options": ["15 अगस्त 1947", "26 जनवरी 1950", "26 नवंबर 1949", "2 अक्टूबर 1950"],
                "answer": "26 जनवरी 1950",
            },
            {
                "q": "भारतीय राष्ट्रीय कांग्रेस की स्थापना किस वर्ष हुई थी?",
                "options": ["1885", "1905", "1920", "1942"],
                "answer": "1885",
            },
            {
                "q": "भारत की राजधानी किस राज्य में स्थित है?",
                "options": ["हरियाणा", "दिल्ली", "उत्तर प्रदेश", "राजस्थान"],
                "answer": "दिल्ली",
            },
        ],
        "Modern History": [
            {
                "q": "1857 के विद्रोह को किस नाम से जाना जाता है?",
                "options": ["स्वाधीनता संग्राम", "गदर विद्रोह", "सिपाही विद्रोह", "राष्ट्रीय आंदोलन"],
                "answer": "सिपाही विद्रोह",
            },
            {
                "q": "महात्मा गांधी ने 'सविनय अवज्ञा' आंदोलन शुरू किया?",
                "options": ["1930", "1922", "1919", "1942"],
                "answer": "1930",
            },
            {
                "q": "कानपुर की रानी लक्ष्मीबाई का जन्म किस शहर से जुड़ा है?",
                "options": ["जयपुर", "लखनऊ", "वाराणसी", "ग्वालियर"],
                "answer": "वाराणसी",
            },
        ],
        "Geography": [
            {
                "q": "भारत की सबसे लंबी नदी कौन सी है?",
                "options": ["ब्रह्मपुत्र", "गंगा", "यमुना", "गोदावरी"],
                "answer": "गंगा",
            },
            {
                "q": "सिंधु नदी कहाँ से निकलती है?",
                "options": ["हिमालय", "अरावली", "दक्षिणी पठार", "देccan"],
                "answer": "हिमालय",
            },
            {
                "q": "भारत का सबसे बड़ा महासागर से लगा राज्य कौन सा है?",
                "options": ["गुजरात", "ओडिशा", "तामिलनाडु", "केरल"],
                "answer": "तामिलनाडु",
            },
        ],
        "General Science": [
            {
                "q": "पृथ्वी का सबसे बड़ा भाग किस प्रकार का है?",
                "options": ["जल", "भूमि", "वायु", "उपग्रह"],
                "answer": "जल",
            },
            {
                "q": "सूरज से ऊर्जा सीधे किस रूप में आती है?",
                "options": ["कंप्यूटर", "चुनौती", "प्रकाश और ताप", "ध्वनि"],
                "answer": "प्रकाश और ताप",
            },
            {
                "q": "मांसपेशियों के लिए ऊर्जा का मुख्य स्रोत क्या है?",
                "options": ["कैल्सियम", "ग्लूकोज", "लोहे", "विटामिन"],
                "answer": "ग्लूकोज",
            },
        ],
    }

    return quiz_bank.get(category, quiz_bank["Indian Polity"])


st.markdown(
    """
    <div class="app-header">
        <div class="pill">Live Quiz Arena</div>
        <h1>🎯 GK Quiz Arena</h1>
        <p>Smart, friendly, and fast room-based quiz experience for you and your friends.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- LOGIN & ROOM SETUP ---
if not st.session_state.room_code:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Join or Create a Quiz Room")
    username_input = st.text_input("अपना नाम दर्ज करें (Your Name):", value=st.session_state.username)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Create Room (Host)", use_container_width=True):
            if username_input.strip() == "":
                st.error("कृपया पहले अपना नाम दर्ज करें!")
            else:
                st.session_state.username = username_input.strip()
                st.session_state.room_code = str(random.randint(100000, 999999))
                st.session_state.is_host = True
                st.session_state.players = [st.session_state.username]
                st.session_state.scores = {st.session_state.username: 0}
                st.rerun()

    with col2:
        room_input = st.text_input("रूम कोड दर्ज करें (Room Code)", value="")
        if st.button("Join Room", use_container_width=True):
            if username_input.strip() == "" or room_input.strip() == "":
                st.error("नाम और रूम कोड दोनों भरना ज़रूरी है!")
            else:
                st.session_state.username = username_input.strip()
                st.session_state.room_code = room_input.strip()
                st.session_state.is_host = False
                if st.session_state.username not in st.session_state.players:
                    st.session_state.players.append(st.session_state.username)
                    st.session_state.scores.setdefault(st.session_state.username, 0)
                st.rerun()

    st.markdown("<div class='small-note'>Tip: Create a room to host a live quiz, or join with a room code to enter an existing match.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOBBY & GAMEPLAY ---
else:
    st.markdown(
        """
        <div class="glass-card">
            <div class="pill">Room Active</div>
            <div style='font-size:1.1rem; font-weight:700;'>रूम कोड: <span style='color:#a5b4fc;'>"""
        + st.session_state.room_code
        + """</span> · खिलाड़ी: <span style='color:#86efac;'>"""
        + st.session_state.username
        + """</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.quiz_started:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.info("⏳ LOBBY: दोस्तों के जुड़ने का इंतज़ार है...")
        st.write("**जुड़े हुए खिलाड़ी:**")
        st.markdown(
            f"<div class='player-list'>{' • '.join(st.session_state.players)}</div>",
            unsafe_allow_html=True,
        )

        if st.session_state.is_host:
            st.markdown("---")
            st.subheader("Host Controls")
            st.session_state.selected_category = st.selectbox(
                "क्विज़ टॉपिक चुनें:",
                ["Indian Polity", "Modern History", "Geography", "General Science"],
                index=["Indian Polity", "Modern History", "Geography", "General Science"].index(st.session_state.selected_category),
            )

            if st.button("🚀 Start Quiz Now", type="primary", use_container_width=True):
                st.session_state.quiz_started = True
                st.rerun()
        else:
            st.warning("होस्ट के क्विज़ शुरू करने का इंतज़ार करें...")
            if st.button("🔄 रिफ्रेश करें (Refresh Lobby)"):
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ⚡ Live Quiz Started!")
        st.caption(f"Selected Topic: {st.session_state.selected_category}")
        st.markdown("</div>", unsafe_allow_html=True)

        questions = get_questions(st.session_state.selected_category)

        for i, q_data in enumerate(questions):
            st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
            st.markdown(f"<h4>प्रश्न {i + 1}: {q_data['q']}</h4>", unsafe_allow_html=True)
            ans = st.radio("विकल्प चुनें:", q_data["options"], key=f"q_{i}")

            if st.button(f"उत्तर सबमिट करें (Q{i + 1})", key=f"btn_{i}", use_container_width=False):
                if ans == q_data["answer"]:
                    st.success("✅ सही जवाब! (+1 अंक)")
                    st.session_state.scores[st.session_state.username] = st.session_state.scores.get(st.session_state.username, 0) + 1
                else:
                    st.error(f"❌ गलत जवाब! सही उत्तर था: {q_data['answer']}")

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("🏆 लाइव स्कोरबोर्ड (Live Scoreboard)")
        for player, score in st.session_state.scores.items():
            st.markdown(
                f"<div class='score-box'><strong>{player}</strong> : {score} अंक</div>",
                unsafe_allow_html=True,
            )

        if st.button("🔄 गेम रीसेट करें", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚪 Leave Room"):
        for key in [
            "room_code",
            "is_host",
            "username",
            "players",
            "quiz_started",
            "scores",
            "selected_category",
        ]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
