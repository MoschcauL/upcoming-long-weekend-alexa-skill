import sys
import os
import datetime

# change directory
sys.path.append(os.path.dirname(os.getcwd()))
os.chdir(os.path.dirname(os.getcwd()))

import constants as c
import utils as u


def main():
    raw_json_fp = os.path.join(c.RESOURCE_DIRECTORY, c.RAW_OUTPUT_JSON)
    final_json_fp = os.path.join(c.RESOURCE_DIRECTORY, c.FINAL_OUTPUT_JSON)

    holiday_input = u.load_json(raw_json_fp)
    holiday_output = []

    for obj in holiday_input:
        if obj['day'] in c.ACCEPTABLE_DAYS:
            dt = datetime.datetime.strptime(obj['date'], '%b %d')
            output_obj = {
                'type': obj['type'],
                'month': dt.strftime('%B'),
                'date': int(dt.strftime('%d')),
                'day': obj['day'],
                'name': obj['name'],
                'number_of_days': 3
            }
            holiday_output.append(output_obj)

    u.store_json(final_json_fp, holiday_output)


if __name__ == '__main__':
    main()
