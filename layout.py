import customtkinter as ctk

app = ctk.CTk()
app.title("Launcher")
app.geometry("900x650")
app.resizable(True, True)


frame_central = ctk.CTkFrame(app, corner_radius=10)
frame_central.pack(padx=10, pady=10, fill="both", expand=True)


def create_frame_left(app):
    frame_left = ctk.CTkFrame(master=app, width=200, corner_radius=0)
    frame_left.grid(row=0, column=0, sticky="ns")

    # Adicionando o botão "Início"
    inicio_button = ctk.CTkButton(
        master=frame_left,
        text="Início",
        command=lambda: print("Botão Início clicado!"),
        fg_color="transparent",
        text_color="black",
        hover_color="#e0e0e0",
        corner_radius=8
    )
    inicio_button.pack(pady=10, padx=10, anchor="nw")

    return frame_left
