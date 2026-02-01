from dotenv import load_dotenv
from crew import Crew
from pathlib import Path
from datetime import datetime

load_dotenv()


def run(topic: str):
    result = Crew.kickoff(inputs={"topic": topic})

    print("-" * 50)
    print(result)
    print("-" * 50)

    # ==============================
    # Save markdown report manually
    # ==============================
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = reports_dir / f"final_report_{timestamp}.md"

    filename.write_text(result, encoding="utf-8")

    print(f"\n✅ Report saved to: {filename}")


if __name__ == "__main__":
    topic = "AI Agents"
    run(topic)
