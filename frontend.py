import os
from datetime import datetime

import streamlit as st
from langchain_core.messages import HumanMessage
from main import app


# ─────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Travel Booking System",
    page_icon="✈️",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────
if "trip_query" not in st.session_state:
    st.session_state.trip_query = ""

if "generated" not in st.session_state:
    st.session_state.generated = False


# ─────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, .stApp{
    font-family:'Inter',sans-serif;
    background:#070b12;
}

/* Hide Streamlit branding */
#MainMenu, footer, header{
    visibility:hidden;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0b111c !important;
    border-right:1px solid rgba(255,255,255,.05);
}

/* Glass cards */
.glass-card{
    background:rgba(17,25,40,.65);
    border:1px solid rgba(255,255,255,.08);
    border-radius:20px;
    backdrop-filter:blur(20px);
    padding:1rem;
}

/* Sidebar titles */
.sidebar-title{
    color:white;
    font-size:1rem;
    font-weight:700;
    margin-top:1rem;
    margin-bottom:.6rem;
}

/* Sidebar chips */
.sidebar-chip{
    background:#101827;
    border:1px solid rgba(255,255,255,.06);
    border-radius:10px;
    padding:.55rem .8rem;
    margin-bottom:.5rem;
    color:#8cb8e8;
    font-size:.85rem;
}

/* User card */
.user-card{
    background:linear-gradient(
        135deg,
        rgba(58,123,213,.25),
        rgba(0,210,255,.15)
    );

    border:1px solid rgba(255,255,255,.08);
    border-radius:18px;
    padding:1rem;
    margin-bottom:1rem;
}

.user-name{
    color:white;
    font-size:1rem;
    font-weight:700;
}

.user-status{
    color:#8cb8e8;
    font-size:.85rem;
}

/* Inputs */
.stTextInput input,
.stTextArea textarea{
    background:#0d1522 !important;
    color:white !important;
    border:1px solid rgba(255,255,255,.08) !important;
    border-radius:14px !important;
}

/* Buttons */
div[data-testid="stButton"] > button{
    border:none !important;
    border-radius:14px !important;

    background:linear-gradient(
        135deg,
        #1e7cff,
        #1155cc
    ) !important;

    color:white !important;
    font-weight:700 !important;

    transition:.3s !important;

    box-shadow:
        0 8px 25px rgba(30,124,255,.35);
}

div[data-testid="stButton"] > button:hover{
    transform:translateY(-2px);
}

/* Download button */
div[data-testid="stDownloadButton"] > button{
    border-radius:12px !important;
}

/* Markdown text */
.stMarkdown p,
.stMarkdown li{
    color:#dce7f4 !important;
}

