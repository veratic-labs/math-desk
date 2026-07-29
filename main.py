"""
MathDesk
A lightweight desktop mathematics application built with Python

Copyright (c) Veratic Labs
Licensed under the Apache License, Version 2.0
"""

import customtkinter as ctk

from sidebar import Sidebar
from basic import BasicCalculator
from function import FunctionPlot
from calculus import Calculus
from solve import SolveEquation

class MathDesk(ctk.CTk):
    def __init__(self):
        super().__init__()

        #initial window settings
        self.title("MathDesk")
        self.iconbitmap("icon.ico")
        self.geometry("600x400")

        #run all pages
        self.sidebar = Sidebar(self)
        self.basic = BasicCalculator(self)
        self.function = FunctionPlot(self)
        self.calculus = Calculus(self)
        self.solve = SolveEquation(self)

        #show pages
        self.sidebar.pack(side="left", fill="y")
        self.basic.pack(side="left", fill="both", expand=True)

    def change_page(self, page, selected_button):
        self.basic.pack_forget()
        self.function.pack_forget()
        self.calculus.pack_forget()
        self.solve.pack_forget()

        page.pack(side="left", fill="both", expand=True)

        self.sidebar.change_button_color(selected_button)

app = MathDesk()
app.mainloop()