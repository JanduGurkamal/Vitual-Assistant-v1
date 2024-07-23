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


def run():
    import sys
    import requests
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFrame, \
        QWidget, \
        QStackedWidget, QLineEdit, QTextEdit, QComboBox, QDateEdit, QTimeEdit, QListWidget, QInputDialog
    from PyQt5.QtGui import QFont
    from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QDate, QTime

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Futuristic Virtual Assistant")
            self.setGeometry(100, 100, 1024, 768)
            self.setStyleSheet("background-color: #0b0c10; color: #c5c6c7;")

            # Central widget
            central_widget = QWidget(self)
            self.setCentralWidget(central_widget)

            # Main layout
            main_layout = QHBoxLayout(central_widget)

            # Side panel
            side_panel = QFrame(self)
            side_panel.setFixedWidth(200)
            side_panel.setStyleSheet("background-color: #1f2833;")
            side_layout = QVBoxLayout(side_panel)

            # Add user profile section
            profile_label = QLabel("User Profile", self)
            profile_label.setAlignment(Qt.AlignCenter)
            profile_label.setFont(QFont("Open Sans", 14))
            profile_label.setStyleSheet("color: #c5c6c7;")
            side_layout.addWidget(profile_label)

            # Add buttons to side panel
            button1 = QPushButton("Settings", self)
            button1.setFont(QFont("Roboto", 12))
            button1.setStyleSheet("background-color: #1f2833; color: #66fcf1; border: none; padding: 10px;")
            button1.setCursor(Qt.PointingHandCursor)
            button1.clicked.connect(self.show_settings)
            side_layout.addWidget(button1)

            button2 = QPushButton("Logs", self)
            button2.setFont(QFont("Roboto", 12))
            button2.setStyleSheet("background-color: #1f2833; color: #66fcf1; border: none; padding: 10px;")
            button2.setCursor(Qt.PointingHandCursor)
            button2.clicked.connect(self.show_logs)
            side_layout.addWidget(button2)

            button3 = QPushButton("Home", self)
            button3.setFont(QFont("Roboto", 12))
            button3.setStyleSheet("background-color: #1f2833; color: #66fcf1; border: none; padding: 10px;")
            button3.setCursor(Qt.PointingHandCursor)
            button3.clicked.connect(self.show_home)
            side_layout.addWidget(button3)

            # Main content area with QStackedWidget
            self.stack = QStackedWidget(self)
            self.home_widget = QWidget(self)
            self.settings_widget = QWidget(self)
            self.logs_widget = QWidget(self)

            self.stack.addWidget(self.home_widget)
            self.stack.addWidget(self.settings_widget)
            self.stack.addWidget(self.logs_widget)

            # Set up home screen
            home_layout = QVBoxLayout(self.home_widget)
            self.weather_label = QLabel("Weather Widget", self)
            self.weather_label.setAlignment(Qt.AlignCenter)
            self.weather_label.setFont(QFont("Open Sans", 14))
            self.weather_label.setStyleSheet("color: #c5c6c7;")
            home_layout.addWidget(self.weather_label)

            self.calendar_label = QLabel("Calendar Widget", self)
            self.calendar_label.setAlignment(Qt.AlignCenter)
            self.calendar_label.setFont(QFont("Open Sans", 14))
            self.calendar_label.setStyleSheet("color: #c5c6c7;")
            home_layout.addWidget(self.calendar_label)

            self.smart_device_label = QLabel("Smart Device Control", self)
            self.smart_device_label.setAlignment(Qt.AlignCenter)
            self.smart_device_label.setFont(QFont("Open Sans", 14))
            self.smart_device_label.setStyleSheet("color: #c5c6c7;")
            home_layout.addWidget(self.smart_device_label)

            # Add smart device control buttons
            smart_device_layout = QHBoxLayout()
            light_button = QPushButton("Toggle Light", self)
            light_button.setFont(QFont("Roboto", 12))
            light_button.setStyleSheet("background-color: #45a29e; color: #0b0c10; border: none; padding: 10px;")
            light_button.setCursor(Qt.PointingHandCursor)
            light_button.clicked.connect(self.toggle_light)
            smart_device_layout.addWidget(light_button)

            fan_button = QPushButton("Toggle Fan", self)
            fan_button.setFont(QFont("Roboto", 12))
            fan_button.setStyleSheet("background-color: #45a29e; color: #0b0c10; border: none; padding: 10px;")
            fan_button.setCursor(Qt.PointingHandCursor)
            fan_button.clicked.connect(self.toggle_fan)
            smart_device_layout.addWidget(fan_button)

            home_layout.addLayout(smart_device_layout)

            # Add calendar events section
            add_event_button = QPushButton("Add Event", self)
            add_event_button.setFont(QFont("Roboto", 12))
            add_event_button.setStyleSheet("background-color: #45a29e; color: #0b0c10; border: none; padding: 10px;")
            add_event_button.setCursor(Qt.PointingHandCursor)
            add_event_button.clicked.connect(self.add_event)
            home_layout.addWidget(add_event_button)

            self.events_list = QListWidget(self)
            self.events_list.setFont(QFont("Open Sans", 12))
            self.events_list.setStyleSheet("color: #0b0c10; background-color: #c5c6c7; padding: 5px;")
            home_layout.addWidget(self.events_list)

            # Set up settings screen
            settings_layout = QVBoxLayout(self.settings_widget)
            settings_label = QLabel("Settings", self)
            settings_label.setAlignment(Qt.AlignCenter)
            settings_label.setFont(QFont("Open Sans", 14))
            settings_label.setStyleSheet("color: #c5c6c7;")
            settings_layout.addWidget(settings_label)

            api_key_label = QLabel("Weather API Key:", self)
            api_key_label.setFont(QFont("Open Sans", 12))
            api_key_label.setStyleSheet("color: #c5c6c7;")
            settings_layout.addWidget(api_key_label)

            self.api_key_input = QLineEdit(self)
            self.api_key_input.setFont(QFont("Open Sans", 12))
            self.api_key_input.setStyleSheet("color: #0b0c10; background-color: #c5c6c7; padding: 5px;")
            settings_layout.addWidget(self.api_key_input)

            save_button = QPushButton("Save", self)
            save_button.setFont(QFont("Roboto", 12))
            save_button.setStyleSheet("background-color: #45a29e; color: #0b0c10; border: none; padding: 10px;")
            save_button.setCursor(Qt.PointingHandCursor)
            save_button.clicked.connect(self.save_settings)
            settings_layout.addWidget(save_button)

            # Set up logs screen
            logs_layout = QVBoxLayout(self.logs_widget)
            logs_label = QLabel("Logs", self)
            logs_label.setAlignment(Qt.AlignCenter)
            logs_label.setFont(QFont("Open Sans", 14))
            logs_label.setStyleSheet("color: #c5c6c7;")
            logs_layout.addWidget(logs_label)

            self.logs_text = QTextEdit(self)
            self.logs_text.setFont(QFont("Open Sans", 12))
            self.logs_text.setStyleSheet("color: #0b0c10; background-color: #c5c6c7; padding: 5px;")
            logs_layout.addWidget(self.logs_text)

            # Add bottom bar
            bottom_bar = QFrame(self)
            bottom_bar.setFixedHeight(50)
            bottom_bar.setStyleSheet("background-color: #1f2833;")
            bottom_layout = QVBoxLayout(bottom_bar)

            self.voice_command_label = QLabel("Voice Command Input", self)
            self.voice_command_label.setAlignment(Qt.AlignCenter)
            self.voice_command_label.setFont(QFont("Open Sans", 12))
            self.voice_command_label.setStyleSheet("color: #c5c6c7;")
            bottom_layout.addWidget(self.voice_command_label)

            # Add layouts to main layout
            main_layout.addWidget(side_panel)
            main_layout.addWidget(self.stack)
            main_layout.addWidget(bottom_bar, alignment=Qt.AlignBottom)

            # Setup timer for weather updates
            self.setup_timer()

        def show_settings(self):
            self.stack.setCurrentWidget(self.settings_widget)

        def show_logs(self):
            self.stack.setCurrentWidget(self.logs_widget)

        def show_home(self):
            self.stack.setCurrentWidget(self.home_widget)

        def update_weather(self):
            try:
                api_key = self.api_key_input.text()
                response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}')
                weather_data = response.json()
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
                self.weather_label.setText(f"Weather: {weather_description}, Temp: {temperature:.2f}°C")
            except Exception as e:
                self.weather_label.setText("Weather update failed")
                self.logs_text.append(f"Error: {e}")
                print(e)

        def setup_timer(self):
            timer = QTimer(self)
            timer.timeout.connect(self.update_weather)
            timer.start(60000)  # Update every 60 seconds
            self.update_weather()  # Initial call to display weather immediately

        def save_settings(self):
            api_key = self.api_key_input.text()
            self.logs_text.append(f"Saved API Key: {api_key}")
            # Optionally, save to a file or a more secure storage
            self.show_home()

        def fade_in(self, widget):
            animation = QPropertyAnimation(widget, b"windowOpacity")
            animation.setDuration(1000)
            animation.setStartValue(0)
            animation.setEndValue(1)
            animation.start()

        def toggle_light(self):
            self.logs_text.append("Light toggled")

        def toggle_fan(self):
            self.logs_text.append("Fan toggled")

        def add_event(self):
            event_name, ok = QInputDialog.getText(self, "Add Event", "Event Name:")
            if ok and event_name:
                event_date = QDateEdit(self)
                event_date.setCalendarPopup(True)
                event_date.setDate(QDate.currentDate())
                event_date.dateChanged.connect(lambda date: self.logs_text.append(f"Event Date: {date.toString()}"))

                event_time = QTimeEdit(self)
                event_time.setTime(QTime.currentTime())
                event_time.timeChanged.connect(lambda time: self.logs_text.append(f"Event Time: {time.toString()}"))

                self.events_list.addItem(
                    f"{event_name} on {event_date.date().toString()} at {event_time.time().toString()}")

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())


def check():
    if username_entry.get() == "813958" and password_entry.get() == "1234":
        wrong = tk.Label(root, text="Connecting...!", font=('Helvetica bold', 16), fg="green", pady=10)
        wrong.pack()
        root.destroy()
        run()
    else:
        wrong = tk.Label(root, text="Wrong Connection ID or Password!", font=('Helvetica bold', 16), fg="red", pady=10)
        wrong.pack()




button = tk.Button(root, text="Connect", command=check, width=10, height=2)
button.pack()

root.mainloop()
