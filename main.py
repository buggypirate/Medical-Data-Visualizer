# This file is used for testing during development
# Import the tests from test_module.py
import sys
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Test the functions
if __name__ == "__main__":
    print("Testing categorical plot...")
    fig_cat = draw_cat_plot()
    plt.savefig('cat_plot.png')
    print("Saved cat_plot.png")
    plt.close(fig_cat)
    
    print("Testing heatmap...")
    fig_heat = draw_heat_map()
    plt.savefig('heat_map.png')
    print("Saved heat_map.png")
    plt.close(fig_heat)
    
    print("All tests completed successfully!")
