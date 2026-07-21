import customtkinter as ctk

from sidebar import Sidebar
from basic import BasicCalculator
from function import FunctionPlot

class MathDesk(ctk.CTk):
    def __init__(self):
        super().__init__()

        #initial window settings
        self.title("MathDesk")
        self.geometry("600x400")

        #run all pages
        self.sidebar = Sidebar(self)
        self.basic = BasicCalculator(self)
        self.function = FunctionPlot(self)

        #show pages
        self.sidebar.pack(side="left", fill="y")
        self.basic.pack(side="left", fill="both", expand=True)

    def change_page(self, page, selected_button):
        self.basic.pack_forget()
        self.function.pack_forget()

        page.pack(side="left", fill="both", expand=True)

        self.sidebar.change_button_color(selected_button)

app = MathDesk()
app.mainloop()