This project is a simple Pwnagotchi GUI application that loads and displays Pwnagotchi screen

## ⚙️ Features
- Load and display images in a PyQt5 window
- Catch and display errors with custom font styling
- Easily tweak font size, color, and background using either `QFont` or stylesheets

## 🧠 How It Works
- it connects to the pwnagotchi IP:PORT then calculates the timestamp and generate a url for the current image and display it, it if cant connect to the given IP:PORT it will give a connectivity error

## 📦 Requirments
- Python 3.x
- PyQt5
- yaml

Install dependencies:
`pip install PyQt5`
`pip install yaml`

## 🚀 Running the App
in the `config.yaml` set your ip and port
then run the command `python main.py`

## 📸 Screenshot
<img width="722" height="482" alt="image" src="https://github.com/user-attachments/assets/aa628d03-26fe-44e3-b050-fd79005eacdb" />


