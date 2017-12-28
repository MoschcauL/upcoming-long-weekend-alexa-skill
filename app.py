import json
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

HOLIDAY_JSON_PATH = "res/2018.json"


def _load_json(fp):
    with open(fp) as data_file:
        return json.load(data_file)


@ask.launch
def welcome():
    msg = render_template('welcome')
    session.attributes['counter'] = 0
    return question(msg)


@ask.intent("HolidayIntent")
def holiday():
    holidays_data = _load_json(HOLIDAY_JSON_PATH)
    if 'counter' in session.attributes:
        holiday_ctr = session.attributes['counter']
    else:
        session.attributes['counter'] = 0
        holiday_ctr = 0

    if holiday_ctr >= len(holidays_data):
        return statement(render_template('complete'))

    holiday_type = holidays_data[holiday_ctr]['type']
    month = holidays_data[holiday_ctr]['month']
    date = holidays_data[holiday_ctr]['date']
    day = holidays_data[holiday_ctr]['day']
    number_of_days = holidays_data[holiday_ctr]['number_of_days']

    holiday_message = render_template('holiday', holiday_type=holiday_type, month=month, date=date, day=day,
                                      number_of_days=number_of_days)
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
