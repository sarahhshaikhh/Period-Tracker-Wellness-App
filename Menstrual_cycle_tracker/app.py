from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from tutorial import tutorial_bp  # Import the tutorial blueprint

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'menstrual_tracker'
app.secret_key = '123'  # Required for session management

mysql = MySQL(app)

# Home Route (Redirect to login)
@app.route('/')
def home():
    return redirect(url_for('login'))

# Route for Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
            mysql.connection.commit()
            cursor.close()

            flash('Registration Successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username already exists. Please choose a different one.', 'danger')
            return render_template('register.html')  # Show the registration form again

    return render_template('register.html')

# Route for Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password):  # Assuming password is at index 2
            session['loggedin'] = True
            session['username'] = user[1]  # Assuming username is at index 1
            return redirect(url_for('home_page'))  # Redirect to home_page

        flash('Incorrect username or password!', 'danger')

    return render_template('login.html')


# Home Route (After Login)
@app.route('/home')
def home_page():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])  # Render home.html
    return redirect(url_for('login'))

@app.route('/support')
def support():
    return render_template('support.html')

# Route for Expert Advice
@app.route('/expert_advice')
def expert_advice():
    return render_template('expert_advice.html')

# Route for Set Goals
@app.route('/set_goal', methods=['GET', 'POST'])
def set_goals():
    if request.method == 'POST':
        # Extract goals from the form
        mood_goal = request.form['moodGoal']
        nutrition_goal = request.form['nutritionGoal']
        exercise_goal = request.form['exerciseGoal']

        # Here, you can save these goals to your database if needed

        flash('Goals saved successfully!', 'success')
        return redirect(url_for('insights'))  # Redirect to insights or any other page you want
    
    return render_template('set_goal.html')

# Route for Insights
@app.route('/insights')
def insights():
    return render_template('insights.html')

# Register the tutorial blueprint
app.register_blueprint(tutorial_bp)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('You have been logged out!', 'success')
    return redirect(url_for('login'))

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    mood_data = request.form['mood']
    # Process mood data (e.g., save to database)
    return redirect('/mood')

@app.route('/submit_nutrition', methods=['POST'])
def submit_nutrition():
    food_data = request.form.get('food')  # Use get() to avoid KeyErrors
    # Process food_data (e.g., save to database)
    return redirect(url_for('nutrition'))


@app.route('/submit_exercise', methods=['POST'])
def submit_exercise():
    exercise_data = request.form['exercise']
    # Process exercise data (e.g., save to database)
    return redirect('/exercise')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
