import customtkinter as ctk

app = ctk.CTk()
app.title("Launcher")
app.geometry("900x650")
app.resizable(True, True)



frame_central = ctk.CTkFrame(app, corner_radius=10)
frame_central.pack(padx=10, pady=10, fill="both", expand=True)
