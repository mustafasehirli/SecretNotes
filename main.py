import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.minsize(width=400, height=700)
window.config(padx=20, pady=20)
open_image = Image.open("download.png")
image = ImageTk.PhotoImage(open_image)


# onclick save button
def onclick_save_button():
    pass


# onclick fetch button
def onclick_fetch_button():
    pass


# image
image_label = tkinter.Label(image=image)
image_label.config(width=75, height=75)
image_label.pack()

# note title
password_title = tkinter.Label()
password_title.config(text="Note Title", pady=10, padx=20)
password_title.pack()

# Entry
password_entry = tkinter.Entry()
password_entry.pack()

# note text title
note_text = tkinter.Label()
note_text.config(text="Note Text", pady=10, padx=20)
note_text.pack()

# text
text = tkinter.Text()
text.config(width=30, height=10, pady=30)
text.pack()

# password title
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
