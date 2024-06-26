# -*- coding: utf-8 -*-
"""EDA&Cleaning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ORJ0gtvvTVvqo7oWKaEURfqeBToldusX
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import shapiro
from sklearn.preprocessing import LabelEncoder

# Function to load the dataset
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    print('---------------------------------------------------------------------')
    return df

# Function to display if there is any duplicat or null values
def check_duplicat_or_null(df):
  print(df.isnull().sum()/len(df)*100)
  print('---------------------------------------------------------------------')
  print(df.duplicated().sum())
  print('---------------------------------------------------------------------')

# Function to display dataset information
def display_dataset_info(df):
    print("Dataset Info:")
    print(df.info())
    print('---------------------------------------------------------------------')

# Function to display dataset summary statistics
def display_summary_statistics(df):
    print("Summary Statistics:")
    print(df.describe())
    print('---------------------------------------------------------------------')

# Function to display unique values count in each column
def display_unique_values_count(df):
    print("Unique Values Count:")
    print(df.nunique())
    print('---------------------------------------------------------------------')

# Function to perform exploratory data analysis and visualizations  #EDA
def exploratory_data_analysis(df):
    plt.figure(figsize=(10, 30))
    for i, col in enumerate(df.columns[1:-1], 1):
        plt.subplot(8, 1, i)
        sns.histplot(x=df[col], hue=df["fuelType"], multiple="dodge")
        plt.title(f"Distribution of {col} Data")
        plt.xticks(rotation=90)
        plt.tight_layout()
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["price"], hue = df[df["fuelType"] == "Petrol"]["fuelType"])
    plt.title("Mileage vs Price for Petrol Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["price"], hue = df[df["fuelType"] == "Diesel"]["fuelType"])
    plt.title("Mileage vs Price for Diesel Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["transmission"], hue = df[df["fuelType"] == "Petrol"]["fuelType"])
    plt.title("Mileage vs Transmission for Petrol Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["transmission"], hue = df[df["fuelType"] == "Diesel"]["fuelType"])
    plt.title("Mileage vs Transmission for Diesel Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["tax"], hue = df[df["fuelType"] == "Petrol"]["fuelType"])
    plt.title("Mileage vs Tax for Petrol Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["tax"], hue = df[df["fuelType"] == "Diesel"]["fuelType"])
    plt.title("Mileage vs Tax for Diesel Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["engineSize"], hue = df[df["fuelType"] == "Petrol"]["fuelType"])
    plt.title("Mileage vs Engine Size for Petrol Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["engineSize"], hue = df[df["fuelType"] == "Diesel"]["fuelType"])
    plt.title("Mileage vs Engine Size for Diesel Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["Manufacturer"], hue = df[df["fuelType"] == "Petrol"]["fuelType"])
    plt.title("Mileage vs Manufacturer for Petrol Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

    sns.scatterplot(x = df["mileage"], y = df["Manufacturer"], hue = df[df["fuelType"] == "Diesel"]["fuelType"])
    plt.title("Mileage vs Manufacturer for Diesel Vehicles")
    plt.show()
    print('---------------------------------------------------------------------')

def visualize_categorical_features(df):
    # Use LabelEncoder on object type of some features
    cat_cols = ["model", "transmission", "fuelType", "Manufacturer"]
    le = LabelEncoder()
    for label in cat_cols:
        df[label] = le.fit_transform(df[label])

    # Print the head of the DataFrame after encoding
    print(df.head())
    print('---------------------------------------------------------------------')

    # Compute correlation matrix
    df_corr = df.corr()

    # Sort the correlation of 'fuelType' in descending order
    sorted_corr = df_corr["fuelType"].sort_values(ascending=False)

    # Visualize correlation heatmap
    sns.heatmap(df_corr, fmt=".3f", cmap="YlGnBu")
    plt.show()
    print('---------------------------------------------------------------------')

    # Scatter plot for 'price' vs 'engineSize' for fuelType == 0 (Petrol)
    sns.scatterplot(x=df["price"], y=df["engineSize"], hue=df[df["fuelType"] == 0]["fuelType"])
    plt.show()
    print('---------------------------------------------------------------------')

    # Scatter plot for 'price' vs 'engineSize' for fuelType == 2 (Diesel)
    sns.scatterplot(x=df["price"], y=df["engineSize"], hue=df[df["fuelType"] == 2]["fuelType"])
    plt.show()
    print('---------------------------------------------------------------------')

    # Scatter plot for 'price' vs 'year' for fuelType == 0 (Petrol)
    sns.scatterplot(x=df["price"], y=df["year"], hue=df[df["fuelType"] == 0]["fuelType"])
    plt.show()
    print('---------------------------------------------------------------------')

    # Scatter plot for 'price' vs 'year' for fuelType == 2 (Diesel)
    sns.scatterplot(x=df["price"], y=df["year"], hue=df[df["fuelType"] == 2]["fuelType"])
    plt.show()
    print('---------------------------------------------------------------------')

    # Print the columns of the DataFrame except the last one
    print(df.columns[:-1])
    print('---------------------------------------------------------------------')

    return df

def remove_outliers(df):
    # Check outliers
    plt.figure(figsize=(10, 20))
    for i, col in enumerate(df.columns[:-1], 1):
        plt.subplot(3, 3, i)
        skewness = df[col].skew()
        sns.histplot(df[col], kde=True, label="Skew = %.3f" % (skewness))
        plt.title(f"Skewness of {col} Data")
        plt.legend(loc="best")
        plt.tight_layout()
        plt.plot()
        print('---------------------------------------------------------------------')

    for col in df.columns[:-1]:
        print(f"Column : {col}")
        plt.hist(df[col], density=True, bins=30)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = stats.norm.pdf(x, np.mean(df[col]), np.std(df[col]))
        plt.plot(x, p, 'k', linewidth=2)
        plt.show()
        print('---------------------------------------------------------------------')

        stat, p = shapiro(df[col])
        print("Statistics = %.3f, p = %.3f" % (stat, p))

        alpha = 0.05
        if p > alpha:
            print("Data looks Gaussian Distribution(fail to reject H0) \n")
        else:
            print("Data does not look Gaussian Distribution(reject H0) \n")

    # remove outliers
    for col in df.columns[:-1]:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= (Q1 - 1.5 * IQR)) & (df[col] <= (Q3 + 1.5 * IQR))]

    # Check how many outliers are removed
    plt.figure(figsize=(10, 20))
    for i, col in enumerate(df.columns[:-1], 1):
        plt.subplot(3, 3, i)
        skewness = df[col].skew()
        sns.histplot(df[col], kde=True, label="Skew = %.3f" % (skewness), bins=30)
        plt.title(f"Skewness of {col} data outliers removed")
        plt.legend(loc="best")
        plt.tight_layout()
        plt.plot()
        print('---------------------------------------------------------------------')

    return df

def main():
  file_path = '/content/CarsData.csv'
  df = load_dataset(file_path)
  check_duplicat_or_null(df)
  display_dataset_info(df)
  display_summary_statistics(df)
  display_unique_values_count(df)
  exploratory_data_analysis(df)
  df = visualize_categorical_features(df)
  df = remove_outliers(df)
  df.to_csv('cleanning_CarsData.csv',encoding='utf-8',sep=',',index=False)

if __name__ == '__main__':
  main()

