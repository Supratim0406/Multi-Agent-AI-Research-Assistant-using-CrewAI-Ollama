import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()


# ======================================================
# ENV (safe defaults)
# ======================================================
PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

MODEL = os.getenv("ANALYST_AGENT_LLM", "mistral")
TEMPERATURE = float(os.getenv("ANALYST_AGENT_TEMPERATURE", 0.2))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 600))

BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")


# ======================================================
# LLM FACTORY
# ======================================================
def build_llm():

    if PROVIDER == "ollama":
        return LLM(
            model=MODEL,
            base_url=BASE_URL,
            api_key="none",
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )

    elif PROVIDER == "groq":
        return LLM(
            model=MODEL,
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )

    elif PROVIDER == "openai":
        return LLM(
            model=MODEL,
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )

    else:
        raise ValueError(f"Unsupported provider: {PROVIDER}")


llm = build_llm()


# ======================================================
# AGENT
# ======================================================
data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Extract insights and summarize findings clearly.",

    backstory="Expert analyst who converts research data into concise insights.",

    llm=llm,
    verbose=True,
)
