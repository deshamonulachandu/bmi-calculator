import tkinter as tk
import csv
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x350")

history = []

try:
    with open("bmi_history.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            history.append(row)

except FileNotFoundError:
    try:
        with open("bmi_history.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "BMI", "Category"])
    except OSError:
        print("Error: Unable to create BMI history file.")


title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

name_label = tk.Label(root, text="Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.pack(pady=5)

height_entry = tk.Entry(root)
height_entry.pack(pady=5)


def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            result_label.config(text="Please enter positive values.")
            return

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        if category == "Normal":
            result_color = "green"
        elif category == "Obese":
            result_color = "red"
        elif category == "Overweight":
            result_color = "orange"
        else:
            result_color = "blue"

        result_label.config(
             text=name + "'s BMI is: " + str(bmi) +
             "\nCategory: " + category,
             fg=result_color
)
        record = name + " - BMI: " + str(bmi) + " - " + category

        history.append([name, str(bmi), category])

        try:
            with open("bmi_history.csv", "a", newline="") as file:
               writer = csv.writer(file)
               writer.writerow([name, bmi, category])
        except OSError:
            result_label.config(
        text="Error: Unable to save BMI history.",
        fg="red"
    )
    except ValueError:
        result_label.config(text="Please enter numbers only.")


def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
def show_graph():
    if len(history) == 0:
        result_label.config(text="No BMI history available.")
        return

    names = []
    bmi_values = []

    for record in history:
        names.append(record[0])
        bmi_values.append(float(record[1]))

    plt.figure(figsize=(7, 4))
    plt.plot(names, bmi_values, marker="o")

    plt.title("BMI Trend")
    plt.xlabel("Name")
    plt.ylabel("BMI")

    plt.axhline(y=18.5, linestyle="--")
    plt.axhline(y=25, linestyle="--")
    plt.axhline(y=30, linestyle="--")

    plt.tight_layout()
    plt.show()
def view_history():
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("400x300")

    if len(history) == 0:
        history_label = tk.Label(
            history_window,
            text="No BMI history available."
        )
        history_label.pack(pady=20)

    else:
        for record in history:
            name = record[0]
            bmi = record[1]
            category = record[2]

            history_label = tk.Label(
                history_window,
                text=name + " - BMI: " + bmi + " - " + category,
                font=("Arial", 11)
            )
            history_label.pack(pady=5)


calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=5
)
calculate_button.pack()

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=5
)
clear_button.pack(pady=10)
history_button = tk.Button(
    root,
    text="View History",
    command=view_history,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=5
)
history_button.pack(pady=10)
graph_button = tk.Button(
    root,
    text="Show BMI Graph",
    command=show_graph,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=5
)
graph_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold")
)
result_label.pack()

root.mainloop()