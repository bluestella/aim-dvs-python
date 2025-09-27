# Altair Setup Guide

This guide will help you set up Altair for data visualization on your local machine.

## Installation

First, install Altair and its dependencies:

```bash
pip install altair vega_datasets pandas
```

For saving visualizations to files, you'll also need:

```bash
pip install altair_saver
```

If you want to save as PNG/SVG, you'll need additional dependencies:
```bash
# Option 1: Using Selenium + Chrome/Firefox
pip install selenium
# Plus download appropriate webdriver for your browser

# Option 2: Using Node.js packages (recommended)
npm install -g vega-lite vega-cli canvas
```

## Common Issues and Solutions

### 1. Visualization Not Displaying

**Problem**: Charts don't appear when running scripts locally.

**Solution**: Use the appropriate renderer for your environment:

```python
# For Jupyter notebooks
alt.renderers.enable('notebook')

# For standalone HTML files (most reliable for local development)
alt.renderers.enable('html')
chart.save('my_visualization.html')  # Save to HTML file to view in browser

# For VS Code with Jupyter extension
alt.renderers.enable('mimetype')
```

### 2. Missing Dependencies

**Problem**: Error about missing vega or vega-lite.

**Solution**: Ensure you have the complete stack:

```bash
pip install altair vega_datasets notebook vega
```

### 3. Data Loading Issues

**Problem**: Cannot load example datasets.

**Solution**: Use vega_datasets or pandas:

```python
# Using vega_datasets
from vega_datasets import data
source = data.cars()

# Or using pandas with your own data
import pandas as pd
source = pd.read_csv('your_data.csv')
```

## Working Example

Here's a complete working example that saves to an HTML file:

```python
import altair as alt
from vega_datasets import data
import pandas as pd

# Set renderer to HTML
alt.renderers.enable('html')

# Load dataset
source = data.cars()

# Create chart
chart = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

# Save to HTML file
chart.save('altair_visualization.html')
print("Visualization saved to 'altair_visualization.html'")
```

## Viewing Your Visualizations

1. Run your Python script
2. Open the generated HTML file in your web browser
3. Interact with your visualization

## Advanced Configuration

For more advanced configuration options, see the [Altair documentation](https://altair-viz.github.io/user_guide/display_options.html).