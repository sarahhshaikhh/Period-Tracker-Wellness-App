from flask import Flask, render_template

app = Flask(__name__)

@app.route('/expert_advice')
def expert_advice():
    return render_template('expert_advice.html')

if __name__ == '__main__':
    app.run(debug=True)
