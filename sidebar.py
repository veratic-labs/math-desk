import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=200, corner_radius=0)
        
        # Application name
        self.title_label = ctk.CTkLabel(self, text="MathDesk", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(30, 25))

        # Sidebar buttons
        self.basic_button = ctk.CTkButton(self, text="Basic Calculator", fg_color="#1f6aa5",
            command=lambda: master.change_page(master.basic, self.basic_button))
        self.basic_button.pack(padx=20, pady=5)

        self.function_button = ctk.CTkButton(self, text="Function Plot", fg_color="transparent",
            command=lambda: master.change_page(master.function, self.function_button))
        self.function_button.pack(padx=20, pady=5)

        self.calculus_button = ctk.CTkButton(self, text="Calculus", fg_color="transparent",
            command=lambda: master.change_page(master.calculus, self.calculus_button))
        self.calculus_button.pack(padx=20, pady=5)

        self.solve_button = ctk.CTkButton(self,text="Solve Equation", fg_color="transparent",
            command=lambda: master.change_page(master.solve, self.solve_button))
        self.solve_button.pack(padx=20, pady=5)

    def change_button_color(self, selected_button):
        self.buttons = [
            self.basic_button,
            self.function_button,
            self.calculus_button,
            self.solve_button,
        ]
        
        for button in self.buttons:
            button.configure(fg_color="transparent")

        selected_button.configure(fg_color="#1f6aa5")

