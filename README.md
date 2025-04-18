# 🌸 Bloom Period Tracker - Menstrual Tracker Web App 🌸
Bloom Period Tracker
Bloom Period Tracker is a web-based platform designed to empower women with tools for tracking their menstrual cycles, setting wellness goals, and accessing educational resources. This platform offers a comprehensive approach to women’s health with features that include expert advice scheduling, community support, and personalized progress tracking.

# Key Features
1. Educational Videos on Menstrual Health
A Tutorial Section filled with educational videos on menstrual health, aimed at providing crucial information on cycle tracking, hormonal health, and general wellness.

2. Expert Advice Scheduling
Flexible Appointment Booking: Seamlessly schedule consultations with healthcare professionals to get personalized advice on menstrual and reproductive health.

3. Community Support
A Safe Space for women to share experiences, ask questions, and offer advice. This feature promotes a positive, supportive environment, with all interactions moderated for privacy and safety.

4. Goal-Setting and Tracking
Personalized Goals: Set mood, calorie, and exercise goals to align with your wellness objectives. Track your progress and stay motivated with personalized insights and reports.

5. Insights Dashboard
An Interactive Dashboard that displays a summary of your health data, tracking progress over time. The dashboard includes key metrics like mood, physical activity, and overall health, helping users stay motivated and on track.

# Frontend Overview
The user interface is designed to be intuitive and easy to navigate. Developed using HTML and CSS, the frontend provides:

- Pop-Up Modals: For scheduling appointments and engaging with community support.

- Interactive Forms: For goal-setting, logging entries, and tracking personal progress.

- Insights Dashboard: A motivating visual summary of your wellness journey, showing data trends and achievements.

# Technologies Used:
HTML: Structure and content of the web pages.

CSS: Styling to ensure the platform is visually appealing and user-friendly.

# Backend Overview
The Flask framework is utilized for backend management, handling data processing, session management, and ensuring smooth integration between frontend and backend. Core functionalities include:

- Data Processing: Storing and managing user entries and wellness goals.

- Appointment Scheduling: Safely managing user preferences for consultations with healthcare professionals.

- Community Features: Allowing users to interact, share, and support one another in a secure environment.

- Insights Calculation: Aggregating user data to provide personalized summaries and actionable insights.

# Technologies Used:
Flask: Web framework for managing routing, requests, and backend logic.

Python: For server-side scripting and logic.

SQL/Database: Secure storage of user data, logs, and preferences.

# Data Management and Security
User data is handled with care, ensuring privacy and security at all stages. The following data is securely stored:

- User Data: Personal preferences, goal entries, and tracking logs.

- Scheduling Information: Appointment preferences and schedules for healthcare consultations.

- Community Interactions: All user-generated content in the community section is stored and moderated.

Security Features:

- Data encryption and secure storage for all sensitive information, including health data.

- Robust authentication and session management to ensure privacy and security for each user.

# Installation & Setup
To get started with Bloom Period Tracker locally, follow the instructions below:

1. Clone the Repository:
bash
Copy
Edit
git clone https://github.com/your-username/bloom-period-tracker.git
2. Install Dependencies:
Make sure you have Python 3.8+ installed. Then, run:

bash
Copy
Edit
pip install -r requirements.txt
3. Set up the Database:
Configure your database (use SQLite for simplicity during development, or another database for production).

Run the migration scripts if necessary to set up tables.

4. Run the Application:
bash
Copy
Edit
python app.py
The application should now be running locally at http://localhost:5000.

