import matplotlib.pyplot as plt
import mpld3
from matplotlib import patches

# Define the regions to be colored and their group names
df = {'group1': [('95906', '104903'), ('102794', '122504'), ('162313', '162609'), ('269472', '289602'), ('270605', '272936'), ('403455', '403751')],
      'TraesCS1A03G0001300.1': [('169592', '169969'), ('297266', '297652'), ('326099', '326518')]}

# Create a horizontal bar chart
fig, ax = plt.subplots()

# Set the x-axis range
ax.set_xlim(0, 500000)

# Iterate through the groups in df
patches_list = []
for group, regions in df.items():
    # Create a patch for the group
    color = 'C' + str(len(patches_list))
    patch = patches.Patch(color=color, label=group)
    patches_list.append(patch)

    # Iterate through the regions in the group
    for region in regions:
        # Get the start and end positions of the region
        start, end = int(region[0]), int(region[1])
        # Plot the region as a rectangle on the bar chart
        ax.barh(0, end - start, left=start, height=1, color=color, alpha=0.7, edgecolor='black', linewidth=0.2)
        # Add the group label to the region
        ax.text(start + (end - start) / 2, 1, group, ha='center', va='center', color='black', fontsize=8)

# Position the labels to prevent overlap
ax.text(0, 1.1, 'Group 1', ha='left', va='center', fontsize=8)
ax.text(0, 0.9, 'TraesCS1A03G0001300.1', ha='left', va='center', fontsize=8)

# Add the legend
ax.legend(handles=patches_list)

# Show the plot
mpld3.show()