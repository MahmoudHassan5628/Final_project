import tkinter as tk
from tkinter import ttk
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the trained model
model = joblib.load(r"D:\PROJECTS\Final_Project\models\random_forest_model")

# Dictionary mapping predicted values to fuel types
fuel_type_mapping = {
    0: "Petrol",
    1: "Diesel",
    2: "Hybrid",
    3: "Electric",
    4: "Other"
}

# Function to predict fuelType
def predict_fuel_type():
    # Get input values
    model_val = model_entry.get()
    year_val = int(year_entry.get())
    price_val = float(price_entry.get())
    transmission_val = transmission_combobox.get()
    mileage_val = float(mileage_entry.get())
    tax_val = float(tax_entry.get())
    mpg_val = float(mpg_entry.get())
    engine_size_val = float(engine_size_entry.get())
    manufacturer_val = manufacturer_entry.get()

    # Make prediction
    features = [[model_val, year_val, price_val, transmission_val, mileage_val, tax_val, mpg_val, engine_size_val, manufacturer_val]]
    fuel_type_prediction = model.predict(features)

    # Map predicted value to fuel type
    predicted_fuel_type = fuel_type_mapping.get(fuel_type_prediction[0], "Unknown")

    # Display prediction
    result_label.config(text=f"Predicted FuelType: {predicted_fuel_type}")

# Create main window
root = tk.Tk()
root.title("Car FuelType Prediction")

# Add input fields
model_label = ttk.Label(root, text="Model:")
model_label.grid(row=0, column=0, padx=5, pady=5)
model_entry = ttk.Entry(root)
model_entry.grid(row=0, column=1, padx=5, pady=5)

year_label = ttk.Label(root, text="Year:")
year_label.grid(row=1, column=0, padx=5, pady=5)
year_entry = ttk.Entry(root)
year_entry.grid(row=1, column=1, padx=5, pady=5)

price_label = ttk.Label(root, text="Price:")
price_label.grid(row=2, column=0, padx=5, pady=5)
price_entry = ttk.Entry(root)
price_entry.grid(row=2, column=1, padx=5, pady=5)

transmission_label = ttk.Label(root, text="Transmission:")
transmission_label.grid(row=3, column=0, padx=5, pady=5)
transmission_combobox = ttk.Combobox(root, values=[0, 1])
transmission_combobox.grid(row=3, column=1, padx=5, pady=5)

mileage_label = ttk.Label(root, text="Mileage:")
mileage_label.grid(row=4, column=0, padx=5, pady=5)
mileage_entry = ttk.Entry(root)
mileage_entry.grid(row=4, column=1, padx=5, pady=5)

tax_label = ttk.Label(root, text="Tax:")
tax_label.grid(row=5, column=0, padx=5, pady=5)
tax_entry = ttk.Entry(root)
tax_entry.grid(row=5, column=1, padx=5, pady=5)

mpg_label = ttk.Label(root, text="MPG:")
mpg_label.grid(row=6, column=0, padx=5, pady=5)
mpg_entry = ttk.Entry(root)
mpg_entry.grid(row=6, column=1, padx=5, pady=5)

engine_size_label = ttk.Label(root, text="Engine Size:")
engine_size_label.grid(row=7, column=0, padx=5, pady=5)
engine_size_entry = ttk.Entry(root)
engine_size_entry.grid(row=7, column=1, padx=5, pady=5)

manufacturer_label = ttk.Label(root, text="Manufacturer:")
manufacturer_label.grid(row=8, column=0, padx=5, pady=5)
manufacturer_entry = ttk.Entry(root)
manufacturer_entry.grid(row=8, column=1, padx=5, pady=5)

# Add predict button
predict_button = ttk.Button(root, text="Predict FuelType", command=predict_fuel_type)
predict_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Add label for displaying result
result_label = ttk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

# Run the GUI
root.mainloop()
