import json
import requests


def store_json(fp, obj, beautify_mode=True):
    with open(fp, 'wb+') as f:
        if beautify_mode:
            json.dump(obj, f, sort_keys=True, indent=4)
        else:
            json.dump(obj, f)


def load_json(fp):
    with open(fp, 'rb') as f:
        return json.load(f)


def load_url(url):
    try:
        r = requests.get(url)
        if r.ok:
            return r.text
        else:
            return None
    except Exception:
        return None
