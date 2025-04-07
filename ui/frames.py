# 4. Módulo de frames (ui/frames.py)
import customtkinter as ctk

def criar_frames(app):
    frameLeft = ctk.CTkFrame(app, width=200, corner_radius=15)
    frameLeft.pack(fill = "y", side="left", padx = 10, pady=10)
    frameTop = ctk.CTkFrame(app, height=100, corner_radius=15)
    frameTop.pack(fill="x", side="top", padx = 10, pady=10)
    frameTabs = ctk.CTkTabview(app, corner_radius=15)
    frameTabs.pack(fill="both", expand=True, padx = 10)
    frameFooter =  ctk.CTkFrame(app, corner_radius=15, height=60)
    frameFooter.pack(fill = "x", anchor = "se", padx = 10, pady=10)

    

    return frameTop, frameTabs, frameLeft , frameFooter