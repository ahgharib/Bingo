try:
    import tkinter as tk
except ImportError as e1:
    print(f"Error importing modules {e1}")
    exit(1)
except: # general exception catch
    print("An unexpected error occurred during module import")
    exit(1)

class Bingo:
    def __init__(self, username, drive_link):
        self.username = username
        self.drive_link = drive_link
    
    def display_info(self):
        print(f"Username: {self.username}")
        print(f"Drive Link: {self.drive_link}")
    
    def edit_name(self, new_name):
        self.username = new_name
        print(f"Username updated to: {self.username}")
    
    def edit_drive_link(self, new_link):
        self.drive_link = new_link
        print(f"Drive Link updated to: {self.drive_link}")


class BingoApp:
    window = tk.BaseWidget()
    window.mainloop()