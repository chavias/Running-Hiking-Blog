import os
import secrets
from flask import url_for, current_app


def save_gpx(form_gpx):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_gpx.filename)
    gpx_fn =  random_hex + f_ext
    gpx_path = os.path.join(current_app.root_path,'static/route_gpx', gpx_fn)
    form_gpx.save(gpx_path)
    return gpx_fn