/* Status widgets */
[data-testid="stStatusWidget"]{
    border-radius:18px !important;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────
with st.sidebar:

    st.markdown("""
    <div class="user-card">
        <div class="user-name">👤 Amit Yadav</div>
        <div class="user-status">AI Travel Planner Session</div>
    </div>
    """, unsafe_allow_html=True)

    thread_id = st.text_input(
        "User ID",
        value="amit_user"
    )

    st.markdown("<div class='sidebar-title'>⚙ Powered By</div>",
                unsafe_allow_html=True)

    tech_stack = [
        "🔗 LangGraph",
        "🧠 Groq LLaMA 3.3 70B",
        "🐘 PostgreSQL",
        "🔍 Tavily Search",
        "✈ AviationStack"
    ]

    for tech in tech_stack:
        st.markdown(
            f"<div class='sidebar-chip'>{tech}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='sidebar-title'>🤖 Agent Pipeline</div>",
                unsafe_allow_html=True)

    pipeline = [
        "① Flight Agent",
        "② Hotel Agent",
        "③ Itinerary Agent",
        "④ Final Agent"
    ]

    for p in pipeline:
        st.markdown(
            f"<div class='sidebar-chip'>{p}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='sidebar-title'>🟢 System Status</div>",
                unsafe_allow_html=True)

    systems = [
        "Groq API Online",
        "PostgreSQL Connected",
        "Tavily Search Active",
        "AviationStack Ready"
    ]

    for item in systems:
        st.success(item)
        
        
# ─────────────────────────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────────────────────────

st.markdown("""
<div style="
position:relative;
overflow:hidden;
border-radius:28px;
height:320px;
margin-bottom:2rem;
background:
linear-gradient(
135deg,
rgba(9,15,25,.85),
rgba(13,24,40,.75)
);
border:1px solid rgba(255,255,255,.06);
">

<img
src="https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600&q=80"
style="
position:absolute;
width:100%;
height:100%;
object-fit:cover;
filter:brightness(.28);
"/>

<div style="
position:relative;
z-index:2;
height:100%;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
padding:2rem;
">

<div style="
background:rgba(58,123,213,.18);
padding:.45rem 1rem;
border-radius:50px;
border:1px solid rgba(255,255,255,.08);
color:#8ec7ff;
font-size:.8rem;
font-weight:600;
margin-bottom:1rem;
">
✦ Multi-Agent AI System
</div>

<div style="
font-size:3rem;
font-weight:700;
color:white;
line-height:1.15;
">
✈ AI Travel Booking System
</div>

<div style="
max-width:700px;
margin-top:1rem;
font-size:1rem;
color:#9bb4cf;
">
Four specialized AI agents collaborate to search flights,
discover hotels, build itineraries and deliver your complete travel plan.
</div>

</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────────

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Countries", "50+")

with c2:
    st.metric("AI Agents", "4")

with c3:
    st.metric("Travel Plans", "1000+")

with c4:
    st.metric("Availability", "24/7")


st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# DESTINATIONS
# ─────────────────────────────────────────────────────────────

st.subheader("🌍 Explore Destinations")

DESTINATIONS = [

(
"🇯🇵 Tokyo",
"https://www.universalweather.com/blog/wp-content/uploads/2019/07/tokyo-ops-7-19.jpg",
"https://www.japan.travel/en/"
),

(
"🇫🇷 Paris",
"https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80",
"https://en.parisinfo.com/"
),

(
"🇹🇭 Bangkok",
"https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=600&q=80",
"https://www.tourismthailand.org/"
),

(
"🇮🇹 Rome",
"https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=600&q=80",
"https://www.turismoroma.it/en"
),

(
"🇦🇪 Dubai",
"https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600&q=80",
"https://www.visitdubai.com/en"
)

]

cols = st.columns(5)

for col, (name, img, link) in zip(cols, DESTINATIONS):

    with col:

        st.markdown(f"""
        <a href="{link}" target="_blank" style="text-decoration:none;">

        <div style="
        position:relative;
        overflow:hidden;
        border-radius:20px;
        height:170px;
        border:1px solid rgba(255,255,255,.06);
        ">

        <img src="{img}"
        style="
        width:100%;
        height:100%;
        object-fit:cover;
        filter:brightness(.55);
        ">

        <div style="
        position:absolute;
        bottom:12px;
        left:0;
        right:0;
        text-align:center;
        color:white;
        font-size:.95rem;
        font-weight:700;
        ">
        {name}
        </div>

        </div>
        </a>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# POPULAR TRIPS
# ─────────────────────────────────────────────────────────────

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🔥 Popular Trips")


pc1, pc2 = st.columns(2)
pc3, pc4 = st.columns(2)

with pc1:
    if st.button("🇯🇵 Japan Explorer • 7 Days • ₹2L"):
        st.session_state.trip_query = (
            "Plan a complete 7-day Japan trip under ₹2 lakhs"
        )

with pc2:
    if st.button("🇫🇷 Paris Escape • 5 Days"):
        st.session_state.trip_query = (
            "Plan a 5-day Paris vacation"
        )

with pc3:
    if st.button("🇦🇪 Dubai Weekend"):
        st.session_state.trip_query = (
            "Plan a Dubai weekend trip"
        )

with pc4:
    if st.button("🏝 Bali Backpacking • 10 Days"):
        st.session_state.trip_query = (
            "Plan a 10-day Bali backpacking trip"
        )


# ─────────────────────────────────────────────────────────────
# QUERY BOX
# ─────────────────────────────────────────────────────────────

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("🗺 Describe Your Trip")

user_query = st.text_area(
    "",
    value=st.session_state.trip_query,
    height=130,
    placeholder="""
Example:

Plan a 7-day Japan trip including:

• Flights
• Hotels
• Attractions
• Food recommendations

Budget: ₹2 Lakhs
""",
    label_visibility="collapsed"
)

generate = st.button(
    "🚀 Generate Travel Plan",
    use_container_width=True
)

# ─────────────────────────────────────────────────────────────
# AGENT METADATA
# ─────────────────────────────────────────────────────────────

AGENT_META = {
    "flight_agent": ("✈️", "Flight Agent"),
    "hotel_agent": ("🏨", "Hotel Agent"),
    "itinerary_agent": ("🗓️", "Itinerary Agent"),
    "final_agent": ("🧠", "Final Agent"),
}


# ─────────────────────────────────────────────────────────────
# GENERATE
# ─────────────────────────────────────────────────────────────

if generate:

    if not user_query.strip():
        st.warning("Please describe your trip first.")

    else:

        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        collected = {
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "final_response": "",
            "llm_calls": 0
        }

        st.markdown("---")

        st.subheader("🤖 AI Agent Workflow")

        progress_bar = st.progress(0)

        progress_step = {
            "flight_agent": 25,
            "hotel_agent": 50,
            "itinerary_agent": 75,
            "final_agent": 100
        }

        for chunk in app.stream(

            {
                "messages": [
                    HumanMessage(content=user_query)
                ],

                "user_query": user_query,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,

            },

            config=config,
            stream_mode="updates"

        ):

            for node_name, state_update in chunk.items():

                icon, label = AGENT_META.get(
                    node_name,
                    ("🔧", node_name)
                )

                progress_bar.progress(
                    progress_step.get(node_name, 100)
                )

                with st.status(
                    f"{icon} {label}",
                    expanded=True,
                    state="complete"
                ):

                    # Flight
                    if node_name == "flight_agent":

                        text = state_update.get(
                            "flight_results",
                            ""
                        )

                        collected["flight_results"] = text

                        st.markdown(
                            text or "_No flight data returned._"
                        )

                    # Hotel
                    elif node_name == "hotel_agent":

                        text = state_update.get(
                            "hotel_results",
                            ""
                        )

                        collected["hotel_results"] = text

                        st.markdown(
                            text or "_No hotel data returned._"
                        )

                    # Itinerary
                    elif node_name == "itinerary_agent":

                        text = state_update.get(
                            "itinerary",
                            ""
                        )

                        collected["itinerary"] = text

                        st.markdown(
                            text or "_No itinerary generated._"
                        )

                    # Final response
                    elif node_name == "final_agent":

                        msgs = state_update.get(
                            "messages",
                            []
                        )

                        final_text = (
                            msgs[-1].content
                            if msgs else ""
                        )

                        collected["final_response"] = final_text

                        st.markdown(
                            final_text or "_No response generated._"
                        )

                    collected["llm_calls"] = state_update.get(
                        "llm_calls",
                        collected["llm_calls"]
                    )


        # ─────────────────────────────────────
        # METRICS
        # ─────────────────────────────────────

        st.markdown("<br>", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
                "Agents Run",
                "4"
            )

        with m2:
            st.metric(
                "LLM Calls",
                collected["llm_calls"]
            )

        with m3:
            st.metric(
                "Status",
                "Success"
            )

        with m4:
            st.metric(
                "Pipeline",
                "Completed"
            )


        st.markdown("---")


        # ─────────────────────────────────────
        # FLIGHT CARD
        # ─────────────────────────────────────

        if collected["flight_results"]:

            with st.expander(
                "✈ Flight Results",
                expanded=False
            ):

                st.markdown(
                    collected["flight_results"]
                )


        # ─────────────────────────────────────
        # HOTEL CARD
        # ─────────────────────────────────────

        if collected["hotel_results"]:

            with st.expander(
                "🏨 Hotel Results",
                expanded=False
            ):

                st.markdown(
                    collected["hotel_results"]
                )


        # ─────────────────────────────────────
        # ITINERARY CARD
        # ─────────────────────────────────────

        if collected["itinerary"]:

            with st.expander(
                "🗓 Trip Itinerary",
                expanded=False
            ):

                st.markdown(
                    collected["itinerary"]
                )
                
        # ─────────────────────────────────────
        # FINAL RESPONSE
        # ─────────────────────────────────────

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("🧠 Final Travel Plan")

        if collected["final_response"]:

            with st.chat_message("assistant"):

                st.markdown(
                    collected["final_response"]
                )


        # ─────────────────────────────────────
        # SAVE FILE
        # ─────────────────────────────────────

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"travel_plan_{timestamp}.md"
        )

        save_dir = os.path.join(
            os.path.dirname(__file__),
            "travel_plans"
        )

        os.makedirs(
            save_dir,
            exist_ok=True
        )

        file_content = f"""
# Travel Plan

**User ID:** {thread_id}

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## Query

{user_query}

---

## Flight Information

{collected['flight_results'] or 'N/A'}

---

## Hotel Information

{collected['hotel_results'] or 'N/A'}

---

## Itinerary

{collected['itinerary'] or 'N/A'}

---

## Final Travel Plan

{collected['final_response'] or 'N/A'}

---

LLM Calls: {collected['llm_calls']}
"""

        filepath = os.path.join(
            save_dir,
            filename
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(file_content)


        # ─────────────────────────────────────
        # DOWNLOAD
        # ─────────────────────────────────────

        st.markdown("<br>", unsafe_allow_html=True)

        d1, d2 = st.columns([1, 2])

        with d1:

            st.download_button(
                label="⬇ Download Plan",
                data=file_content,
                file_name=filename,
                mime="text/markdown",
                use_container_width=True
            )

        with d2:

            st.success(
                f"Saved → travel_plans/{filename}"
            )


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:2rem;">

<div style="
font-size:1rem;
font-weight:700;
color:white;
">
✈ AI Travel Booking System
</div>

<div style="
margin-top:.7rem;
color:#8fa7c2;
font-size:.9rem;
">
Built with LangGraph • Groq • PostgreSQL • Streamlit
</div>

<div style="
margin-top:.4rem;
color:#5d7692;
font-size:.85rem;
">
© 2026 Amit Yadav
</div>

</div>
""",
unsafe_allow_html=True
)