import tkinter as tk
class GameUI:
    def __init__(self):
        window = tk.Tk()
        label = tk.Label(text='Tura gracza 2', master=window)
        label.pack(side='top')
        main_frame = tk.Frame(master=window)
        main_frame.pack(side='top')
        color ="#000000"
        secondary_c = '#ffffff'
        for i in range(8):
            for j in range(8):
                button = tk.Button (
                    master=main_frame,
                    relief=tk.RAISED,
                    borderwidth=1,
                    padx = 10,
                    pady = 10,
                    fg = color,
                    bg= secondary_c,
                    text = f"Row {i}\nColumn {j}"

                )
                button.grid(row=i, column=j)
                color = '#000000' if color=='#ffffff' else '#ffffff'
                secondary_c = '#ffffff' if color == '#000000' else '#000000'
            color = '#000000' if color == '#ffffff' else '#ffffff'
            secondary_c = '#ffffff' if color == '#000000' else '#000000'
        window.mainloop()