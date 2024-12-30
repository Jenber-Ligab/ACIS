import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_visualization import DataVisualizer

# Set page config
st.set_page_config(
    page_title="Insurance Data EDA",
    page_icon="📊",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Data/processed/cleaned_data.csv", low_memory=False)

def main():
    st.title("Insurance Data Exploratory Analysis")
    
    # Load data
    df = load_data()
    visualizer = DataVisualizer(df)
    
    # Sidebar
    st.sidebar.header("Visualization Options")
    analysis_type = st.sidebar.selectbox(
        "Choose Analysis Type",
        ["Overview", "Numerical Analysis", "Geographical Analysis", "Premium Analysis"]
    )
    
    if analysis_type == "Overview":
        st.header("Dataset Overview")
        st.write(df.head())
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Dataset Info")
            buffer = io.StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())
        
        with col2:
            st.subheader("Basic Statistics")
            st.write(df.describe())
    
    elif analysis_type == "Numerical Analysis":
        st.header("Numerical Features Analysis")
        
        # Outliers Analysis
        st.subheader("Outliers Analysis")
        numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        selected_cols = st.multiselect("Select columns for outlier analysis", numerical_cols)
        
        if selected_cols:
            fig, ax = plt.subplots(figsize=(12, 6))
            visualizer.plot_outliers_boxplot(selected_cols)
            st.pyplot(fig)
        
        # Correlation Analysis
        st.subheader("Correlation Analysis")
        fig, ax = plt.subplots(figsize=(10, 8))
        visualizer.plot_correlation_heatmap(numerical_cols)
        st.pyplot(fig)
    
    elif analysis_type == "Geographical Analysis":
        st.header("Geographical Analysis")
        
        # Get top cover types
        top_n = st.slider("Select number of top cover types", 2, 10, 5)
        common_cover_types = df['CoverType'].value_counts().nlargest(top_n).index.tolist()
        
        fig = plt.figure(figsize=(16, 12))
        visualizer.plot_geographical_trends(common_cover_types)
        st.pyplot(fig)
        
        # Additional province-wise analysis
        st.subheader("Province-wise Statistics")
        province_stats = df.groupby('Province').agg({
            'TotalPremium': ['mean', 'median', 'count'],
            'VehicleType': 'nunique'
        }).round(2)
        st.write(province_stats)
    
    elif analysis_type == "Premium Analysis":
        st.header("Premium Analysis")
        
        # Premium distribution by cover type
        st.subheader("Premium Distribution by Cover Type")
        fig = plt.figure(figsize=(12, 6))
        visualizer.plot_violin_premium_by_cover('CoverType', 'TotalPremium')
        st.pyplot(fig)
        
        # Premium statistics
        st.subheader("Premium Statistics by Cover Type")
        premium_stats = df.groupby('CoverType')['TotalPremium'].describe().round(2)
        st.write(premium_stats)

if __name__ == "__main__":
    main() 