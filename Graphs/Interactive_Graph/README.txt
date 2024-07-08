This repository contains a Python script that uses Plotly to create an interactive bar graph for visualizing ortholog groups in Triticum aestivum chromosome 1A. The script generates a custom bar graph with ortholog groups represented in distinct colors. The graph is interactive, allowing users to pan, zoom, and toggle the visibility of groups by clicking on the legend.

Prerequisites
Python 3.x
Plotly (install using pip install plotly)
PyCharm or any other Python IDE

Running the Script
1. Create a new PyCharm project or open an existing project in your preferred Python IDE.
2. Add the Python script to your project.
3. (Optional) Update the input data dictionaries df and nameDF with your own data.
4. Run the script in your IDE.

Understanding the Code
The script contains the following key components:

1. hex_to_rgba(hex_color, alpha): This function converts a hex color code to an RGBA color code with a specified alpha value for transparency.

2. Data dictionaries df and nameDF: These dictionaries store the input data for the ortholog groups and their corresponding gene IDs.

3. Plotly figure creation: The script creates a go.Figure() object and loops through the ortholog groups in the input data. For each group, it calculates the x values for the middle of each range and adds a bar trace to the figure with a unique color.

4. Figure settings: The script updates the y-axis and layout settings to customize the appearance of the graph.

5. Display the figure: The script calls fig.show() to display the interactive graph.

Output
The script generates an interactive bar graph with ortholog groups represented in distinct colors. The graph allows users to pan, zoom, and toggle the visibility of the groups by clicking on the legend. The hover text displays the group name and the start and end values of each range.