import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

def open_file():
    """Open a file for editing."""
    filepath= askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All files", "*.*")]
        )
    if not filepath: return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes = [("Text Files", "*.txt"), ("Python files", "*.py"), ("All Files", "*.*")]
        )
    if not filepath: return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

window = tk.Tk()
window.title('Text Editor')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

fr_buttons = tk.Frame(master = window, relief=tk.RAISED, borderwidth=1, relief = tk.RAISED, borderwidth=5)

btn_open = tk.Button(master = fr_buttons, text='Open', command = open_file, bg='DeepSkyBlue')
btn_save = tk.Button(master = fr_buttons, text = 'Save As', command = save_file, bg='DeepSkyBlue')

btn_open.grid(row=0, column= 0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')

txt_edit = tk.Text(master = window, bg='cornflower blue', borderwidth=5, relief=tk.RAISED)
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()
