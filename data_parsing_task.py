from crewai import Task

data_parsing_task = Task(
    description='Parse the extracted text to identify relevant information.',
    expected_output='Parsed data from the business card text.',
    tools=[],
    agent=data_parsing_agent,
)
