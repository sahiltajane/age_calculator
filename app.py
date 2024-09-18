import os
from datetime import datetime
from flask import Flask, render_template, request

# Flask app initialization
app = Flask(__name__)

# Ensure the data folder exists
if not os.path.exists("data"):
    os.makedirs("data")

# Function to calculate exact age
def calculate_exact_age(birthdate):
    now = datetime.now()
    time_difference = now - birthdate

    total_seconds = time_difference.total_seconds()
    years = total_seconds // (365.25 * 24 * 3600)
    remaining_seconds = total_seconds % (365.25 * 24 * 3600)
    months = remaining_seconds // (30 * 24 * 3600)  # Approximate month calculation
    remaining_seconds %= (30 * 24 * 3600)
    days = remaining_seconds // (24 * 3600)
    remaining_seconds %= (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return int(years), int(months), int(days), int(hours), int(minutes), int(seconds)

# Function to predict the day of the next birthday
def predict_next_birthday(birthdate):
    now = datetime.now()
    this_year_birthday = birthdate.replace(year=now.year)
    
    if this_year_birthday < now:
        next_birthday = this_year_birthday.replace(year=now.year + 1)
    else:
        next_birthday = this_year_birthday

    return next_birthday.strftime("%A"), next_birthday

# Function to sanitize the filename (remove special characters from name)
def sanitize_filename(name):
    return "".join(c for c in name if c.isalnum() or c in (' ', '_')).rstrip()

# Function to save data to a new file
def save_to_new_file(name, data):
    # Use the sanitized name and timestamp to create a unique filename
    sanitized_name = sanitize_filename(name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{sanitized_name}_{timestamp}.txt"
    file_path = os.path.join("data", file_name)
    
    with open(file_path, "w") as file:
        file.write(data)
    
    print(f"Data saved to {file_path}")

# Route to render the HTML form and display results
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        birth_date_input = request.form['birthdate']

        try:
            # Convert input to a datetime object
            birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

            # Calculate exact age
            years, months, days, hours, minutes, seconds = calculate_exact_age(birth_date)
            age_info = (f"Name: {name}\nEmail: {email}\nYour age is: {years} years, {months} months, "
                        f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

            # Predict the day of the next birthday
            next_birthday_day, next_birthday_date = predict_next_birthday(birth_date)
            birthday_info = (f"Your next birthday will be on: {next_birthday_day}, "
                             f"{next_birthday_date.strftime('%Y-%m-%d')}.")

            # Combine all information
            full_info = f"{age_info}\n{birthday_info}"

            # Save data to a new file in the "data" folder, with the user's name in the filename
            save_to_new_file(name, full_info)

            return render_template('index.html', age_info=age_info, birthday_info=birthday_info)

        except ValueError:
            return render_template('index.html', error="Invalid date format. Please use YYYY-MM-DD.")
    
    return render_template('index.html')

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
