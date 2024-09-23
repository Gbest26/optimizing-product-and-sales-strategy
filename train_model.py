# Import necessary libraries
import argparse
import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from category_encoders import OneHotEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import pickle

def main(args):
    # Enable MLflow autologging
    mlflow.autolog()

    # Start an MLflow run
    with mlflow.start_run():
        # Read data
        df = get_data(args.training_data)

        # Split data
        X_train, X_test, y_train, y_test = split_data(df)

        # Train model
        model = train_model(args.reg_rate, X_train, y_train)

        # Evaluate model
        eval_model(model, X_train, X_test, y_train, y_test)

        # Save model
        save_model(model, 'production_and_sales_model.pkl')


# Function to read the dataset
def get_data(path):
    print("Reading data...")
    df = pd.read_csv(path)
    return df


# Function to split the data into training and test sets
def split_data(df):
    print("Splitting data...")

    target = "Price(USD)"
    X = df.drop(columns=[target])
    y = df[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
    
    return X_train, X_test, y_train, y_test


# Function to train the model using Ridge regression
def train_model(reg_rate, X_train, y_train):
    print("Training model...")

    # Preprocessing pipeline
    pipeline = Pipeline(steps=[
        ('encoder', OneHotEncoder(use_cat_names=True)),
        ('imputer', SimpleImputer(strategy='mean')),
        ('ridge', Ridge(alpha=1/reg_rate))
    ])

    # Fit the model
    model = pipeline.fit(X_train, y_train)
    return model


# Function to evaluate the model performance
def eval_model(model, X_train, X_test, y_train, y_test):
    print("Evaluating model...")

    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Calculate MAE
    mae_train = mean_absolute_error(y_train, y_train_pred)
    mae_test = mean_absolute_error(y_test, y_test_pred)

    # Log metrics to MLflow
    mlflow.log_metric("MAE Train", mae_train)
    mlflow.log_metric("MAE Test", mae_test)

    # Print MAE
    print(f"MAE Train: {mae_train}")
    print(f"MAE Test: {mae_test}")

    # Plot predictions vs actuals
    plt.scatter(y_test, y_test_pred)
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted Prices')
    plt.show()

    # Log the plot to MLflow
    plt.savefig("predictions_vs_actuals.png")
    mlflow.log_artifact("predictions_vs_actuals.png")


# Function to save the model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model saved to {filename}")
    mlflow.log_artifact(filename)


# Argument parser
def parse_args():
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--training_data", type=str, required=True, help="Path to the training data CSV file")
    parser.add_argument("--reg_rate", type=float, default=0.01, help="Regularization rate (inverse of alpha)")

    # Parse arguments
    args = parser.parse_args()
    return args


# Entry point
if __name__ == "__main__":
    print("\n\n" + "*" * 60)

    # Parse command-line arguments
    args = parse_args()

    # Run the main function
    main(args)

    print("*" * 60 + "\n\n")
