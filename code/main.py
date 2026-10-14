"""Entry point for the File Encryption Tool.

Run this file to open the GUI window: python main.py
"""
from ui.pages import EncryptionApp

if __name__ == "__main__":
    app = EncryptionApp()
    app.mainloop()