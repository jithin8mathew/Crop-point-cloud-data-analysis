#!/usr/bin/env python
# coding: utf-8

import numpy as np
from laspy.file import File
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

inFile = File("./wheat3000.las", mode = "r")

point_records = inFile.points
print(point_records)

pointformat = inFile.point_format

for spec in inFile.point_format:
    print(spec.name)


x,y,z = inFile.X , inFile.Y , inFile.Z

print(len(y), len(x), len(z))

noise = np.concatenate((np.where(y<= -370)[0], np.where(y>= 1100)[0], np.where(x>2510)[0]), axis=None)

print(len(x),len(y),len(z))

x1,y1,z1 = np.delete(x, noise) , np.delete(y, noise), np.delete(z, noise)
print(len(y1), len(x1), len(z1))

fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z, mode='markers', marker=dict( size=0.4, color=x, opacity=0.8)
)])

fig.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
fig.show()

##################################
fig = go.Figure(data=[go.Scatter3d(
    x=x1, y=y1, z=z1, mode='markers', marker=dict( size=0.4, color=x, opacity=0.8)
)])

fig.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
fig.show()

lidar_Maxpoint = np.max(x1)
lidar_Maxpoint

x1= lidar_Maxpoint - x1

fig = go.Figure(data=[go.Scatter3d(
    x=x1, y=y1, z=z1, mode='markers', marker=dict( size=0.5, color=x, opacity=0.8)
)])

fig.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
fig.show()

header_len = inFile.header.data_record_length
scl= inFile.header.scale
prc= inFile.header.point_return_count
rc= inFile.header.records_count
dfi= inFile.header.data_format_id
do= inFile.header.data_offset
hs= inFile.header.header_size
v= inFile.header.version
gui= inFile.header.guid
gps= inFile.header.gps_time_type


print(header_len)
print(scl)
print(prc)
print(rc)
print(dfi)
print(do)
print(hs)
print(v)
print(gui)
print(gps)

x1 = [lidar_Maxpoint - i for i in list(x1)]
x1 = np.array(x1)


fig = go.Figure(data=[go.Scatter3d(
    x=x1, y=y1, z=z1, mode='markers', marker=dict( size=0.5, color=x, opacity=0.8)
)])

fig.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
fig.show()


inFile = File("./calibration4.las", mode = "r")
point_records = inFile.points
x,y,z = inFile.X , inFile.Y , inFile.Z


noise = np.concatenate((np.where(y<= -730)[0], np.where(y>= 1400)[0], np.where(x>2510)[0]), axis=None)
noise

x1,y1,z1 = np.delete(x, noise) , np.delete(y, noise), np.delete(z, noise)
print(len(y1), len(x1), len(z1))

lidar_Maxpoint = np.max(x1)
x1= lidar_Maxpoint - x1
lidar_Maxpoint


x1 = x1/ 25

fig = go.Figure(data=[go.Scatter3d(
    x=x1, y=y1, z=z1, mode='markers', marker=dict( size=0.4, color=x, opacity=0.8)
)])

fig.update_layout(template='plotly_dark', margin=dict(l=0, r=0, b=0, t=0))
fig.show()



