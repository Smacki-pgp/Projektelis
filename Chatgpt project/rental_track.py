import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os
import sqlite3

# Set up the save directory in the user's Documents folder
save_directory = os.path.join(os.path.expanduser("~"), "Documents", "Duomenys")
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Create a database connection
conn = sqlite3.connect(os.path.join(save_directory, 'rental_data.db'))
cursor = conn.cursor()

# Create a table to store rental data if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS rental_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kliento_vardas TEXT,
    kliento_numeris TEXT,
    imones_kodas TEXT,
    automobilio_modelis TEXT,
    pradinis_km REAL,
    galutinis_km REAL,
    dienos INTEGER,
    dienos_kaina REAL,
    bendra_kaina REAL,
    nuolaida TEXT,
    komentarai TEXT
)
''')
conn.commit()

# Function to convert and validate numeric inputs
def convert_to_float(value, error_label):
    try:
        return float(value)
    except ValueError:
        error_label.grid(padx=5, pady=2)
        return None

def convert_to_int(value, error_label):
    try:
        return int(value)
    except ValueError:
        error_label.grid(padx=5, pady=2)
        return None

# Function to calculate rental cost
def calculate_rental():
    # Get input values
    client_name = entry_client_name.get()
    client_number = entry_client_number.get()
    company_code = entry_company_code.get()
    car_model = car_model_var.get()
    day_price = convert_to_float(entry_day_price.get(), label_day_price_error)
    start_km = entry_start_km.get()
    end_km = entry_end_km.get()
    days = entry_days.get()
    discount = discount_var.get()
    comments = entry_comments.get("1.0", tk.END).strip()

    # Clear previous error indicators
    clear_error_indicators()

    # Validate inputs
    error = False
    if not client_name:
        label_client_name_error.grid(row=0, column=3, padx=5, pady=2)
        error = True
    if not client_number:
        label_client_number_error.grid(row=1, column=3, padx=5, pady=2)
        error = True
    if not company_code:
        label_company_code_error.grid(row=2, column=3, padx=5, pady=2)
        error = True
    if not car_model:
        label_car_model_error.grid(row=10, column=3, padx=5, pady=2)
        error = True
    if day_price is None:
        error = True

    start_km = convert_to_float(start_km, label_start_km_error)
    if start_km is None:
        error = True

    end_km = convert_to_float(end_km, label_end_km_error)
    if end_km is None or (start_km is not None and end_km < start_km):
        if end_km is not None and end_km < start_km:
            messagebox.showerror("Klaida įvedant", "Galutinis km negali būti mažesnis už pradinį km.")
        error = True

    days = convert_to_int(days, label_days_error)
    if days is None or (days is not None and days <= 0):
        if days is not None and days <= 0:
            messagebox.showerror("Klaida įvedant", "Dienų skaičius turi būti didesnis už nulį.")
        error = True

    if error:
        return

    # Calculate cost
    total_cost = days * day_price

    # Apply discount
    if discount == "10% Nuolaida":
        total_cost *= 0.9
    elif discount == "20% Nuolaida":
        total_cost *= 0.8

    # Store data in the database
    cursor.execute('''
        INSERT INTO rental_data (kliento_vardas, kliento_numeris, imones_kodas, automobilio_modelis, pradinis_km, galutinis_km, dienos, dienos_kaina, bendra_kaina, nuolaida, komentarai)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (client_name, client_number, company_code, car_model, start_km, end_km, days, day_price, total_cost, discount, comments))
    conn.commit()

    # Display success message
    messagebox.showinfo("Sėkmingai pavyko", f"Nuoma įrašyta klientui {client_name}. Bendra kaina: {total_cost:.2f}")

# Function to export data to CSV
def export_to_csv():
    try:
        # Ensure data is committed before attempting to export
        conn.commit()
        cursor.execute('SELECT * FROM rental_data')
        rows = cursor.fetchall()
        if rows:
            columns = ["ID", "Kliento Vardas", "Kliento Numeris", "Įmonės Kodas", "Automobilio Modelis", "Pradinis KM", "Galutinis KM", "Dienos", "Dienos Kaina", "Bendra Kaina", "Nuolaida", "Komentarai"]
            df = pd.DataFrame(rows, columns=columns)
            csv_path = os.path.join(save_directory, 'automobiliu_nuoma.csv')
            df.to_csv(csv_path, index=False)
            messagebox.showinfo("Eksportas sėkmingas", f"Duomenys eksportuoti į {csv_path}")
        else:
            messagebox.showwarning("Nėra duomenų", "Nėra duomenų eksportavimui. Įsitikinkite, kad duomenys buvo įvesti ir išsaugoti.")
    except Exception as e:
        messagebox.showerror("Klaida eksportuojant", f"Įvyko klaida eksportuojant į CSV: {e}")

# Function to clear error indicators
def clear_error_indicators():
    label_client_name_error.grid_remove()
    label_client_number_error.grid_remove()
    label_company_code_error.grid_remove()
    label_start_km_error.grid_remove()
    label_end_km_error.grid_remove()
    label_days_error.grid_remove()

# Create the main application window
app = tk.Tk()
app.title("Automobilių Nuomos Sekimo Sistema")
app.geometry("640x600")  # Adjusted window size
app.configure(bg="#ffffff")  # White background for better aesthetics

