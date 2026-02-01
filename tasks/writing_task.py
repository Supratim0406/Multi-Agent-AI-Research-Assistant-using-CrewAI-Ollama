import textwrap
from crewai import Task
from agents.content_writer import content_writer_agent
from tasks.analysis_task import analysis_task
from tasks.research_task import research_task


writing_task = Task(
    agent=content_writer_agent,

    description=textwrap.dedent("""
        Create the final report for: {topic}

        Combine research findings and analysis into a clear, professional document.
    """),

    expected_output=textwrap.dedent("""
        Markdown report with sections:

        # Executive Summary
        ## Introduction
        ## Key Findings
        ## Analysis & Insights
        ## Conclusions & Recommendations
        ## Sources
    """),

    context=[research_task, analysis_task],

    output_file="final_report.md"
)
