from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def welcome():
    msg = render_template('welcome')
    session.attributes['counter'] = 0
    return question(msg)


@ask.intent("HolidayIntent")
def holiday():
    holiday_type = "National"
    month = "January"
    date = "26"
    day = "Friday"
    number_of_days = 3

    holiday_message = render_template('holiday', holiday_type=holiday_type, month=month, date=date, day=day, number_of_days=number_of_days)
    session.attributes['counter'] += 1

    if session.attributes['counter'] == 1:
        msg = render_template('first') + holiday_message + " " + render_template('next')
    else:
        msg = render_template('subsequent') + holiday_message + " " + render_template('next')
    
    return question(msg)


@ask.intent("ThankYouIntent")
def thank_you():
    msg = render_template('finish')
    return statement(msg)


@ask.intent("AMAZON.StopIntent")
def thank_you():
    msg = render_template('finish')
    return statement(msg)


@ask.intent("AMAZON.CancelIntent")
def thank_you():
    msg = render_template('finish')
    return statement(msg)
    

@ask.intent("AMAZON.HelpIntent")
def handle_help():
    help_text = render_template('help_text')
    return question(help_text)


@ask.session_ended
def session_ended():
    """
    Returns an empty for `session_ended`.
    """
    return statement("")

if __name__ == '__main__':
    app.run(debug=True)
