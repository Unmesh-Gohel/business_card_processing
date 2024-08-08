from crewai import Agent
from database_tool import insert_into_database

database_insertion_agent = Agent(
    role='Database Insertion Agent',
    goal='Insert parsed data into the database.',
    verbose=True,
    memory=True,
    tools=[insert_into_database],
    backstory='You ensure the accurate insertion of data into the database.'
)
