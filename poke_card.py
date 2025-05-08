import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import pytesseract as pt
import os

#TODO Add resizing filters to only read the cards name and set number
#TODO Find way to read the set symbol and match it to a symbol on a site such as pokesymbols.com/tcg/sets to get set name
#TODO Connect the application to Pokemon TCG API to get card details
#TODO Add messaging center for microservice usage

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class PokemonCard:

    def __init__(self, image_file):
        self._file_name = image_file
        self._img = Image.open(self._file_name)
        self._img.show()

        self._img_copy = self._img.copy()
        self._width, self._height = self._img.size
        self._crop_card()
        self._img.show()

        self._set = self._get_set_name()
        self._card_num = self._get_card_num()
        self._card_code = None

    def get_card(self):
        """
        Get the card code for the card object -> [set_code + card_num]
        Will return teh card code if identified.
        Will return -1 if card can not be identified or if an error occcured.
        """
        if self._set == -1:
            self._card_code = -1
        elif self._card_num == -1:
            self._card_code = -1

        return self._card_code

    def _get_set_name(self):
        """
        Method to fetch the name of the set for the object card.
        If found it will return the set code.
        Will return -1 if set can not be identified.  
        """
        pass
    
    def _get_card_num(self):
        """
        Method to fetch the card number for the object card.
        If found it will return the card number of the card object.
        WIll return -1 if card_num can not be identified.
        """
        pass
        
    def _crop_card(self):
        """Will cut the card image in half to view only necessary details"""
        new_height = self._height / 2
        left = 0
        top = new_height
        right = self._width
        bottom = self._height

        self._img = self._img.crop((left, top, right, bottom))
