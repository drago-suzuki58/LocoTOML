import tkinter as tk
from tkinter import messagebox
from locotoml import LocoTOML
import locale
import webbrowser

# Get the system locale
system_locale = locale.getdefaultlocale()[0].split('_')[0] or "en"
if system_locale not in ["ja", "en"]:
    system_locale = "en"

# Create a LocoTOML object
loc = LocoTOML(system_locale)

def change_language(lang):
    loc.change_locale(lang)
    root.title(loc.content.title())
    message_label.config(text=loc.content.message())
    error_button.config(text=loc.button.demo.error())
    warning_button.config(text=loc.button.demo.warning())
    create_menu_labels()

def create_menu_labels():
    # initial menu
    menubar.delete(0, tk.END)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label=loc.label.file.new_file())
    filemenu.add_command(label=loc.label.file.new_folder())
    filemenu.add_command(label=loc.label.file.open_file())
    filemenu.add_command(label=loc.label.file.open_folder())
    filemenu.add_separator()
    filemenu.add_command(label=loc.label.file.quit(), command=root.quit)
    menubar.add_cascade(label=loc.menubar.file(), menu=filemenu)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label=loc.label.edit.undo())
    editmenu.add_command(label=loc.label.edit.redo())
    editmenu.add_separator()
    editmenu.add_command(label=loc.label.edit.cut())
    editmenu.add_command(label=loc.label.edit.copy())
    editmenu.add_command(label=loc.label.edit.paste())
    editmenu.add_command(label=loc.label.edit.delete())
    editmenu.add_separator()
    editmenu.add_command(label=loc.label.edit.select_all())
    menubar.add_cascade(label=loc.menubar.edit(), menu=editmenu)

    viewmenu = tk.Menu(menubar, tearoff=0)
    viewmenu.add_command(label=loc.label.view.reload())
    viewmenu.add_command(label=loc.label.view.toggle_fullscreen())
    viewmenu.add_command(label=loc.label.view.toggle_devtools())
    menubar.add_cascade(label=loc.menubar.view(), menu=viewmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label=loc.label.help.about(), command=lambda: webbrowser.open("https://github.com/drago-suzuki58/LocoTOML"))
    menubar.add_cascade(label=loc.menubar.help(), menu=helpmenu)

    langmenu = tk.Menu(menubar, tearoff=0)
    langmenu.add_command(label="日本語", command=lambda: change_language("ja"))
    langmenu.add_command(label="English", command=lambda: change_language("en"))
    langmenu.add_command(label="Unknown", command=lambda: change_language("unknown"))
    menubar.add_cascade(label=loc.menubar.language(), menu=langmenu)

def error_message_demo():
    messagebox.showerror(loc.system.error.title(), loc.system.error.message())

def warning_message_demo():
    messagebox.showwarning(loc.system.warning.title(), loc.system.warning.message())

# Create a Tkinter window
root = tk.Tk()
root.geometry("800x600")
root.title(loc.content.title())

menubar = tk.Menu(root)

create_menu_labels()

root.config(menu=menubar)

message_label = tk.Label(root, text=loc.content.message())
message_label.pack()

error_button = tk.Button(root, text=loc.button.demo.error(), command=error_message_demo)
error_button.pack(pady=10)

warning_button = tk.Button(root, text=loc.button.demo.warning(), command=warning_message_demo)
warning_button.pack(pady=10)

root.mainloop()