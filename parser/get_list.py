import sys
import os
import math
from bs4 import BeautifulSoup

# change directory
sys.path.append(os.path.dirname(os.getcwd()))
os.chdir(os.path.dirname(os.getcwd()))

import constants as c
import utils as u


def main():
    raw_output = []
    html = u.load_url(c.HOLIDAYS_URL)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        cells = soup.findAll(['th', 'td'])
        row_len = int(math.ceil(len(cells) / 4))
        for ctr in xrange(0, row_len):
            # skip headers
            if ctr == 0:
                continue

            offset = ctr * 4
            holiday_type = cells[offset + 3].text.split()
            if holiday_type[0] in c.IGNORE_HOLIDAY_TYPES:
                raw_output_obj = {
                    'date': cells[offset + 0].text.strip(),
                    'day': cells[offset + 1].text.strip(),
                    'name': cells[offset + 2].text.strip(),
                    'type': holiday_type[0]
                }
                raw_output.append(raw_output_obj)
            else:
                print holiday_type

    output_fp = os.path.join(c.RESOURCE_DIRECTORY, c.RAW_OUTPUT_JSON)
    u.store_json(output_fp, raw_output)


if __name__ == '__main__':
    main()
