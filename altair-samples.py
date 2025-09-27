import altair as alt
from vega_datasets import data
import pandas as pd

# Set up the renderer properly for your environment
# For Jupyter notebooks
# alt.renderers.enable('notebook')
# For standalone HTML files
alt.renderers.enable('html')
# For VS Code
# alt.renderers.enable('mimetype')

# Load the dataset
source = data.cars()

# Create the chart
chart = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

# Save the chart to an HTML file that you can open in your browser
chart.save('index.html')

print("Visualization saved to 'altair_visualization.html'. Open this file in your browser to view the chart.")

# If you want to display the chart directly in a Python environment that supports it:
# display(chart)