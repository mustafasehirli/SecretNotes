import tkinter
from PIL import Image, ImageTk
from cryptography.fernet import Fernet


window = tkinter.Tk()
window.minsize(width=400, height=700)
window.config(padx=20, pady=20)
open_image = Image.open("download.png")
image = ImageTk.PhotoImage(open_image)


# onclick save button
def onclick_save_button():
    title = note_title_entry.get()
    key = Fernet.generate_key()
    fernet = Fernet(key)
    data_text = note_text.get(1.0, "end")
    encrypted = fernet.encrypt(bytes(data_text, "utf-8"))
    with open(f"{title}.txt", mode="wb") as file:
        file.write(encrypted)
    note_title_entry.delete(0, "end")
    note_text.delete(1.0, "end")


# onclick fetch button
def onclick_fetch_button():
    pass


# image
image_label = tkinter.Label(image=image)
image_label.config(width=75, height=75)
image_label.pack()

# # note title
note_title = tkinter.Label()
note_title.config(text="Note Title", pady=10, padx=20)
note_title.pack()

# Entry
note_title_entry = tkinter.Entry()
note_title_entry.pack()

# # note text title
note_title_text = tkinter.Label()
note_title_text.config(text="Note Text", pady=10, padx=20)
note_title_text.pack()


# text
note_text = tkinter.Text()
note_text.config(width=30, height=10)
note_text.pack()

# # password title
password_title = tkinter.Label()
password_title.config(text="Password Title", pady=10, padx=20)
password_title.pack()

# password Entry
password_entry = tkinter.Entry()
password_entry.pack()

# Save Button
save_button = tkinter.Button()
save_button.config(text="Save", padx=10, command=onclick_save_button)
save_button.pack()

# Fetch Button
save_button = tkinter.Button()
save_button.config(text="Fetch", padx=10, command=onclick_fetch_button)
save_button.pack()

window.mainloop()
