
import unittest
import pandas as pd
import numpy as np
from medical_data_visualizer import df, draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt


class TestMedicalDataVisualizer(unittest.TestCase):
    
    def test_data_loaded(self):
        """Test that data is loaded correctly"""
        self.assertEqual(len(df), 70000, "Dataset should have 70000 rows")
        self.assertIn('age', df.columns, "Dataset should have 'age' column")
        self.assertIn('cardio', df.columns, "Dataset should have 'cardio' column")
    
    def test_overweight_column_exists(self):
        """Test that overweight column is added"""
        self.assertIn('overweight', df.columns, "Dataset should have 'overweight' column")
        self.assertTrue(df['overweight'].isin([0, 1]).all(), "Overweight should be binary")
    
    def test_overweight_calculation(self):
        """Test overweight calculation"""
        # BMI > 25 should be 1, otherwise 0
        bmi = df['weight'] / ((df['height'] / 100) ** 2)
        expected = (bmi > 25).astype(int)
        pd.testing.assert_series_equal(df['overweight'], expected, check_names=False)
    
    def test_cholesterol_normalized(self):
        """Test that cholesterol is normalized to 0 and 1"""
        self.assertTrue(df['cholesterol'].isin([0, 1]).all(), "Cholesterol should be 0 or 1")
    
    def test_gluc_normalized(self):
        """Test that gluc is normalized to 0 and 1"""
        self.assertTrue(df['gluc'].isin([0, 1]).all(), "Glucose should be 0 or 1")
    
    def test_cat_plot_function(self):
        """Test categorical plot function"""
        try:
            fig = draw_cat_plot()
            self.assertIsNotNone(fig, "Categorical plot should return a figure")
            plt.close(fig)
        except Exception as e:
            self.fail(f"draw_cat_plot failed with error: {e}")
    
    def test_heat_map_function(self):
        """Test heatmap function"""
        try:
            fig = draw_heat_map()
            self.assertIsNotNone(fig, "Heatmap should return a figure")
            plt.close(fig)
        except Exception as e:
            self.fail(f"draw_heat_map failed with error: {e}")


if __name__ == '__main__':
    unittest.main()
