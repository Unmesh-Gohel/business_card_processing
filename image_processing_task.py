from crewai import Task

image_processing_task = Task(
    description='Capture and process the image of the business card to extract text.',
    expected_output='Extracted text from the business card image.',
    tools=[ocr_tool],
    agent=image_processing_agent,
)
