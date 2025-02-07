import os
from PIL import Image 
from pytesseract import pytesseract

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Um diretório acima
WORKING_DIR = os.path.dirname(os.path.realpath(__file__)) # Diretório atual

path_to_tesseract = f"{BASE_DIR}\\tesseract-ocr\\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

image_path = f"{WORKING_DIR}\\sample_text.jpg"
img = Image.open(image_path)

text = pytesseract.image_to_string(img)
print(text[:-1])
