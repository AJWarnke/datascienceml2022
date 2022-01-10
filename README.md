# Forecasting-Challenge
This repository contains code for predicting the water level of the Rhine.

## Install
In order to install all the dependencies via conda use the command:
> conda env create --name envname --file=environment.yml

## Files

In the following, I will provide a short summary about the individual files. The main files are analysis.ipynb and network-DWD.ipynb. The main contributions are in bold:

* __analysis.ipynb__: Analysis and visualization of the dataset.
* __network-DWD.ipynb__: Prediction on the data using additional data from Deutscher Wetterdienst (DWD)
* __duplicates.ipynb__: Shows the duplicate/missing values in the original and first updated values
* __sarima.ipynb__: Prediction using SARIMA
* network-sine.ipynb: Shows that the implementation of the LSTM model is right (Proof of concept) and that it works on seasonal data
* network-passengers.ipynb: Implementation of LSTM on short airplane passengers data from kaggle. Shows the problems LSTM when having not enough data
