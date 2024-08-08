from crewai import Task

database_insertion_task = Task(
    description='Insert the parsed data into the database.',
    expected_output='Confirmation of data insertion.',
    tools=[insert_into_database],
    agent=database_insertion_agent,
)
