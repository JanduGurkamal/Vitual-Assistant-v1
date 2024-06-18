
import ibackend

class VirtualAssistant(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Virtual Assistant")
        self.geometry("800x500")
        self.resizable(False, False)

        # Create a label for the virtual assistant's name
        name_label = tk.CTkLabel(self, text="VEGA", font=("", 20))
        name_label.pack(pady=10)

        # Create a text box for user input
        self.logs = tk2.Text(self, width=100, height=10)
        self.logs.pack(pady=10)

        # Create a button to trigger the virtual assistant's response
        response_button = tk.CTkButton(self, text="Ask", font=("Arial", 12), command=ibackend.wake_up)
        response_button.pack(pady=10)


    def respond(self):

        # Display the response in the text box
        self.logs.insert(tk2.END, "You:" + ibackend.command + "\n")

# Run the application
app = VirtualAssistant()
app.mainloop()