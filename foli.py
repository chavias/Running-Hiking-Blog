data = {'Date': '28.09.2014', 'Race': '41. Berlin Marathon', 'Latitude': 52.51625499, 'Longitude': 13.37757535, 'Time': '4:17:35', 'Link': 'https://www.bmw-berlin-marathon.com/'}

import folium

run_map = folium.Map(location=[data['Latitude'], data['Longitude']], tiles=None, zoom_start=12)

# add Openstreetmap layer
folium.TileLayer('openstreetmap', name='OpenStreet Map').add_to(run_map)

fg_marathons = folium.FeatureGroup(name='Marathons').add_to(run_map)

# create marker and add it to marathon feature group
folium_marker = folium.Marker(location=[data['Latitude'], data['Longitude']], tooltip=data['Race'], icon=folium.Icon(color='red'))
folium_marker.add_to(fg_marathons)

# add legend in top right corner
run_map.add_child(folium.LayerControl(position='topright', collapsed=False, autoZIndex=True))


popup_html = f"<b>Date:</b> {data['Date']}<br/>"
popup_html += f"<b>Race:</b> {data['Race']}<br/>"
popup_html += f"<b>Time:</b> {data['Time']}<br/>"
popup_html += '<b><a href="{}" target="_blank">Event Page</a></b>'.format(data['Link'])
popup_iframe = folium.IFrame(width=200, height=110, html=popup_html)

# modify the marker object to display the pop-up
folium_marker = folium.Marker(location=[data['Latitude'], data['Longitude']], tooltip=data['Race'], popup=folium.Popup(popup_iframe), icon=folium.Icon(color='red'))
folium_marker.add_to(fg_marathons)



# parse gpx file
import gpxpy
gpx_file = '/home/mach/Downloads/glarus.gpx'
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

# add segments to the map
folium_gpx = folium.PolyLine(points, color='red', weight=5, opacity=0.85).add_to(run_map)

# add the gpx trace to our marathon group
folium_gpx.add_to(fg_marathons)



# save and open map
run_map.save('run_map.html')