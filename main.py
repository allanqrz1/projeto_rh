from ui.app import iniciar_app
import customtkinter as ctk
from telas.login_view import LoginView
from controllers.loginController import validar_login
import time

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("App com Login")

        self.login_view = LoginView(self, self.on_login)
        self.login_view.pack(expand=True)

    def on_login(self, usuario, senha):
        if validar_login(usuario, senha):
            self.destroy()

        else:
            erro = ctk.CTkLabel(self, text="Usuário ou senha inválidos", text_color="red")
            erro.pack(pady=20)

if __name__ == "__main__":
    login = App()
    if validar_login():
        return iniciar_app()
    login.mainloop()