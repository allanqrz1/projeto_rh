import customtkinter as ctk
from tkinter import messagebox
from ui.app import iniciar_app

def mostrar_login(app):
    janela_login = ctk.CTkToplevel(app)
    # ... resto do código ...

    def tentar_login(event=None):
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario == "admin" and senha == "1234":
            for btn in ():
                btn.configure(state="normal")
            janela_login.destroy()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    lbl_usuario = ctk.CTkLabel(janela_login, text="Usuário")
    lbl_usuario.pack(pady=(15, 5))
    entry_usuario = ctk.CTkEntry(janela_login)
    entry_usuario.pack(pady=5)

    lbl_senha = ctk.CTkLabel(janela_login, text="Senha")
    lbl_senha.pack(pady=5)
    entry_senha = ctk.CTkEntry(janela_login, show="*")
    entry_senha.pack(pady=5)

    btn_login = ctk.CTkButton(janela_login, text="Login", command=tentar_login)
    btn_login.pack(pady=15)

    entry_senha.bind("<Return>", tentar_login)
    entry_usuario.focus()

