import os
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

import utils as u
import constants as c

app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def welcome():
    msg = render_template('welcome')
    session.attributes['counter'] = 0
    return question(msg)


@ask.intent("HolidayIntent")
def holiday():
    holiday_fp = os.path.join(c.RESOURCE_DIRECTORY, c.FINAL_OUTPUT_JSON)
    holidays_data = u.load_json(holiday_fp)
    if 'counter' in session.attributes:
        holiday_ctr = session.attributes['counter']
    else:
        session.attributes['counter'] = 0
        holiday_ctr = 0

    if holiday_ctr >= len(holidays_data):
        return statement(render_template('complete'))

    holiday_obj = holidays_data[holiday_ctr]

    session.attributes['counter'] += 1
    holiday_message = render_template('holiday', holiday_obj=holiday_obj)
    if session.attributes['counter'] == 1:
        msg = render_template('first') + holiday_message + " " + \
              render_template('next')
    else:
        msg = render_template('subsequent') + holiday_message + " " + \
              render_template('next')

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
    return statement("")


if __name__ == '__main__':
    app.run(debug=True)
