
import tkinter
from PIL import Image, ImageTk
import base64


window = tkinter.Tk()
window.minsize(width=400, height=700)
window.config(padx=20, pady=20)
open_image = Image.open("topsecret.png")
image = ImageTk.PhotoImage(open_image)


# onclick save button
def onclick_save_button():
    title = note_title_entry.get()
    data = note_text.get(1.0, "end")

    data_bytes = data.encode("utf-8")
    base64_bytes = base64.b64encode(data_bytes)
    base64_string = base64_bytes.decode('utf-8')

    with open(f"{title}.txt", mode="wb") as file:
        file.write(base64_string.encode('utf-8'))
    file.close()

    note_title_entry.delete(0, "end")
    note_text.delete(1.0, "end")


# onclick fetch button
def onclick_fetch_button():
    base64_string = note_text.get(1.0, "end")
    base64_bytes = base64_string.encode('utf-8')
    data_bytes = base64.b64decode(base64_bytes)
    data = data_bytes.decode('utf-8')
    note_text.delete("1.0", "end")
    for i in data:
        note_text.insert("end", i)


# image
image_label = tkinter.Label(image=image)
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
