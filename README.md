
### Code and data for paper "Population-scale dietary interests during the COVID-19 pandemic"
### URL: https://arxiv.org/abs/2109.10808


## Repository structure

### foodle-trends

#### ---> foodle-trends/data
        Contains the datasets necessary to reproduce the results.
        In particular, it contains:

        1. Aggregated dataframes:
        'df_agg_cats.pickle' contains Google Trends attention timeseries for foods belonging to different categories.
        ‘df_agg_modes.pickle’ contains Google Trends attention timeseries for foods belonging to different ways of accessing food.


        2. Raw dataframes:
        ‘food_timeseries.parquet’
        ‘modes_timeseries.parquet’


        3. Mobility dataframes:
        ‘df_mobility.csv ‘ is a dataset with mobility data, per day, per country, downloaded from https://www.google.com/covid19/mobility/
                        
#### ---> foodle-trends/figures
        Once the code is evaluated, the figures are stored here.

#### ---> foodle-trends/code

#####        ---> foodle-trends/code/analyses
                This folder contains all the code necessary for reproducing the results reported in the manuscript.
                The code is in the format of Jupyter notebooks. Once the notebook is evaluated, figures are saved in the figures folder, in pdf format. The input for the analyses is loaded from foodle-trends/data folder. The main results are computed in Notebooks 1-4.
                Please see which figure is produced in the corresponding notebook:
                Maps.ipynb: Fig 1B and 1B
                Notebook_1.ipynb: Fig 3A, Fig 6, Fig 7B, Fig S5, Fig S8, Fig S10, Fig S12B
                Notebook_2.ipynb: Fig 5, Fig 7A, Fig S12A
                Notebook_3.ipynb: Fig 3B, Fig 4B, Fig S2A
                Notebook_4.ipynb: Fig 4A, Fig S2B
                Table_1.ipynb: Table 1
                Table_2.ipynb: Table 2
                
                All notebooks except Notebook_1.ipynb are expected to evaluate all cells within a couple of minutes.
                Notebook_1.ipynb can take around 10 minutes to evaluate.
                Code for producing other, supplementary figures and tables is here.
                Each notebook is titled after the figure or table it produces.

######        ---> foodle-trends/code/analysesupplementary material
                                Fig_S1.ipynb
                                Fig_S11a.ipynb
                                Fig_S11b.ipynb
                                Fig_S3a.ipynb
                                Fig_S3b_S6.ipynb
                                Fig_S4a.ipynb
                                Fig_S4b_S7.ipynb
                                Fig_S9a.ipynb
                                Fig_S9b_Tab1.ipynb
                                Table_S1.ipynb
                                Table_S2.ipynb
  

-------------------------------------------------


### System requirements and installation guide


We recommend a local installation of Anaconda (https://www.anaconda.com/distribution/#download-section, Python 3.8 version). The code was tested on macOS with standard hardware.


1. Open the terminal. To avoid any incompatibility issue, please install a new conda environment with a suitable version of python packages. Installation is expected to take a couple of minutes.

"conda create -n foodletrends python=3.8 matplotlib=3.1.3 pandas=1.0.3 numpy=1.18.1 scikit-learn=0.22.1 scipy=1.4.1 statsmodels=0.11.0"

2. Activate the environment.
"conda activate foodletrends"

3. Start a Jupiter notebook server.
"jupyter notebook"

### Instructions for use and reproduction instructions

4. Navigate to "foodle-trends/code" folder from the browser. Select the desired figure to reproduce and click on the corresponding notebook. Select "Cells->Run all". The figures will be displayed in the browser and saved in foodle-trends/figures folder.


