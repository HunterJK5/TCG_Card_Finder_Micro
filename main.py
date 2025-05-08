import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import pytesseract as PT
import os
from poke_card import PokemonCard
#TODO Add resizing filters to only read the cards name and set number
#TODO Find way to read the set symbol and match it to a symbol on a site such as pokesymbols.com/tcg/sets to get set name
#TODO Connect the application to Pokemon TCG API to get card details
#TODO Add messaging center for microservice usage


PT.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

my_card = PokemonCard("test.png")