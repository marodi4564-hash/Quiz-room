import streamlit as st
import random

st.set_page_config(page_title="GK Quiz Arena", page_icon="🎯", layout="centered")

# ------------------------------
# Custom Styling
# ------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg-1: #07111f;
        --bg-2: #0f172a;
        --bg-3: #111827;
        --panel: rgba(15, 23, 42, 0.72);
        --panel-strong: rgba(15, 23, 42, 0.95);
        --border: rgba(148, 163, 184, 0.25);
        --text: #e2e8f0;
        --muted: #cbd5e1;
        --primary: #8b5cf6;
        --secondary: #22c55e;
        --accent: #f59e0b;
        --danger: #ef4444;
        --blue: #60a5fa;
        --cyan: #2dd4bf;
        --shadow: rgba(2, 6, 23, 0.45);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, rgba(139, 92, 246, 0.18), transparent 25%),
                    radial-gradient(circle at bottom right, rgba(34, 197, 94, 0.14), transparent 30%),
                    linear-gradient(135deg, var(--bg-1), var(--bg-2) 40%, var(--bg-3));
        color: var(--text);
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    .hero {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.22), rgba(34, 197, 94, 0.12));
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 1.6rem 1.6rem 1.2rem;
        box-shadow: 0 18px 50px var(--shadow);
        margin-bottom: 1.3rem;
    }

    .hero-tag {
        display: inline-block;
        background: rgba(167, 139, 250, 0.18);
        color: #ddd6fe;
        border: 1px solid rgba(196, 181, 253, 0.35);
        border-radius: 999px;
        padding: 0.38rem 0.8rem;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }

    .hero h1 {
        margin: 0;
        font-size: clamp(2.1rem, 3vw, 3rem);
        line-height: 1.1;
        font-weight: 800;
    }

    .hero p {
        margin: 0.75rem 0 0 0;
        color: var(--muted);
        font-size: 1rem;
    }

    .glass {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 1.1rem 1.1rem 0.9rem;
        box-shadow: 0 10px 25px rgba(2, 6, 23, 0.28);
        margin-bottom: 1rem;
    }

    .room-banner {
        background: linear-gradient(135deg, rgba(96, 165, 250, 0.12), rgba(45, 212, 191, 0.12));
        border: 1px solid rgba(96, 165, 250, 0.22);
        border-radius: 18px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
    }

    .room-banner strong {
        color: #f8fafc;
    }

    .player-box {
        background: rgba(15, 118, 110, 0.12);
        border: 1px solid rgba(45, 212, 191, 0.24);
        border-radius: 14px;
        padding: 0.8rem 0.95rem;
        color: #d1fae5;
        line-height: 1.7;
        margin-top: 0.6rem;
    }

    .score-box {
        background: rgba(2, 6, 23, 0.45);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 14px;
        padding: 0.8rem 0.9rem;
        margin: 0.5rem 0;
    }

    .score-box strong {
        color: #f8fafc;
    }

    .question-card {
        background: rgba(15, 23, 42, 0.88);
        border: 1px solid rgba(96, 165, 250, 0.18);
        border-left: 5px solid var(--blue);
        border-radius: 18px;
        padding: 1rem 1rem 0.8rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.10);
    }

    .question-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 0.7rem;
    }

    .question-tag {
        display: inline-block;
        background: rgba(96, 165, 250, 0.12);
        border: 1px solid rgba(96, 165, 250, 0.26);
        border-radius: 999px;
        padding: 0.28rem 0.7rem;
        color: #bfdbfe;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    .question-card h4 {
        margin: 0;
        font-size: 1.15rem;
        color: #f8fafc;
        line-height: 1.5;
    }

    .progress-wrap {
        margin: 0.8rem 0 1rem;
    }

    .stProgress > div > div {
        background: linear-gradient(90deg, #8b5cf6, #22c55e);
    }

    .stRadio > div {
        background: rgba(15, 23, 42, 0.7);
        border-radius: 12px;
        padding: 0.4rem 0.5rem;
        border: 1px solid rgba(148, 163, 184, 0.12);
    }

    .stButton > button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em !important;
        border: none !important;
        background: linear-gradient(135deg, #8b5cf6, #6d28d9) !important;
        color: white !important;
        padding: 0.75rem 1rem !important;
        box-shadow: 0 10px 22px rgba(124, 58, 237, 0.22) !important;
        transition: 0.2s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 12px 24px rgba(124, 58, 237, 0.28) !important;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #22c55e, #16a34a) !important;
        box-shadow: 0 10px 22px rgba(34, 197, 94, 0.24) !important;
    }

    .stSuccess {
        background: rgba(16, 185, 129, 0.12) !important;
        border: 1px solid rgba(16, 185, 129, 0.35) !important;
        border-radius: 12px !important;
        color: #d1fae5 !important;
    }

    .stError {
        background: rgba(239, 68, 68, 0.12) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        border-radius: 12px !important;
        color: #fee2e2 !important;
    }

    .stWarning {
        background: rgba(245, 158, 11, 0.11) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        border-radius: 12px !important;
        color: #fef3c7 !important;
    }

    .stInfo {
        background: rgba(59, 130, 246, 0.10) !important;
        border: 1px solid rgba(96, 165, 250, 0.28) !important;
        border-radius: 12px !important;
        color: #dbeafe !important;
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

    .muted {
        color: var(--muted);
        font-size: 0.92rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# State Setup
# ------------------------------
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
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "submitted_answers" not in st.session_state:
    st.session_state.submitted_answers = {}

# ------------------------------
# Quiz Data
# ------------------------------
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

# ------------------------------
# App UI
# ------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">LIVE QUIZ</div>
        <h1>🎯 GK Quiz Arena</h1>
        <p>Play, compete, and learn with a smarter, smoother quiz experience.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- LOGIN / ROOM CREATION ---
if not st.session_state.room_code:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.subheader("Join or Create a Quiz Room")
    username_input = st.text_input("अपना नाम दर्ज करें (Your Name):", value=st.session_state.username)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Create Room (Host)", use_container_width=True):
            if not username_input.strip():
                st.error("कृपया पहले अपना नाम दर्ज करें!")
            else:
                st.session_state.username = username_input.strip()
                st.session_state.room_code = str(random.randint(100000, 999999))
                st.session_state.is_host = True
                st.session_state.players = [st.session_state.username]
                st.session_state.scores = {st.session_state.username: 0}
                st.session_state.question_index = 0
                st.session_state.submitted_answers = {}
                st.rerun()

    with col2:
        room_input = st.text_input("रूम कोड दर्ज करें (Room Code)", value="")
        if st.button("Join Room", use_container_width=True):
            if not username_input.strip() or not room_input.strip():
                st.error("नाम और रूम कोड दोनों भरना ज़रूरी है!")
            else:
                st.session_state.username = username_input.strip()
                st.session_state.room_code = room_input.strip()
                st.session_state.is_host = False
                if st.session_state.username not in st.session_state.players:
                    st.session_state.players.append(st.session_state.username)
                    st.session_state.scores.setdefault(st.session_state.username, 0)
                st.session_state.question_index = 0
                st.session_state.submitted_answers = {}
                st.rerun()

    st.markdown("<div class='muted'>Tip: Create a room to host a live quiz, or enter a code to join a friend’s match.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown(
        """
        <div class="room-banner">
            <div class="hero-tag" style="margin-bottom:0.5rem;">ROOM ACTIVE</div>
            <div><strong>रूम कोड:</strong> <span style='color:#a5b4fc;'>"""
        + st.session_state.room_code
        + """</span> &nbsp;•&nbsp; <strong>खिलाड़ी:</strong> <span style='color:#86efac;'>"""
        + st.session_state.username
        + """</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.quiz_started:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.info("⏳ LOBBY: दोस्तों के जुड़ने का इंतज़ार है...")
        st.write("**जुड़े हुए खिलाड़ी:**")
        st.markdown(
            f"<div class='player-box'>{' • '.join(st.session_state.players)}</div>",
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
                st.session_state.question_index = 0
                st.session_state.submitted_answers = {}
                st.rerun()
        else:
            st.warning("होस्ट के क्विज़ शुरू करने का इंतज़ार करें...")
            if st.button("🔄 रिफ्रेश करें (Refresh Lobby)"):
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        questions = get_questions(st.session_state.selected_category)
        total_questions = len(questions)

        st.markdown(
            '<div class="glass progress-wrap">',
            unsafe_allow_html=True,
        )
        progress = (st.session_state.question_index / total_questions) if total_questions else 0
        st.progress(progress, text=f"Question {min(st.session_state.question_index + 1, total_questions)} / {total_questions}")
        st.markdown("</div>", unsafe_allow_html=True)

        current_question = questions[st.session_state.question_index]

        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        st.markdown(
            f"<div class='question-top'><span class='question-tag'>Question {st.session_state.question_index + 1}</span><span class='muted'>{st.session_state.selected_category}</span></div>",
            unsafe_allow_html=True,
        )
        st.markdown(f"<h4>{current_question['q']}</h4>", unsafe_allow_html=True)

        selected = st.radio("विकल्प चुनें:", current_question["options"], key=f"current_option_{st.session_state.question_index}")

        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("Submit Answer", type="primary", use_container_width=True):
                st.session_state.submitted_answers[st.session_state.question_index] = selected
                if selected == current_question["answer"]:
                    st.session_state.scores[st.session_state.username] = st.session_state.scores.get(st.session_state.username, 0) + 1
                    st.success("✅ सही जवाब! (+1 अंक)")
                else:
                    st.error(f"❌ गलत जवाब! सही उत्तर था: {current_question['answer']}")

                if st.session_state.question_index < total_questions - 1:
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    st.session_state.quiz_started = False
                    st.session_state.question_index = 0
                    st.rerun()

        with col_b:
            if st.button("Reset Game", use_container_width=True):
                st.session_state.quiz_started = False
                st.session_state.question_index = 0
                st.session_state.submitted_answers = {}
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.subheader("🏆 लाइव स्कोरबोर्ड (Live Scoreboard)")
        for player, score in st.session_state.scores.items():
            st.markdown(
                f"<div class='score-box'><strong>{player}</strong> : {score} अंक</div>",
                unsafe_allow_html=True,
            )
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
            "question_index",
            "submitted_answers",
        ]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
