import textwrap
from crewai import Task
from agents.research_specialist import research_specialist_agent


research_task = Task(
    agent=research_specialist_agent,

    description=textwrap.dedent("""
        Research the topic: {topic}

        Collect accurate, up-to-date information from reliable sources.
        Focus on facts, statistics, expert opinions, and recent developments.
    """),

    expected_output=textwrap.dedent("""
        Markdown report with sections:

        ## Key Findings
        ## Statistics & Data
        ## Expert Insights
        ## Recent Developments
        ## Sources
    """),

    output_file="research_findings.md"
)
