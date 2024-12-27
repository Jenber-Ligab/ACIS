import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
  def __init__(self, data: pd.DataFrame):
   if __name__ == "__main__":
    # Read the processed data
    df = pd.read_csv("Data/processed/cleaned_data.csv")
    import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the DataVisualizer class with a dataset.
        """
        self.data = data
        sns.set(style="whitegrid")  # Set a global seaborn style

    # ... rest of the class methods ...

if __name__ == "__main__":
    # Read the processed data
    df = pd.read_csv("Data/processed/cleaned_data.csv")
    
    # Create visualizer instance
    visualizer = DataVisualizer(df)
    
    # Generate and save all plots
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    # 1. Numerical columns analysis
    visualizer.plot_outliers_boxplot(numerical_cols)
    
    # 2. Correlation analysis
    visualizer.plot_correlation_heatmap(numerical_cols)
    
    # 3. Premium analysis
    visualizer.plot_violin_premium_by_cover('CoverType', 'TotalPremium')
    
    # 4. Geographical analysis
    common_cover_types = df['CoverType'].value_counts().nlargest(5).index.tolist()
    visualizer.plot_geographical_trends(common_cover_types)
    # Create visualizer instance
    visualizer = DataVisualizer(df)
    
    # Create output directory
    os.makedirs("Data/visualizations", exist_ok=True)
    
    # Save plots to files
    plt.figure(figsize=(12, 8))
    
    # 1. Numerical columns analysis
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    visualizer.plot_outliers_boxplot(numerical_cols)
    plt.savefig("Data/visualizations/numerical_analysis.png")
    plt.close()
    
    # 2. Correlation analysis
    plt.figure(figsize=(10, 8))
    visualizer.plot_correlation_heatmap(numerical_cols)
    plt.savefig("Data/visualizations/correlation_heatmap.png")
    plt.close()
    
    # 3. Premium analysis
    plt.figure(figsize=(12, 6))
    visualizer.plot_violin_premium_by_cover('CoverType', 'TotalPremium')
    plt.savefig("Data/visualizations/premium_by_cover.png")
    plt.close()
    
    # 4. Geographical analysis
    common_cover_types = df['CoverType'].value_counts().nlargest(5).index.tolist()
    visualizer.plot_geographical_trends(common_cover_types)
    plt.savefig("Data/visualizations/geographical_trends.png")
    plt.close()