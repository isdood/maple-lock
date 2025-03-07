import tkinter as tk
from theme_engine import apply_theme

class MapleLockInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Maple Lock")
        self.apply_theme()

    def apply_theme(self):
        theme_color = apply_theme()
        self.root.configure(bg=f'#{theme_color[0]:02x}{theme_color[1]:02x}{theme_color[2]:02x}')

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    interface = MapleLockInterface(root)
    interface.run()
