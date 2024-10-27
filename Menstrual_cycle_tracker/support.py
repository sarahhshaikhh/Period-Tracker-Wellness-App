from flask import Flask, render_template

app = Flask(__name__)

@app.route('/support')
def expert_advice():
    return render_template('support.html')

if __name__ == '__main__':
    app.run(debug=True)
