import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io


def add_fielder_positions(ax, positions_and_names):
    for position, name in positions_and_names.items():
        color = 'blue' if 'Batsman' in name else 'orange'
        ax.scatter(position[0], position[1], c=color)
        ax.text(position[0], position[1]+0.01, name, fontsize=8, ha='center', color=color)
def add_stumps(ax):
    stump_width = 0.002
    stump_height = 0.01
    
    # Draw batting stumps
    for x in [0.49, 0.50, 0.51]:
        ax.plot([x, x], [0.615, 0.615 + stump_height], color='red', linewidth=1, zorder=2)

    # Draw bowling stumps
    for x in [0.49, 0.50, 0.51]:
        ax.plot([x, x], [0.385, 0.385 + stump_height], color='red', linewidth=1, zorder=2)
    
    # Add label for stumps
    ax.text(0.50, 0.622 + stump_height, '(Batting Side)\nStump ', fontsize=8, color='white', ha='center')  # Batting stump label
    ax.text(0.50, 0.350 + stump_height, 'Stump \n (Bowling Side)', fontsize=8, color='white', ha='center')  # Bowling stump label


def add_bat(ax):
    bat = patches.Rectangle((0.525, 0.605), 0.03, 0.004, angle=165, facecolor='saddlebrown', edgecolor='black', zorder=1)
    ax.add_patch(bat)

def draw_cricket_pitch():
    # Create the main cricket ground ellipse (outer boundary)
    out_field = patches.Ellipse((0.5, 0.5), 1, 0.8, facecolor='darkgreen', zorder=0)

    # Create a subplot with one axis and set the figure size
    fig, ax = plt.subplots(1, figsize=(8, 8))

    # Add the main cricket ground ellipse to the axis
    ax.add_patch(out_field)

    # Add the pitch ellipse (inner boundary representing the pitch)
    inner_circle = patches.Ellipse((0.5, 0.5), 0.6, 0.5, edgecolor='white', fill=False, ls='-.', zorder=0)
    ax.add_patch(inner_circle)

    # Add the rectangular patch for one end of the pitch
    pitch = patches.Rectangle((0.425, 0.35), 0.15, 0.3, facecolor='peru', alpha=1, zorder=0)
    ax.add_patch(pitch)

    # Add grease
    for y in [0.6, 0.375]:
        grease = patches.Rectangle((0.45, y), 0.1, 0.03, edgecolor='white', fill=False, zorder=0)
        ax.add_patch(grease)

    # Wide line
    for y in [0.6, 0.375]:
        wide_line = patches.Rectangle((0.465, y), 0.07, 0.03, edgecolor='white', fill=False, zorder=0)
        ax.add_patch(wide_line)

    # Scatter plot to represent player positions with labels
    positions_and_names = {
        (0.65, 0.6): 'Mid Wicket',
        (0.1, 0.7): 'Deep Backward Point',
        (0.3, 0.5): 'Deep Point',
        (0.5, 0.22): 'Bowler',
        (0.5, 0.69): 'Keeper',
        (0.15, 0.28): 'Long Off',
        (0.7, 0.18): 'Long On',
        (0.8, 0.69): 'Short Third Man',
        (0.43, 0.71): '1st Slip',
        (0.8, 0.5): 'Point',
        (0.33, 0.68): 'Cover',
        (0.529, 0.605): 'Batsman',  # Batsman position
        (0.55, 0.405): 'NS \nBatsman'  # Non-striking Batsman position
    }
    add_fielder_positions(ax, positions_and_names)

    # Add stumps and draw lines
    add_stumps(ax)

    # Add bat
    add_bat(ax)


    # Add bat
    add_bat(ax)
    
    # Add watermark
    watermark_text = 'Hari-BME'
    ax.annotate(watermark_text, xy=(0.5, 0.5), xycoords='axes fraction',
                fontsize=12, color='grey', alpha=0.5, rotation=45, ha='center', va='center')




# Hide axis
    ax.axis('off')

    # Save the plot as an image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Display the image using Streamlit
    st.image(img)

def main():
    st.title('Cricket Pitch Visualization')
    draw_cricket_pitch()

if __name__ == '__main__':
    main()
