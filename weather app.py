
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(200, 200, 350, 250)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")

        self.search_button = QPushButton("Get Weather")
        self.result_label = QLabel("Enter a city to see its weather")

        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.search_button.clicked.connect(self.get_weather)



    def get_weather(self):
        city = self.city_input.text().strip()

        if not city:
            self.result_label.setText("Please enter a city name.")
            return

        api_key = "0178ad425f0a0e118b133d871fd9c34c"

        url = "https://api.openweathermap.org/data/2.5/weather"

        try:
            response = requests.get(
                url,
                params={
                    "q": city,
                    "appid": api_key,
                    "units": "metric"
                },
                timeout=10
            )

            data = response.json()

            if response.status_code == 200:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]

                self.result_label.setText(
                    f"{city}: {temperature}°C, {description}"
                )
            else:
                self.result_label.setText(data.get("message", "Weather not found"))

        except requests.RequestException:
            self.result_label.setText("Connection error. Please try again.")



app = QApplication(sys.argv)
window = WeatherApp()
window.show()
sys.exit(app.exec_())


