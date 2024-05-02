import streamlit as st
from openbb import obb
from phi.assistant import Assistant
from phi.llm.groq import Groq
from phi.tools.openbb_tools import OpenBBTools

import sys, os
current_dir = os.path.dirname(__file__)

#For this code, we go up 3 levels to reach the tools folder
app_root_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
# Append the path to sys.path
sys.path.append(app_root_dir)

from tools.setup_environment import EnvironmentSetup

envkeys = EnvironmentSetup()
envkeys.setup_environment()

assistant = Assistant(
    llm=Groq(model="llama3-70b-8192"),
    tools=[OpenBBTools(obb=obb, company_profile=True, company_news=True, price_targets=True)],
    show_tool_calls=True,
)

assistant.cli_app(markdown=True, stream=False, user="Groq Caju")
assistant.print_response("What's the stock price for meta", markdown=True, stream=False)
# assistant.print_response("Are analysts expecting meta to go up, share details", markdown=True, stream=False)
# assistant.print_response("What are analysts saying about NVDA", markdown=True, stream=False)
