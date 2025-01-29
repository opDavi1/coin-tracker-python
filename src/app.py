# app.py is part of coin_tracker by opDavi1; see LICENSE for details

import tkinter as tk


class CoinTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry = "800x500"

        # Keep at bottom of __init__
        self.window.mainloop()
