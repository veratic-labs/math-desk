import customtkinter as ctk

from sidebar import Sidebar
from basic import BasicCalculator

class MathDesk(ctk.CTk):
    def __init__(self):
        super().__init__()

        #initial window settings
        self.title("MathDesk")
        self.geometry("600x400")

        #run all pages
        self.sidebar = Sidebar(self)
        self.basic = BasicCalculator(self)

        #show pages
        self.sidebar.pack(side="left", fill="y")
        self.basic.pack(side="left", fill="both", expand=True)

app = MathDesk()
app.mainloop()