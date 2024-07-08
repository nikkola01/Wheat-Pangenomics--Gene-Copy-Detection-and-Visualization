This repository contains a Python script that uses Matplotlib and mpld3 to create an interactive horizontal bar chart for visualizing ortholog groups in Triticum aestivum chromosome 1A. The script generates a custom bar chart with ortholog groups represented in distinct colors. The graph is interactive, allowing users to pan and zoom.

Note: The saved graph may not be interactive. To solve this issue, run the provided script to generate an interactive version of the graph.

Prerequisites
Python 3.x
Matplotlib (install using pip install matplotlib)
mpld3 (install using pip install mpld3)
PyCharm or any other Python IDE

Running the Script
1. Create a new PyCharm project or open an existing project in your preferred Python IDE.
2. Add the Python script to your project.
3. (Optional) Update the input data dictionary df with your own data.
4. Run the script in your IDE.

Understanding the Code
The script contains the following key components:

1. Data dictionary df: This dictionary stores the input data for the ortholog groups and their corresponding regions.

2. Horizontal bar chart creation: The script creates a plt.subplots() object and loops through the ortholog groups in the input data. For each group, it calculates the start and end positions for each region and adds a rectangle to the chart with a unique color.

3. Figure settings: The script positions the labels to prevent overlap and adds a legend to the chart.

4. Display the figure: The script calls mpld3.show() to display the interactive graph.

Output
The script generates an interactive horizontal bar chart with ortholog groups represented in distinct colors. The graph allows users to pan and zoom. The group labels are positioned to prevent overlap, and a legend displays the group names and their corresponding colors.