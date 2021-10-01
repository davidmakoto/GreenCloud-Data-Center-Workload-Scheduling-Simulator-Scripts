# Very simple script that takes in a trace file (hard coded for now) and plots using plotly.express into "images" folder
# Note: the trace files currently don't have labels so it's important to identify that ahead of time and manually change axis titles here


import pandas as pd
import plotly.express as px
import os

df = pd.read_csv('/serverLoadTrace/Green_3tier_dcServLoad.tr', delim_whitespace = True)
fig = px.line(df, x = 'server_count', y = 'server_load', title='Server Load vs Server Count Green Scheduler ')
# df = pd.read_csv('dcServLoad.tr', delim_whitespace = True)
# fig = px.line(df, title='Server Load vs Server Count')

fig.show()
if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/fig1.png")