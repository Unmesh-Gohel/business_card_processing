from crewai_tools import tool
import pytesseract
from PIL import Image

@tool
def ocr_tool(image_path: str) -> str:
    """
    Tool to extract text from an image using Tesseract OCR.
    :param image_path: Path to the image file.
    :return: Extracted text.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)
