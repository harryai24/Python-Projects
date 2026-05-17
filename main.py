from tkinter import * 
from tkinter import messagebox
import base64
import os

# Define global variables
screen = None
text1 = None
code = None

def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  # Remove extra spaces
        try:
            base64_bytes = base64.b64decode(message.encode("ascii"))  # Corrected decryption
            decrypted_message = base64_bytes.decode("ascii")
        except Exception as e:
            decrypted_message = "Invalid encrypted text!"

        Label(screen2, text="DECRYPTED TEXT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    else:
        messagebox.showerror("Encryption", "Invalid Password")

def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()
        base64_bytes = base64.b64encode(message.encode("ascii"))
        encrypted_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPTED TEXT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypted_message)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    else:
        messagebox.showerror("Encryption", "Invalid Password")

def reset():
    text1.delete(1.0, END)  # Clear text input
    code.set("")  # Clear secret key

def main_screen():
    global text1, code, screen
    
    screen = Tk()
    screen.geometry("375x398")
    screen.title("Cryptex 🛡️")

    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)
    
    text1 = Text(screen, font="Roboto 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(screen, text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)

    Button(screen, text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(screen, text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
