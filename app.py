import os
import streamlit as st
from dotenv import load_dotenv

# --------------------------------------------------
# Disable CrewAI telemetry (fix signal/thread issue)
# --------------------------------------------------
os.environ["CREWAI_TELEMETRY_DISABLED"] = "true"

load_dotenv()


# ======================================================
# ENV
# ======================================================
PROVIDER = os.getenv("LLM_PROVIDER", "ollama")


# ======================================================
# KEY CHECK (provider aware)
# ======================================================
def check_api_keys():
    required = ["SERPER_API_KEY"]

    if PROVIDER == "groq":
        required.append("GROQ_API_KEY")

    if PROVIDER == "openai":
        required.append("OPENAI_API_KEY")

    return [v for v in required if not os.getenv(v)]


# ======================================================
# MAIN
# ======================================================
def main():

    # ------------------------------
    # UI loads instantly now
    # ------------------------------
    st.set_page_config(
        page_title="AI Research Assistant",
        page_icon="🔬",
        layout="wide"
    )

    st.title("🔬 AI Research Assistant")
    st.caption(f"CrewAI • Provider: {PROVIDER.upper()}")

    # --------------------------------------------------
    # Session state
    # --------------------------------------------------
    st.session_state.setdefault("research_completed", False)
    st.session_state.setdefault("research_error", None)

    # ==================================================
    # SIDEBAR
    # ==================================================
    with st.sidebar:
        st.header("⚙️ Configuration")

        if PROVIDER == "ollama":
            st.success("🟢 Ollama (Local & Free)")
        elif PROVIDER == "groq":
            st.info("🟡 Groq Cloud")
        else:
            st.info("🔵 OpenAI")

        missing = check_api_keys()

        if missing:
            st.error("Missing keys:")
            for m in missing:
                st.code(f"{m}=your_key")
        else:
            st.success("Config OK")

        st.markdown("---")
        st.markdown("""
        **Agents**
        - 🔍 Research
        - 📊 Analysis
        - ✍️ Writing
        """)

    # ==================================================
    # INPUT
    # ==================================================
    col1, col2 = st.columns([2, 1])

    with col1:
        topic = st.text_input(
            "Enter research topic",
            placeholder="AI trends in 2026"
        )

        run_btn = st.button(
            "🚀 Start Research",
            disabled=bool(check_api_keys())
        )

        # --------------------------------------------------
        # LAZY IMPORT CREW (🔥 IMPORTANT)
        # --------------------------------------------------
        if run_btn:

            if not topic.strip():
                st.warning("Please enter a topic")
                return

            st.session_state.research_completed = False
            st.session_state.research_error = None

            with st.spinner("🤖 Agents working..."):

                try:
                    # import ONLY when needed
                    from crew import research_crew

                    research_crew.kickoff({"topic": topic})

                    st.session_state.research_completed = True

                except Exception as e:
                    st.session_state.research_error = str(e)
                    st.session_state.research_completed = True

    # ==================================================
    # STATUS
    # ==================================================
    with col2:
        st.header("Status")

        if st.session_state.research_error:
            st.error(st.session_state.research_error)
        elif st.session_state.research_completed:
            st.success("Completed")
        else:
            st.info("Idle")

    # ==================================================
    # RESULTS
    # ==================================================
    if st.session_state.research_completed and not st.session_state.research_error:

        st.header("📄 Results")

        files = {
            "research_findings.md": "🔍 Research",
            "analysis_report.md": "📊 Analysis",
            "final_report.md": "📝 Final Report",
        }

        tabs = st.tabs(files.values())

        for tab, fname in zip(tabs, files.keys()):
            with tab:
                if os.path.exists(fname):
                    content = open(fname, encoding="utf-8").read()
                    st.markdown(content)
                    st.download_button("⬇ Download", content, fname)
                else:
                    st.warning(f"{fname} not found")


# ======================================================
# RUN
# ======================================================
if __name__ == "__main__":
    main()
