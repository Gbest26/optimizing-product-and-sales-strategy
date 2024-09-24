# Project Title: Optimizing Product  and Sales Strategy for Healthy Foods
## Sub Head: Healthy Foods Price Prediction Across Seasons

## Project Overview:

This project aims to assist customers and new business owners in the healthy food sector by providing insights into the average price of various healthy foods across different seasons. This model helps users anticipate and plan for price fluctuations based on the seasonality of products, offering them a sense of how much these items typically cost in different countries and times of the year.

## Data:

The dataset used for this project was gathered from Kaggle and various online resources. It includes information about the prices of healthy foods, categorized by country, season, food type, unit of measurement, and measurement type. 

The Price (USD) is the target vector used for prediction in this project.

## Model and Deployment:

A Linear Regression model was built to predict the price of healthy foods based on the dataset. The key input features for the model include:

    Countries
    Seasons
    Healthy Foods
    Unit of Measurement
    Measurement Type

After training the model, it was deployed on Microsoft Azure using Azure’s Machine Learning services. The model was exposed via an endpoint, which allows for real-time predictions based on user input.

## Application:

A Streamlit web application was developed to provide an easy-to-use interface for users to input their data and get instant price predictions. The Streamlit app was then deployed to the Streamlit Cloud for public access. The web app enables users to select a country, season, and food type, input their unit of measurement, and instantly receive a price prediction for the selected food item.

## Purpose:

This project primarily serves as a pricing tool for healthy food vendors, customers, and small business owners, giving them a sense of how food prices fluctuate across countries and seasons. It is especially useful for those planning to enter the market, as it provides average pricing trends that could be used for cost analysis and market strategy planning.
