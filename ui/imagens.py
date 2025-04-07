# 5. Módulo de imagens (ui/imagens.py)
import os
from PIL import Image
import customtkinter as ctk

def carregar_logo():
    img_path = "logo.png"
    if os.path.exists(img_path):
        image = Image.open(img_path)
        return ctk.CTkImage(light_image=image, dark_image=image, size=(120, 120))
    return None

def carregar_icone(caminho, tamanho):
    if os.path.exists(caminho):
        image = Image.open(caminho)
        return ctk.CTkImage(light_image=image, dark_image=image, size=tamanho)
    return None

icon_autochrome = carregar_icone("icon1.png", (20, 20))
icon_fazeradmissao = carregar_icone("icon2.png", (20, 20))
icon_excel = carregar_icone("icon3.png", (20, 20))
icon_gmail = carregar_icone("gmail.png", (20, 20))
icon_lock = carregar_icone("padlock.png", (25, 25))
icon_quit = carregar_icone("quit.png", (30, 30))