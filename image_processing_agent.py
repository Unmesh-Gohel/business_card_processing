from crewai import Agent
from ocr_tool import ocr_tool

image_processing_agent = Agent(
    role='Image Processing Agent',
    goal='Extract text from business card images.',
    verbose=True,
    memory=True,
    tools=[ocr_tool],
    backstory='You are skilled in processing images and extracting text using OCR technology.'
)
