import streamlit as st
import pandas as pd
import json
import requests

# Title for the web app
st.title('Healthy Foods Average Price Prediction')

# Collect input from the user
country = st.selectbox('Select a Country', ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Cote D\'Ivoire (Ivory Coast)', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji Islands', 'Finland', 'France', 'Gabon', 'Gambia The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Vincent And The Grenadines', 'Samoa', 'San Marino', 'Sao Tome And Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
)
season = st.selectbox('Select a Season', ['Summer', 'Winter', 'Spring', 'Fall', 'Wet Season', 'Dry Season'])
healthy_food = st.selectbox('Select a Healthy Food', ["Avocado", "Quinoa", "Cucumber", "Almonds", "Chia Seeds", "Blueberries", 
            "Greek Yogurt", "Spinach", "Salmon", "Olive Oil", "Broccoli", "Sweet Potatoes", 
            "Walnuts", "Oats", "Green Tea", "Garlic", "Turmeric", "Ginger", "Flax Seeds", 
            "Honey", "Dark Chocolate", "Lentils", "Brown Rice", "Hemp Seeds", "Pineapple", 
            "Goji Berries", "Coconut Oil", "Eggs", "Pumpkin Seeds", "Matcha", "Mango", 
            "Tuna", "Hummus", "Pomegranate", "Beets", "Bell Peppers", "Cottage Cheese", 
            "Brussels Sprouts", "Carrots", "Tomatoes", "Artichokes", "Cashews", "Figs", 
            "Papaya", "Seaweed", "Cranberries", "Kimchi", "Chickpeas", "Raspberries", 
            "Pistachios"]
)
unit_of_measurement = st.number_input('Enter Unit of Measurement (e.g., 100 for grams, 1 for piece)', min_value=1)
measurement_type = st.selectbox('Select a Measurement Type', ['Bulk', 'Grams', 'Grams Per Bulk', 'Grams Per Grams Per Can', 'Grams Per Bunch', 'Tea Bag', 'Kilogram', 'Millilitres', 'Piece'])

# Create input data for the prediction
input_data = {
    "input_data": {
        "columns": ["Countries", "Seasons", "Healthy Foods", "Unit of Measurement", "Measurement Type"],
        "index": [0],
        "data": [[country, season, healthy_food, unit_of_measurement, measurement_type]]
    }
}

# Display the input data
# st.write("Input Data for Prediction:")
# st.json(input_data)

# Send data to your Azure ML model for prediction
if st.button('Predict Price'):
    url = 'https://optimizing-production-and-jfimz.eastus2.inference.ml.azure.com/score'
    api_key = 'eOgSsBbK4luONHPTVCOgrAZs6vLrsyXE'  # Replace with your API key

    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {api_key}'}

    # Call the Azure ML service and get the prediction
    try:
        response = requests.post(url, headers=headers, json=input_data)
        result = response.json()
        st.success(f"Predicted Price (USD): {result[0]:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
