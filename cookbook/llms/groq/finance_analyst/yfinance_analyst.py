from phi.assistant import Assistant
from phi.tools.yfinance import YFinanceTools
from phi.llm.groq import Groq

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
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
)
assistant.cli_app(markdown=True, stream=False, user="Groq")
# assistant.print_response("What's the NVDA stock price", markdown=True, stream=False)
# assistant.print_response("Share NVDA analyst recommendations", markdown=True, stream=False)
# assistant.print_response("Summarize fundamentals for TSLA", markdown=True, stream=False)
