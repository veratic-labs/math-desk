import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np

class FunctionPlot(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        #function plot title
        self.title_label = ctk.CTkLabel(self, text="Function Plot", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(anchor="w", padx=20, pady=(20, 10))

        #a frame of input, including y=... and an entry
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(anchor="w", padx=20, pady=10)

        self.y_label = ctk.CTkLabel(self.input_frame, text="y =")
        self.y_label.pack(side="left", padx=(0, 10))

        self.function_entry = ctk.CTkEntry(self.input_frame, width=300, placeholder_text="Enter a function...")
        self.function_entry.pack(side="left")

        #x min and x max
        self.x_range_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.x_range_frame.pack(anchor="w", padx=20, pady=10)

        self.xmin_label = ctk.CTkLabel(self.x_range_frame, text="X Min")
        self.xmin_label.pack(side="left", padx=(0, 5))

        self.xmin_entry = ctk.CTkEntry(self.x_range_frame, width=80)
        self.xmin_entry.pack(side="left", padx=(0, 20))

        self.xmax_label = ctk.CTkLabel(self.x_range_frame, text="X Max")
        self.xmax_label.pack(side="left", padx=(0, 5))

        self.xmax_entry = ctk.CTkEntry(self.x_range_frame, width=80)
        self.xmax_entry.pack(side="left")

        #default values of x min and x max
        self.xmin_entry.insert(0, "-10")
        self.xmax_entry.insert(0, "10")

        #button frame
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(anchor="w", padx=20, pady=(10, 20))

        #calculate button
        self.calculate_button = ctk.CTkButton(self.button_frame, text="Calculate", width=100, command=self.plot_function)
        self.calculate_button.pack(side="left")

        #clear button
        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear", width=80, command=self.clear)
        self.clear_button.pack(side="left", padx=(10, 0))

        #warning label
        self.warning = ctk.CTkLabel(self, text="Invalid Input", font=ctk.CTkFont(size=16))
    
    def plot_function(self):
        self.warning.pack_forget()
        
        points_num = 1000

        #enable users to enter special values for x min and max
        safe_globals = {
            "__builtins__": {},
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "pi": np.pi,
            "e": np.e,
            "sqrt": np.sqrt,
            "log": np.log,
            "log10": np.log10,
            "exp": np.exp,
        }
        
        #get values
        function = self.function_entry.get()
        x_min = eval(self.xmin_entry.get(), safe_globals, {})
        x_max = eval(self.xmax_entry.get(), safe_globals, {})

        x = np.linspace(x_min, x_max, points_num)

        #safe globals for functions
        safe_globals = {
            "__builtins__": {},
            "x": x,
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "sqrt": np.sqrt,
            "log": np.log,
            "log10": np.log10,
            "exp": np.exp,
            "pi": np.pi,
            "e": np.e,
            "abs": abs,
            "round": round,
        }
        
        #draw the graph
        try:
            y = eval(function, safe_globals, {})
            plt.plot(x, y)
            
            #adjust axis
            ax = plt.gca()
            ax.spines["left"].set_position("zero")
            ax.spines["bottom"].set_position("zero")

            ax.spines["right"].set_color("none")
            ax.spines["top"].set_color("none")

            ax.xaxis.set_ticks_position("bottom")
            ax.yaxis.set_ticks_position("left")

            plt.title(f"y = {function}")
            plt.show()
        
        except Exception:
            self.warning.pack(fill="x", padx=20)

    def clear(self):
        self.function_entry.delete(0, "end")
        self.xmin_entry.delete(0, "end")
        self.xmax_entry.delete(0, "end")
        self.warning.configure(text="")

        plt.close()