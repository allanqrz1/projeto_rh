# 2. Módulo de interface (ui/app.py)
import customtkinter as ctk
from ui.frames import criar_frames, adicionar_botao_home
from ui.imagens import carregar_logo
from ui.estilo import aplicar_tema

def iniciar_app():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Launcher")
    
    aplicar_tema(app)

    # Criar e empacotar os frames principais
    frameTop, frameLeft,frameTabs, frameFooter = criar_frames(app)
    adicionar_botao_home(frameLeft)

    # Logo no topo
    logo = carregar_logo()
    if logo:
        lbl_logo = ctk.CTkLabel(frameTop, image=logo, text="")
        lbl_logo.pack(side="left", padx=15, pady=10, anchor="s")
    app.mainloop()
