import streamlit as st
st.title("EDA PAGE")
from home import data 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.style.use("fivethirtyeight")

def main():
    st.sidebar.subheader("Choose the plot")

    # show data
    if st.sidebar.checkbox("show data", False):
        st.write(data)

    #univariate histograms
    def histograms(data):
        st.write("Histograms")
        data.hist()
        plt.tight_layout()
        st.pyplot()

    
    def histplot_boxplot(data, feature, bins=None, figsize=(12,7)):
        fig, (ax_box, ax_hist)=plt.subplots(
        nrows=2,
        sharex=True,
        gridspec_kw={"height_ratios":(0.25, 0.75)},
        figsize=figsize)
        
        sns.boxplot(data=data, x=feature, showmeans=True, ax=ax_box, color="violet")
        sns.histplot(data=data, x=feature, bins=bins,ax=ax_hist, pallete="winter") if bins else sns.histplot(data=data,
                                                            x=feature, ax=ax_hist)
        ax_hist.axvline(data[feature].mean(), color='green', linestyle="--")
        ax_hist.axvline(data[feature].median(), color='black', linestyle="-")
        
        st.pyplot()
        
    def countplot(data, feature):
        plt.figure(figsize=(12,7))
        ax=sns.countplot(data=data, x=feature, color="green")
        for p in ax.patches:
            x=p.get_bbox().get_points()[:,0]
            y=p.get_bbox().get_points()[1,1]
            ax.annotate("{:.3g}%".format(100.*y/len(data)), (x.mean(), y), ha="center", va="bottom")
        st.pyplot()

    plot=st.sidebar.selectbox("Choose Plot", ('histograms', 'boxplot-histplot','countplot'))
    if plot=="histograms":
        if st.sidebar.button("PLOT"):
            histograms(data)

    if plot=="boxplot-histplot":
        if st.sidebar.button("PLOT"):
            for col in data.select_dtypes(exclude="O").columns:
                st.write(col)
                histplot_boxplot(data=data, feature=col)
    if plot=="countplot":
        if st.sidebar.button("PLOT"):
                countplot(data, feature="Outcome")
            
    Bivariate_plots = st.sidebar.selectbox("Choose Bivariate Graph", ("Bivariate bar graph", "Scatterplots", "Heatmap "))



    # Bivariate -categorical vs numericAal
    def bivariate_barplot(data, feature1, feature2):
        data.groupby(feature1)[feature2].mean().plot(kind="bar", color="orange")
        plt.ylabel(feature2)
        st.pyplot()

    if Bivariate_plots == 'Bivariate bar graph':
        if st.sidebar.button('PLOT', key='bivars'):
            bivariate_barplot(data, feature1 = 'Outcome', feature2 = 'Age')
    





if __name__=="__main__":
    main()

        