# trend_spotter/agent.py
from google.adk.agents import Agent
from google.adk.tools import google_search
from . import prompt
from dotenv import load_dotenv
import os


load_dotenv()

# Use the "latest" tag to always get the most recent stable version of the model.
MODEL = "gemini-2.5-flash"
# This single agent will perform all the work.
trend_spotter_agent = Agent(
    model=MODEL,
    name="trend_spotter_agent",
    description="An agent that finds and reports on AI agent trends.",
    # The agent's entire logic comes from our detailed prompt.
    instruction=prompt.TREND_SPOTTER_PROMPT,
    # We give the agent a single tool: the ability to search Google.
    tools=[google_search],
)
# We assign it to `root_agent` by convention for ADK to discover.
root_agent = trend_spotter_agent