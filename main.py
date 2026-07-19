import customtkinter as ctk

class MathDesk(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MathDesk")
        self.geometry("1000x650")

        # Create the sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        # Application name
        self.title_label = ctk.CTkLabel(self.sidebar, text="MathDesk", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(30, 25))

        # Sidebar buttons
        self.basic_button = ctk.CTkButton(self.sidebar, text="Basic Calculator", fg_color="transparent",
            command=lambda: self.select_button(self.basic_button))
        self.basic_button.pack(padx=20, pady=5)

        self.function_button = ctk.CTkButton(self.sidebar, text="Function Plot", fg_color="transparent",
            command=lambda: self.select_button(self.function_button))
        self.function_button.pack(padx=20, pady=5)

        self.chart_button = ctk.CTkButton(self.sidebar, text="Data Charts", fg_color="transparent",
            command=lambda: self.select_button(self.chart_button))
        self.chart_button.pack(padx=20, pady=5)

        self.calculus_button = ctk.CTkButton(self.sidebar, text="Calculus", fg_color="transparent",
            command=lambda: self.select_button(self.calculus_button))
        self.calculus_button.pack(padx=20, pady=5)

        self.numerical_button = ctk.CTkButton(self.sidebar,text="Numerical Methods", fg_color="transparent",
            command=lambda: self.select_button(self.numerical_button))
        self.numerical_button.pack(padx=20, pady=5)

        self.matrix_button = ctk.CTkButton(self.sidebar, text="Matrix", fg_color="transparent",
            command=lambda: self.select_button(self.matrix_button))
        self.matrix_button.pack(padx=20, pady=5)

    def select_button(self, selected_button):
        buttons = [
            self.basic_button,
            self.function_button,
            self.chart_button,
            self.calculus_button,
            self.numerical_button,
            self.matrix_button
        ]

        for button in buttons:
            button.configure(fg_color="transparent")

        selected_button.configure(fg_color="#1f6aa5")

app = MathDesk()
app.mainloop()