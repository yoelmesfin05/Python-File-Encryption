"""Graphical user interface for the File Encryption Tool.

Defines the main Tkinter window that lets the user pick a file and
encrypt or decrypt it.
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from core.encryption import generate_key, encrypt_data, decrypt_data
from core.data import save_key_to_file, read_target_file, write_target_file, load_key_from_file


class EncryptionApp(tk.Tk):
    """Main window of the File Encryption Tool.

    Holds the currently selected file path and provides buttons to
    browse for a file, encrypt it and decrypt it.
    """

    def __init__(self):
        """Create the window and build the file selection and action sections."""
        super().__init__()
        self.title("File Encryption Tool")
        self.geometry("550x450")
        self.resizable(False, False)  #prevents window resizing

        self.selected_file_path = tk.StringVar() #remembers which file is being selected

        #file selection section

        file_frame = ttk.LabelFrame(self, text="1. Select File", padding = 15)
        file_entry = ttk.Entry(file_frame, textvariable = self.selected_file_path, width = 42)
        browse_button = ttk.Button(file_frame, text="Browse", command = self.browse_file)

        file_frame.pack(fill = "x", padx = 20, pady = 10)
        file_entry.pack(side = "left", padx=(0, 10))
        browse_button.pack(side = "left")

        action = ttk.LabelFrame(self, text = "2. Encrypt / Decrypt", padding = 15)
        encrypt = ttk.Button(action, text = "Encrypt", command = self.encrypt_file)
        decrypt = ttk.Button(action, text = "Decrypt", command = self.decrypt_file)
    
        action.pack(fill = "x", padx = 20, pady = 10)
        encrypt.pack(side = "left", padx = (0, 10))
        decrypt.pack(side = "left")
    
    def browse_file(self):
        """Open a file picker and store the chosen file path."""
        filename = filedialog.askopenfilename()
        if filename:
            self.selected_file_path.set(filename)


    def encrypt_file(self):
        """Encrypt the selected file in place.

        Gets the key (reusing secret.key if it exists), saves it, then
        overwrites the file with its encrypted contents. Shows a success
        or error message to the user.
        """
        file_path = self.selected_file_path.get()
        
        if not file_path:
            messagebox.showerror("Error", "Please select a file first!")    
            return
        
        try: 

            key = generate_key()
            save_key_to_file(key, "secret.key")

            file_data = read_target_file(file_path)
            encrypted_data = encrypt_data(key, file_data)
            
            write_target_file(file_path, encrypted_data)
            
            messagebox.showinfo("Success!", "File encyrpted successfully!")
        
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
            return

            
    def decrypt_file(self):
        """Decrypt the selected file in place.

        Loads the key from secret.key and overwrites the file with its
        decrypted contents. Shows a success or error message to the user,
        including when the key is wrong or the file is not encrypted.
        """
        file_path = self.selected_file_path.get()
        
        if not file_path:       # if user doesn't select a file, return this response
            messagebox.showerror("Error", "Please select a file first!")
            return
        
        try:

            key = load_key_from_file("secret.key")    # generate the file
            encrypted_data = read_target_file(file_path)

            decrypted_data = decrypt_data(key, encrypted_data)
            write_target_file(file_path, decrypted_data)

            messagebox.showinfo("Success!", "File decrypted successfully!")
        
        except Exception as e:
                messagebox.showerror("Error", f"Couldn't decrypt file: {e}")
                return