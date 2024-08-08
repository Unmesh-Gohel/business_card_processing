from crewai import Crew, Process

crew = Crew(
    agents=[image_processing_agent, data_parsing_agent, database_insertion_agent],
    tasks=[image_processing_task, data_parsing_task, database_insertion_task],
    process=Process.sequential
)

# Assuming the image is located at 'business_card.jpg'
result = crew.kickoff(inputs={'image_path': 'business_card.jpg'})
print(result)
