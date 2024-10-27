from flask import Blueprint, render_template

# Define the blueprint
tutorial_bp = Blueprint('tutorial_bp', __name__, url_prefix='/tutorial')

# Tutorial route
@tutorial_bp.route('/')
def tutorial():
    return render_template('tutorial.html')


if __name__ == '__main__':
    app.run(debug=True)
