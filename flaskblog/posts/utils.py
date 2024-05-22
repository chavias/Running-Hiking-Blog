import os
import secrets
from flask import url_for, current_app, send_from_directory, flash
import gpxpy
import folium
from folium.plugins import Fullscreen, Geocoder, Draw


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


    m = folium.Map(tiles='cartodbpositron',location=points[len(points)//2],zoom_start=16)

    # add marker 
    folium.Marker(points[0], popup="Start").add_to(m)
    folium.Marker(points[len(points)-1], popup="End").add_to(m)
    

    # add fullscreen button
    folium.plugins.Fullscreen(
        position="bottomright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m)

    # add geocoder 
    folium.plugins.Geocoder().add_to(m)

    # add Draw
    Draw(export=True).add_to(m)

    # add segments to the map
    folium_gpx = folium.PolyLine(points, color='red', weight=5, opacity=0.85).add_to(m)
    
    return m._repr_html_()
