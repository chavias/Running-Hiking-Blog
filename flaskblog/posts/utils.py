import os
import secrets
from flask import url_for, current_app
import gpxpy
import folium


def save_gpx(form_gpx):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_gpx.filename)
    gpx_fn =  random_hex + f_ext
    gpx_path = os.path.join(current_app.root_path,'static/route_gpx', gpx_fn)
    form_gpx.save(gpx_path)
    return gpx_fn


def create_map(gpx_fn):
    gpx_file = os.path.join(current_app.root_path,'static/route_gpx', gpx_fn)
    gpx = gpxpy.parse(open(gpx_file))
    track = gpx.tracks[0]
    segment = track.segments[0]
    # load coordinate points
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            step = 10
            for point in segment.points[::step]:
                points.append(tuple([point.latitude, point.longitude]))


    m = folium.Map(location=points[len(points)//2],zoom_start=20)
    # add segments to the map
    folium_gpx = folium.PolyLine(points, color='red', weight=5, opacity=0.85).add_to(m)
    
    return m._repr_html_()

def load_map(gpx_fn):
    gpx_file = os.path.join(current_app.root_path,'static/route_gpx', gpx_fn)
    gpx = gpxpy.parse(open(gpx_file))
    track = gpx.tracks[0]
    segment = track.segments[0]
    # load coordinate points
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            step = 10
            for point in segment.points[::step]:
                points.append(tuple([point.latitude, point.longitude]))


    m = folium.Map(location=points[len(points)//2],zoom_start=12)
    # add segments to the map
    folium_gpx = folium.PolyLine(points, color='red', weight=5, opacity=0.85).add_to(m)
    
    return m._repr_html_()