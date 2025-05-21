from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

feedbacks = []

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        feedback = request.form.get('feedback')

        # Save feedback
        feedback_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'feedback': feedback
        }

        feedbacks.append(feedback_data)

    return render_template('index.html', feedbacks=feedbacks)
