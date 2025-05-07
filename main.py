from PIL import Image, ImageFilter, ImageEnhance
import pytesseract as PT

#TODO Add resizing filters to only read the cards name and set number
#TODO Find way to read the set symbol and match it to a symbol on a site such as pokesymbols.com/tcg/sets to get set name
#TODO Connect the application to Pokemon TCG API to get card details
#TODO Add messaging center for microservice usage


PT.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("test.png")

text = PT.image_to_string(img)

print(text)