
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import base64


window = tkinter.Tk()
window.minsize(width=400, height=700)
window.config(padx=20, pady=20)
open_image = Image.open("topsecret.png")
image = ImageTk.PhotoImage(open_image)


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


# onclick save button
def onclick_save_button():
    title = note_title_entry.get()
    message = note_text.get(1.0, "end")
    password = password_entry.get()

    if title == "" or message == "" or password == "" :
        tkinter.messagebox.showerror(title="Error", message="Please enter all info")

    else:
        message_encrypted = encode(password, message)

        try:
            with open(f"MyText.txt", mode="a") as file:
                file.write(f"\n{title}\n{message_encrypted}")
            file.close()
        except FileNotFoundError:
            with open(f"MyText.txt", mode="w") as file:
                file.write(f"\n{title}\n{message_encrypted}")
            file.close()
        finally:
            note_title_entry.delete(0, "end")
            note_text.delete(1.0, "end")
            password_entry.delete(0, "end")


# onclick fetch button
def onclick_fetch_button():
    message = note_text.get(1.0, "end")
    password = password_entry.get()

    if message == "" or password == "" :
        tkinter.messagebox.showerror(title="Error", message="Please enter all info")

    else:
        try:
            message_encrypted = decode(password, message)
            note_text.delete(1.0, "end")
            note_text.insert("1.0", message_encrypted)
        except:
            tkinter.messagebox.showerror(title="Error", message="Please make sure of encrypted info.")


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
