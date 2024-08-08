from crewai import Agent
import re

def parse_text(text: str) -> dict:
    """
    Parses the extracted text to identify relevant information.
    :param text: Extracted text from OCR.
    :return: Parsed data as a dictionary.
    """
    data = {
        'name': re.search(r'Name: (.+)', text).group(1),
        'title': re.search(r'Title: (.+)', text).group(1),
        'company': re.search(r'Company: (.+)', text).group(1),
        'phone': re.search(r'Phone: (.+)', text).group(1),
        'email': re.search(r'Email: (.+)', text).group(1),
    }
    return data

data_parsing_agent = Agent(
    role='Data Parsing Agent',
    goal='Parse extracted text from business cards.',
    verbose=True,
    memory=True,
    tools=[],
    backstory='You are adept at identifying and parsing relevant information from text.'
)
