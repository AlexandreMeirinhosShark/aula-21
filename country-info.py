import requests as rq
import tkinter as tk
from io import BytesIO as Byt
from PIL import Image, ImageTk
from deep_translator import LibreTranslator as Translate


def search():
    try:
        print()  # temp
    except KeyError:
        print("Erro. País não indentificado.")
