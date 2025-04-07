# Modelo 1 - Estrutura com tela de login separada
# Arquivo: telas/login_view.py
import customtkinter as ctk

class LoginView(ctk.CTkFrame):
    def __init__(self, master, on_login_callback):
        super().__init__(master)
        self.on_login_callback = on_login_callback

        self.label_user = ctk.CTkLabel(self, text="Usuário")
        self.label_user.pack(pady=5)

        self.entry_user = ctk.CTkEntry(self)
        self.entry_user.pack(pady=5)

        self.label_pass = ctk.CTkLabel(self, text="Senha")
        self.label_pass.pack(pady=5)

        self.entry_pass = ctk.CTkEntry(self, show="*")
        self.entry_pass.pack(pady=5)

        self.btn_login = ctk.CTkButton(self, text="Login", command=self.realizar_login)
        self.btn_login.pack(pady=10)

    def realizar_login(self):
        usuario = self.entry_user.get()
        senha = self.entry_pass.get()
        self.on_login_callback(usuario, senha)