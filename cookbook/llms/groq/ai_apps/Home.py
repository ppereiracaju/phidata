import nest_asyncio
import streamlit as st

import sys, os
current_dir = os.path.dirname(__file__)

#For this code, we go up 3 levels to reach the tools folder
app_root_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
# Append the path to sys.path
sys.path[0]=(app_root_dir)

from tools.setup_environment import EnvironmentSetup

envkeys = EnvironmentSetup()
envkeys.setup_environment()

nest_asyncio.apply()

st.set_page_config(
    page_title="Groq AI Apps",
    page_icon=":orange_heart:",
)
st.title("Groq AI Apps")
st.markdown("##### :orange_heart: Built with [phidata](https://github.com/phidatahq/phidata)")


def main() -> None:
    st.markdown("---")
    st.markdown("### Select an AI App from the sidebar:")
    st.markdown("#### 1. RAG Research: Generate reports about topics")
    st.markdown("#### 2. RAG Chat: Chat with Websites and PDFs")

    st.sidebar.success("Select App from above")


main()
