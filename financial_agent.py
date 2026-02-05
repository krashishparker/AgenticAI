from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

# 1. Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"), 
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# 2. Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"), 
    tools=[
       YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                     company_news=True) 
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# 3. Multi-AI Agent (The Leader) - UPDATED FOR 2026 STABILITY
multi_ai_agent = Agent(
    # Using the high-capacity OSS model for superior task delegation
    model=Groq(id="openai/gpt-oss-120b"), 
    team=[web_search_agent, finance_agent],
    instructions=[
        "Always include sources",
        "Use tables to display the data",
        "Step 1: Get the list of stocks from the Web Search Agent.",
        "Step 2: Pass those tickers to the Finance AI Agent for details."
    ],
    show_tool_calls=True,
    markdown=True,
)

#Please Summarize analyst recommendation and share the latest news for TESLA 
#Prompt: "Use the web search agent to find a list of 5 tech stocks currently trading near their 52-week lows. "
#"Then, for those specific tickers, use the finance agent to provide a table with their current price, analyst recommendations, and a brief fundamental summary."
#Prompt: "Compare NVDA with AMD and INTC. Create a table showing their current stock prices, P/E ratios, and a summary of recent analyst recommendations for each. "
#"Also, search for any major news from the last 48 hours that might affect their stock performance."
#Prompt: "Analyze Tesla (TSLA). First, get the latest fundamental data and analyst targets. "
#"Then, search the web for the top 3 news stories from this week explaining the recent price action. "
#"Summarize if the overall market sentiment is bullish or bearish."
#Prompt: "Search for 3 high-yield dividend stocks in the energy sector.
#  For each stock, display a table with the dividend yield, current price, and the 1-year target price provided by analysts."
multi_ai_agent.print_response("Search for 3 high-yield dividend stocks in the energy sector. For each stock, display a table with the dividend yield, current price, and the 1-year target price provided by analysts.",stream=True)