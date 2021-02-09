import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"D:\OCR - Tesseract\tesseract.exe"

img = Image.open('image1.png')
text = pytesseract.image_to_string('image1.png')
print(text)
