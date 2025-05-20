from flask import Blueprint, render_template, request

# Define the blueprint before using it
main = Blueprint('main', __name__)

# This will store all the feedback entries
feedback_list = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        feedback = request.form.get('feedback')

        feedback_entry = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'feedback': feedback
        }
        feedback_list.append(feedback_entry)

    return render_template('index.html', feedbacks=feedback_list)
