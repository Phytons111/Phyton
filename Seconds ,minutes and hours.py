import tkinter as tk

window = tk.Tk()
window.title("⏰ Converter")
window.geometry("600x600")

label = tk.Label(window, text="Result will appear here", font=("Arial", 20))
label.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 16))
entry.pack(pady=20)

def hours_to_minutes(hour): return hour * 60
def hours_to_seconds(hour): return hour * 3600
def minutes_to_hours(minute): return minute / 60
def minutes_to_seconds(minute): return minute * 60
def seconds_to_hours(second): return second / 3600
def seconds_to_minutes(second): return second / 60

def years_to_days(years): return years * 365
def days_to_years(days): return days / 365
def years_to_months(years): return years * 12
def months_to_years(months): return months / 12
def months_to_days(months): return months * 30
def days_to_months(days): return days / 30

last_function = None
last_description = ""

def set_conversion(function, description):
    global last_function, last_description
    last_function = function
    last_description = description
    label.config(text=f"Selected: {description}")

def calculate():
    global last_function, last_description
    if last_function is None:
        label.config(text="Please select a conversion first!")
        return
    try:
        value = float(entry.get())
        result = last_function(value)
        label.config(text=f"{value} {last_description} = {result}")
    except ValueError:
        label.config(text="Please enter a number!")

def reset():
    global last_function, last_description
    entry.delete(0, tk.END)
    label.config(text="Result will appear here")
    last_function = None
    last_description = ""

tk.Button(window, text="Hours → Minutes",
          command=lambda: set_conversion(hours_to_minutes, "hours to minutes"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Hours → Seconds",
          command=lambda: set_conversion(hours_to_seconds, "hours to seconds"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Minutes → Hours",
          command=lambda: set_conversion(minutes_to_hours, "minutes to hours"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Minutes → Seconds",
          command=lambda: set_conversion(minutes_to_seconds, "minutes to seconds"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Seconds → Hours",
          command=lambda: set_conversion(seconds_to_hours, "seconds to hours"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Seconds → Minutes",
          command=lambda: set_conversion(seconds_to_minutes, "seconds to minutes"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Years → Days",
          command=lambda: set_conversion(years_to_days, "years to days"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Days → Years",
          command=lambda: set_conversion(days_to_years, "days to years"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Years → Months",
          command=lambda: set_conversion(years_to_months, "years to months"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Months → Years",
          command=lambda: set_conversion(months_to_years, "months to years"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Months → Days",
          command=lambda: set_conversion(months_to_days, "months to days"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Days → Months",
          command=lambda: set_conversion(days_to_months, "days to months"),
          font=("Arial", 14)).pack(pady=5)

tk.Button(window, text="Calculate", command=calculate, font=("Arial", 16), bg="lightblue").pack(pady=20)

tk.Button(window, text="Reset", command=reset, font=("Arial", 16), bg="lightcoral").pack(pady=10)

window.mainloop()