import textwrap
from crewai import Task
from agents.data_analyst import data_analyst_agent
from tasks.research_task import research_task


analysis_task = Task(
    agent=data_analyst_agent,

    description=textwrap.dedent("""
        Analyze the research findings for: {topic}

        Steps:
        - Review findings
        - Identify key patterns and trends
        - Interpret significance
        - Summarize insights
        - Provide conclusions

        Output must be concise and evidence-based.
    """),

    expected_output=textwrap.dedent("""
        Markdown report with sections:

        ## Key Insights
        ## Trends & Patterns
        ## Implications
        ## Expert Interpretation
        ## Actionable Conclusions
    """),

    context=[research_task],

    output_file="analysis_report.md"
)