style = ttk.Style()
style.configure("TLabel", background="#ffffff", foreground="black", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"), padding=8)
style.configure("TEntry", padding=5, fieldbackground="white", foreground="black", font=("Arial", 12))
style.configure("TCombobox", fieldbackground="white", background="white", foreground="black", font=("Arial", 12))

# Center frame to hold all widgets
frame = ttk.Frame(app)
frame.grid(row=0, column=0, sticky='nsew')

# Configure resizing
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(list(range(12)), weight=1)
frame.grid_columnconfigure(1, weight=1)

# Client Information
label_client_name = ttk.Label(frame, text="Kliento Vardas:")
label_client_name.grid(row=0, column=0, padx=10, pady=2, sticky="w")
entry_client_name = tk.Entry(frame, width=40, font=("Arial", 10))
entry_client_name.grid(row=0, column=1, padx=5, pady=2, ipady=2)
label_client_name_error = ttk.Label(frame, text="*", foreground="red")
label_client_name_error.grid(row=0, column=2, padx=5, pady=2)
label_client_name_error.grid_remove()

label_client_number = ttk.Label(frame, text="Kliento Numeris:")
label_client_number.grid(row=1, column=0, padx=10, pady=2, sticky="w")
entry_client_number = tk.Entry(frame, width=40, font=("Arial", 10))
entry_client_number.grid(row=1, column=1, padx=5, pady=2, ipady=2)
label_client_number_error = ttk.Label(frame, text="*", foreground="red")
label_client_number_error.grid(row=1, column=2, padx=5, pady=2)
label_client_number_error.grid_remove()

label_company_code = ttk.Label(frame, text="Įmonės Kodas:")
label_company_code.grid(row=2, column=0, padx=10, pady=2, sticky="w")
entry_company_code = tk.Entry(frame, width=40, font=("Arial", 10))
entry_company_code.grid(row=2, column=1, padx=5, pady=2, ipady=2)
label_company_code_error = ttk.Label(frame, text="*", foreground="red")
label_company_code_error.grid(row=2, column=2, padx=5, pady=2)
label_company_code_error.grid_remove()

label_start_km = ttk.Label(frame, text="Pradinis KM:")
label_start_km.grid(row=3, column=0, padx=10, pady=2, sticky="w")
entry_start_km = tk.Entry(frame, width=40, font=("Arial", 10))
entry_start_km.grid(row=3, column=1, padx=5, pady=2, ipady=2)
label_start_km_error = ttk.Label(frame, text="*", foreground="red")
label_start_km_error.grid(row=3, column=2, padx=5, pady=2)
label_start_km_error.grid_remove()

label_end_km = ttk.Label(frame, text="Galutinis KM:")
label_end_km.grid(row=4, column=0, padx=10, pady=2, sticky="w")
entry_end_km = tk.Entry(frame, width=40, font=("Arial", 10))
entry_end_km.grid(row=4, column=1, padx=5, pady=2, ipady=2)
label_end_km_error = ttk.Label(frame, text="*", foreground="red")
label_end_km_error.grid(row=4, column=2, padx=5, pady=2)
label_end_km_error.grid_remove()

label_day_price = ttk.Label(frame, text="Dienos Kaina:")
label_day_price.grid(row=5, column=0, padx=10, pady=2, sticky="w")
entry_day_price = tk.Entry(frame, width=40, font=("Arial", 10))
entry_day_price.grid(row=5, column=1, padx=5, pady=2, ipady=2)
label_day_price_error = ttk.Label(frame, text="*", foreground="red")
label_day_price_error.grid(row=5, column=2, padx=5, pady=2)
label_day_price_error.grid_remove()

label_days = ttk.Label(frame, text="Dienų Skaičius:")
label_days.grid(row=6, column=0, padx=10, pady=2, sticky="w")
entry_days = tk.Entry(frame, width=40, font=("Arial", 10))
entry_days.grid(row=6, column=1, padx=5, pady=2, ipady=2)
label_days_error = ttk.Label(frame, text="*", foreground="red")
label_days_error.grid(row=6, column=2, padx=5, pady=2)
label_days_error.grid_remove()

label_car_model = ttk.Label(frame, text="Automobilio Modelis:")
label_car_model.grid(row=7, column=0, padx=10, pady=2, sticky="w")
car_model_var = tk.StringVar()
combo_car_model = ttk.Combobox(frame, textvariable=car_model_var, values=["VW Tiguan", "VW Jetta", "VW Crafter", "Toyota Corolla"], state="readonly", width=37, font=("Arial", 10))
combo_car_model.grid(row=7, column=1, padx=5, pady=2)
label_car_model_error = ttk.Label(frame, text="*", foreground="red")
label_car_model_error.grid(row=7, column=2, padx=5, pady=2)
label_car_model_error.grid_remove()

label_discount = ttk.Label(frame, text="Nuolaida:")
label_discount.grid(row=8, column=0, padx=10, pady=2, sticky="w")
discount_var = tk.StringVar()
combo_discount = ttk.Combobox(frame, textvariable=discount_var, values=["Nėra", "10% Nuolaida", "20% Nuolaida"], state="readonly", width=37, font=("Arial", 10))
combo_discount.grid(row=8, column=1, padx=5, pady=2)

label_comments = ttk.Label(frame, text="Komentarai:")
label_comments.grid(row=9, column=0, padx=10, pady=2, sticky="w")
entry_comments = tk.Text(frame, width=40, height=4, font=("Arial", 10))
entry_comments.grid(row=9, column=1, padx=5, pady=2, ipady=2)

# Buttons
button_save = ttk.Button(frame, text="Išsaugoti", command=calculate_rental)
button_save.grid(row=11, column=0, padx=10, pady=10, sticky="e")

button_export = ttk.Button(frame, text="Eksportuoti į CSV", command=export_to_csv)
button_export.grid(row=11, column=1, padx=10, pady=10, sticky="w")

app.mainloop()
