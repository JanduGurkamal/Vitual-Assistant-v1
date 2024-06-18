import tkinter as tk

root = tk.Tk()
root.title("Virtual Assistant")
root.geometry("400x300")

username_label = tk.Label(root, text="Connection ID", font=('Helvetica bold', 20), pady=5)
username_label.pack()
username_entry = tk.Entry(root, font=("Ariel", 18), width=10)
username_entry.pack()

password_label = tk.Label(root, text="Password", font=('Helvetica bold', 20), pady=5)
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Ariel", 18), width=10)
password_entry.pack()


def check():
    if username_entry.get() == "813958" and password_entry.get() == "1234":
        wrong = tk.Label(root, text="Connecting...!", font=('Helvetica bold', 16), fg="green", pady=10)
        wrong.pack()
        root.destroy()
        import interface
    else:
        wrong = tk.Label(root, text="Wrong Connection ID or Password!", font=('Helvetica bold', 16), fg="red", pady=10)
        wrong.pack()


button = tk.Button(root, text="Connect", command=check, width=10, height=2)
button.pack()

root.mainloop()
