from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

feedback_list = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feedback = request.form['feedback']
        feedback_list.append(feedback)
    return render_template('index.html', feedbacks=feedback_list)
