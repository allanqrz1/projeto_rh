# 4. Módulo de frames (ui/frames.py)
import customtkinter as ctk


import customtkinter as ctk

def criar_frames(app):
    frameLeft = ctk.CTkFrame(app, width=120, corner_radius=15)
    frameLeft.pack(fill="y", side="left", padx=10, pady=10)
    frameTop = ctk.CTkFrame(app, height=100, corner_radius=15)
    frameTop.pack(fill="x", side="top", padx=10, pady=10)
    frameTabs = ctk.CTkTabview(app, corner_radius=15)
    frameTabs.pack(fill="both", expand=True, padx=10)
    frameFooter = ctk.CTkFrame(app, corner_radius=15, height=60)
    frameFooter.pack(fill="x", anchor="se", padx=10, pady=10)

    return frameTop, frameTabs, frameLeft, frameFooter

def adicionar_botao_home(frameLeft):
    """Adiciona um botão 'Home' ao frameLeft."""
    def acao_home():
        print("Botão Home clicado!")

    btn_home = ctk.CTkButton(
        frameLeft, 
        text="Home", 
        command=acao_home, 
        width=100, 
        height=40, 
        fg_color="black",
        text_color="white",
    )
    btn_home.grid(pady=20, padx=20)
