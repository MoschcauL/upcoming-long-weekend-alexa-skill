import json
import requests
import math
from bs4 import BeautifulSoup


def load_url(url):
    try:
        r = requests.get(url)
        if r.ok:
            return r.text
        else:
            return None
    except Exception:
        return None


def store_json_response(fp, obj, beautify_mode=True):
    with open(fp, 'w+') as f:
        if beautify_mode:
            json.dump(obj, f, sort_keys=True, indent=4)
        else:
            json.dump(obj, f)


def main():
    output_fp = "../res/2018.raw.json"
    public_url = 'https://www.timeanddate.com/holidays/india/2018'
    html = load_url(public_url)
    raw_output = []
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
            if holiday_type[0] in ["Restricted", 'Gazetted']:
                raw_output_obj = {
                    'date': cells[offset + 0].text.strip(),
                    'day': cells[offset + 1].text.strip(),
                    'name': cells[offset + 2].text.strip(),
                    'type': holiday_type[0]
                }
                raw_output.append(raw_output_obj)
            else:
                print holiday_type

    store_json_response(output_fp, raw_output)


if __name__ == '__main__':
    main()
