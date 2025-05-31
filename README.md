# 🧮 BMI Calculator


**Stanford - Code in Place 2025** - _Final Project by Wanda van den Hoogen_

---
A simple and responsive web application that allows users to calculate their Body Mass Index (BMI) based on their height and weight. The app provides instant feedback and interpretation of the result.

---

![ScreenshotBMI](https://github.com/user-attachments/assets/cdf42f7d-1ec1-4e2c-b72a-133aac8906f7)

---

🔗 **Live demo**: [bmi-calculator-vgwl.onrender.com](https://bmi-calculator-vgwl.onrender.com/) | _It's a free plan on render.com so it takes a few for the application to start._ 

- Enter your height and weight
- Get your BMI score and interpretation instantly
- Stylish and responsive interface
- Possibility to do a new calculation

---

## 🛠️ Techniques used

- **Python 3**
- **Flask** – for setting up the web server and routing
- **HTML5 & CSS3** – for the frontend
- **Google Fonts** – for typography
- **Render** – for hosting and deployment (render.com)
- **Web App Manifest** – for PWA (Progressive Web App) support

---

## 📁 Folder structure
```
bmi/
├── app.py
├── site.webmanifest
├── README.md
├── static/
│   ├── index.css
│   └── assets/
│       ├── android-chrome-192x192.png
│       ├── apple-touch-icon.png
│       ├── bmi.png
│       ├── favicon-16x16.png
│       ├── favicon-32x32.png
│       └── favicon.ico
└──  templates/
    ├── index.html
    └── result.html

```
---

## ![Badge displaying Python 3.10 in blue with white text, representing the programming language and version used in the project](https://img.shields.io/badge/Python-3.10-blue?) Python-code (app.py)

The application logic is written in Python using the Flask framework. The app.py contains routes for displaying the input form and processing the BMI calculation. Based on the entered height and weight, the BMI is calculated and an interpretation is displayed.

---

##  🧪 What is Flask?

Flask is a lightweight web framework for Python. It allows you to build web applications quickly and with minimal code. In this project, Flask is used to:

- Handle routing (e.g., showing the form and result pages)
- Process user input (height and weight)
- Render HTML templates with dynamic content (like the BMI result)

Flask is ideal for small to medium-sized projects due to its simplicity and flexibility.


---

![bmi](https://github.com/user-attachments/assets/38055079-2790-456f-9707-907786b7a2b8)

