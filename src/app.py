# this file is part of coin-tracker by opdavi1 and subject to the GNU GPL-3.0-or-later license.
# See LICENSE for details or go to <https://www.gnu.org/licenses/>

import tkinter as tk


class CoinTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry = "800x500"

        # Keep at bottom of __init__
        self.window.mainloop()
