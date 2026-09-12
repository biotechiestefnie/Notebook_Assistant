
from langchain.tools import tool from src.notebook_parser import parse_notebook # import your existing parser @tool def analyze_notebook(path: str) -> str:
    """ LangChain tool: Analyze a Jupyter notebook using the Notebook Assistant parser. """ return parse_notebook(path)
