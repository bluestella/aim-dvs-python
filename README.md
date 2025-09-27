# Python Basics for Data Visualization

This repository contains a comprehensive Python tutorial designed specifically for data visualization classes. It provides a step-by-step introduction to Python fundamentals with a focus on concepts relevant to data visualization.

## Contents

The main tutorial file `python_basics.py` covers:

1. **Variables and Data Types** - Learn about integers, floats, strings, booleans, and type conversion
2. **Operators** - Arithmetic, comparison, and logical operators
3. **Control Flow** - If-else statements, for loops, and while loops
4. **Functions** - Basic functions, parameters, default arguments, and lambda functions
5. **Data Structures** - Lists, tuples, dictionaries, and sets
6. **NumPy Basics** - Arrays, operations, and statistical functions
7. **Matplotlib Basics** - Line plots and bar charts
8. **Pandas Basics** - DataFrames, data manipulation, and visualization

Additionally, we have Altair examples for interactive visualizations:
- `altair-samples.py` - Interactive scatter plot example using Altair
- `altair_setup_guide.md` - Detailed guide for setting up Altair locally

## Getting Started

### Prerequisites

To run all sections of this tutorial, you'll need Python 3.6+ and the following packages:

```bash
# Basic data science packages
pip install numpy matplotlib pandas

# For Altair visualizations
pip install altair vega_datasets
```

### Running the Tutorial

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd aim-dvs-python
   ```

2. Run the main tutorial script:
   ```bash
   python python_basics.py
   ```

3. For the visualization sections (NumPy, Matplotlib, Pandas), uncomment the relevant code blocks in the script.

### Using Altair for Interactive Visualizations

To run the Altair examples:

1. Install the required packages:
   ```bash
   pip install altair vega_datasets
   ```

2. Run the Altair sample script:
   ```bash
   python3 altair-samples.py
   ```

3. View the visualization using one of these methods:
   
   **Option 1:** Open the generated HTML file directly in your browser
   
   **Option 2:** Use the included web server (recommended):
   ```bash
   python3 serve_visualizations.py
   ```
   This will start a local web server at http://localhost:8000 and automatically open the visualization in your browser.
   
   The enhanced web server now supports:
   - **Dynamic HTML viewing**: Type any HTML file path in the address bar to view it
   - **Directory listing**: Navigate to http://localhost:8000/ to see all available files
   - **HTML file prioritization**: HTML files are listed first for easy access
   
   Additional web server options:
   ```bash
   # Specify a different port
   python3 serve_visualizations.py --port 8080
   
   # Don't open browser automatically
   python3 serve_visualizations.py --no-browser
   
   # Serve from a specific directory
   python3 serve_visualizations.py --directory /path/to/visualizations
   
   # Specify a default file to open
   python3 serve_visualizations.py --default-file my_visualization.html
   ```

For detailed Altair setup instructions and troubleshooting, see the `altair_setup_guide.md` file.

## Learning Path

For beginners, we recommend following this learning path:

1. Start with basic Python syntax (Sections 1-4)
2. Move on to data structures (Section 5)
3. Learn NumPy for numerical operations (Section 6)
4. Explore data visualization with Matplotlib (Section 7)
5. Study data manipulation with Pandas (Section 8)

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## Contributing

Feel free to contribute to this tutorial by submitting pull requests or suggesting improvements.

## License

This project is open source and available under the [MIT License](LICENSE).