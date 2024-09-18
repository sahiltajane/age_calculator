Age Calculator Web Application
This is a Python-based web application that calculates a user's exact age (in years, months, days, hours, minutes, and seconds) and predicts the day of their next birthday. It allows users to input their name, email, and birthdate. Each submission generates a new file that saves the calculated details, including the user's name and the timestamp of the submission.

Features
User input for name, email, and birthdate.
Calculates the user's exact age (years, months, days, hours, minutes, seconds).
Predicts the day of the next birthday.
Saves submission data to a file with the user's name and a timestamp in the filename.
Creates a new file for each submission in the data/ folder.
Project Structure
bash
Copy code
age_calculator/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML form
├── data/                  # Folder for storing user submission files
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
Requirements
Python 3.x
Flask (Python web framework)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/sahiltajane/age-calculator.git
cd age_calculator
Install dependencies:

First, create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Then install Flask using pip:

bash
Copy code
pip install Flask
Run the Flask app:

Start the application by running the app.py file:

bash
Copy code
python app.py
Open the app in your browser:

Navigate to http://127.0.0.1:5000/ in your browser.

Usage
Fill out the form by entering your name, email, and birthdate.
Click the "Calculate Age" button.
The app will display your exact age and the day of your next birthday.
A file will be created in the data/ folder containing the details of the submission. The file will be named using your name and the current timestamp, e.g., JohnDoe_20240918_123456.txt.
Example
A user named John Doe enters their birthdate as 1990-01-01. The app calculates their exact age and predicts their next birthday. The data is saved in a file named JohnDoe_20240918_123456.txt (where the numbers represent the timestamp of the submission).

File Content:

vbnet
Copy code
Name: John Doe
Email: johndoe@example.com
Your age is: 34 years, 8 months, 17 days, 12 hours, 30 minutes, and 45 seconds.
Your next birthday will be on: Monday, 2025-01-01.
Future Improvements
Add validation for name and email fields.
Improve the design of the frontend form.
Store data in a database instead of text files.
License
This project is open source and available under the MIT License.
