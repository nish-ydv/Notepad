import os
from tkinter import *
from tkinter import messagebox,filedialog
def open_file(event=None):
    filepath=filedialog.askopenfilename(title="Select File")
    if not filepath:
        return
    try:
        with open(filepath,"r") as file:
            data=file.read()
            textbox.delete("1.0",END)
            textbox.insert(END,data)
            textbox.config(state=DISABLED)
            word_count()
    except FileNotFoundError:
        messagebox.showerror("Error","File Not Found")
def save_file(event=None):
    filepath=filedialog.asksaveasfilename(title="Save File As:",
                                          defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                                          )
    if not filepath:
        return
    try:
        content = textbox.get("1.0",END)
        with open(filepath,"w") as file:
            file.write(content)
            messagebox.showinfo("Saved","File Saved Successfully")
    except Exception as e:
        messagebox.showerror("Error",f"could not save file: \n{e}")
def edit_file():
    textbox.config(state=NORMAL)
    messagebox.showinfo("Edit Mode","Editing Enabled")
def delete_file():
    filepath=filedialog.askopenfilename(title="Select File")
    if not filepath:
        return
    confirmation = messagebox.askyesno("Delete","Delete File?")
    if confirmation:
        try:
            os.remove(filepath)
            messagebox.showinfo("Deleted","File Deleted Successfully")
        except FileNotFoundError:
            messagebox.showerror("Error","File Not Found")
def New_File():
    textbox.delete("1.0",END)
def word_count(event=None):
    text = textbox.get("1.0",END)
    words = len(text.split())
    word_count_label.config(text=str(words))
    window.update_idletasks()
def toggle_mode():
    global dark_mode
    if dark_mode:
        window.config(bg="#F0F0F0")
        textbox.config(bg="light yellow",fg="dark gray",insertbackground="black")
        label.config(bg="black",fg="white")
        word_count_label.config(bg="black",fg="white")
        button.config(text="Dark Mode",image=small_photo)
        dark_mode = False
    else:
        window.config(bg="#1E1E1E")
        textbox.config(bg="#2C2C2C", fg="#FFFFFF", insertbackground="white")
        label.config(bg="white", fg="black")
        word_count_label.config(bg="white", fg="black")
        button.config(text="Light Mode", image=small_photo2)
        dark_mode = True
dark_mode = False
window = Tk()
window.title("Notepad")
window.state("zoomed")
window.geometry("1000x800")
menubar = Menu(window)
window.config(menu=menubar,bg="#F0F0F0")
FileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="Open",command=open_file)
FileMenu.add_command(label="Edit",command=edit_file)
FileMenu.add_command(label="Save",command=save_file)
FileMenu.add_command(label="Delete", command=delete_file)
FileMenu.add_separator()
FileMenu.add_command(label="New File", command=New_File)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=window.destroy)

textbox = Text(window, width=100,height=30,bg="light yellow",font=('Ink Free',20,'bold'),fg="dark gray")
textbox.grid(row=0,column=0,columnspan=3,padx=20,pady=20,sticky="nsew")

textbox.bind("<Control-o>",open_file)
textbox.bind("<Control-s>",save_file)

label = Label(window,text="Number of Words: ",font=("Arial",15,"bold"),bg="black",fg="white")
label.grid(row=1,column=1,sticky="e",padx=5,pady=10)
word_count_label = Label(window,text="0",font=("Arial",15,"bold"),bg="black",fg="white")
word_count_label.grid(row=1,column=2,sticky="w",padx=5,pady=10)

textbox.bind("<KeyRelease>",word_count)
photo = PhotoImage(file="night-mode_6277998.png")
photo2 = PhotoImage(file="bright_17135304.png")
small_photo= photo.subsample(20,20)
small_photo2 = photo2.subsample(20,20)
button = Button(window,text="Dark mode",font=("Inter",12,"bold"),
                image=small_photo,
                command=toggle_mode,
                compound=TOP,padx=10,pady=10,
                relief=RIDGE)
button.grid(row=1,column=0,sticky="w",padx=5,pady=10)

window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
window.mainloop()
