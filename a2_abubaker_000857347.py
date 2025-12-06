"""I, Ali Abubaker 000857347 certify that this material is my original", "work. I have not shared this file. No other person's work has been used without due acknowledgement."""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def plot_tech_distribution():
    """
        This function shows the most used technologies by co-ops in Summer 2024
        Reads data from CSV, processes it, and creates a pie chart.
    """
    data = pd.read_csv('a2_coop_tech_s24.csv', header=None)
    tech_counts = data.stack().str.strip().str.lower().value_counts()
    significant_techs = tech_counts[tech_counts > tech_counts.max() * 0.1]
    significant_techs['Other'] = tech_counts[tech_counts <= tech_counts.max() * 0.1].sum()
    significant_techs = significant_techs[significant_techs / significant_techs.sum() * 100 >= 1.75].sort_values(ascending=False)
    colors = ['#FFB6C1', '#FFD700', '#98FB98', '#87CEFA', '#FFC0CB', '#90EE90', '#D3D3D3', '#FF6347', '#E6E6FA', '#FF1493']
    explode = [0.1 if tech == 'Other' else 0 for tech in significant_techs.index]
    # Function to format percentages for the pie chart labels
    def format_percentage(percentage):
        return f'{percentage:.1f}%' if percentage >= 1.75 else ''
    # Create the pie chart
    plt.figure(figsize=(8, 6), dpi=100)
    wedges, texts, autotexts = plt.pie(
        significant_techs, colors=colors, startangle=25, pctdistance=0.8, explode=explode,
        autopct=format_percentage, textprops={'fontsize': 8, 'color': 'black'}
    )
    # Label each part of the pie chart with the name of the technology
    for wedge, tech in zip(wedges, significant_techs.index):
        angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
        x, y = np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))
        ha = 'left' if x > 0 else 'right'
        rotation = angle if x > 0 else angle + 180
        label_position = (1.2 * x, 1.2 * y) if tech != 'Other' else (0.1, 1.2)
        plt.annotate(tech, xy=(x, y), xytext=label_position, fontsize=8, ha=ha, rotation=0 if tech == 'Other' else rotation, rotation_mode='anchor')
        if tech == 'Other':
            plt.text(0, 0.6, 'Many Specialized Technologies\n\nWere Reported Only Once', fontsize=10, ha='center', va='center', color='black')
    # Set the title and show the pie chart
    plt.title('Top Technologies Used By Co-ops Summer 2024', fontsize=14, pad=18, fontweight='bold', fontfamily='serif')
    plt.axis('equal')
    plt.savefig('coop_tech_pie_chart.png', bbox_inches='tight', dpi=100)
    plt.show()
if __name__ == "__main__":
    plot_tech_distribution()
