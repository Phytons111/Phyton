import tkinter as tk
import random

def open_converter():
    window = tk.Toplevel(root)
    window.title("Seconds, Minutes and Hours")
    window.geometry("600x600")

    label = tk.Label(window, text="Result will appear here", font=("Arial", 20))
    label.pack(pady=20)

    entry = tk.Entry(window, font=("Arial", 16))
    entry.pack(pady=20)

    def hours_to_minutes(x): return x * 60
    def hours_to_seconds(x): return x * 3600
    def minutes_to_hours(x): return x / 60
    def minutes_to_seconds(x): return x * 60
    def seconds_to_hours(x): return x / 3600
    def seconds_to_minutes(x): return x / 60
    def years_to_days(x): return x * 365
    def days_to_years(x): return x / 365
    def years_to_months(x): return x * 12
    def months_to_years(x): return x / 12
    def months_to_days(x): return x * 30
    def days_to_months(x): return x / 30

    last = {"func": None, "desc": ""}

    def set_conv(f, d):
        last["func"] = f
        last["desc"] = d
        label.config(text=f"Selected: {d}")

    def calculate():
        try:
            v = float(entry.get())
            r = last["func"](v)
            label.config(text=f"{v} {last['desc']} = {r}")
        except:
            label.config(text="Error")

    def reset():
        entry.delete(0, tk.END)
        label.config(text="Result will appear here")
        last["func"] = None
        last["desc"] = ""

    left = tk.Frame(window)
    left.pack(side="left", padx=40, pady=20)

    right = tk.Frame(window)
    right.pack(side="right", padx=40, pady=20)

    tk.Button(left, text="Hours → Minutes", command=lambda: set_conv(hours_to_minutes, "hours to minutes"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(left, text="Hours → Seconds", command=lambda: set_conv(hours_to_seconds, "hours to seconds"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(left, text="Minutes → Hours", command=lambda: set_conv(minutes_to_hours, "minutes to hours"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(left, text="Minutes → Seconds", command=lambda: set_conv(minutes_to_seconds, "minutes to seconds"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(left, text="Seconds → Hours", command=lambda: set_conv(seconds_to_hours, "seconds to hours"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(left, text="Seconds → Minutes", command=lambda: set_conv(seconds_to_minutes, "seconds to minutes"), font=("Arial", 14), width=18).pack(pady=5)

    tk.Button(right, text="Years → Days", command=lambda: set_conv(years_to_days, "years to days"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(right, text="Days → Years", command=lambda: set_conv(days_to_years, "days to years"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(right, text="Years → Months", command=lambda: set_conv(years_to_months, "years to months"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(right, text="Months → Years", command=lambda: set_conv(months_to_years, "months to years"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(right, text="Months → Days", command=lambda: set_conv(months_to_days, "months to days"), font=("Arial", 14), width=18).pack(pady=5)
    tk.Button(right, text="Days → Months", command=lambda: set_conv(days_to_months, "days to months"), font=("Arial", 14), width=18).pack(pady=5)

    tk.Button(window, text="Calculate", command=calculate, font=("Arial", 16), bg="lightblue", width=20).pack(pady=20)
    tk.Button(window, text="Reset", command=reset, font=("Arial", 16), bg="lightcoral", width=20).pack(pady=10)


def open_calculator():
    calc = tk.Toplevel(root)
    calc.title("Calculator")
    calc.geometry("300x400")

    entry = tk.Entry(calc, font=("Arial", 24), justify="right")
    entry.pack(fill="both", padx=10, pady=10)

    def add(c): entry.insert(tk.END, c)
    def clear(): entry.delete(0, tk.END)
    def calc_res():
        try:
            r = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, r)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    frame = tk.Frame(calc)
    frame.pack()

    buttons = ["7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]

    row = col = 0
    for b in buttons:
        cmd = calc_res if b == "=" else lambda x=b: add(x)
        tk.Button(frame, text=b, width=5, height=2, font=("Arial", 18), command=cmd).grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col == 4:
            col = 0
            row += 1

    tk.Button(calc, text="Clear", command=clear, font=("Arial", 16), bg="lightcoral").pack(fill="x", padx=10, pady=10)


def open_game_01():
    window = tk.Toplevel(root)
    window.title("Please 1!")
    window.geometry("600x700")

    status_label = tk.Label(window, text="", font=("Arial", 20))
    status_label.pack(pady=10)

    score = 0
    score_label = tk.Label(window, text=f"Score: {score}", font=("Arial", 16))
    score_label.pack(pady=5)

    grid_frame = tk.Frame(window)
    grid_frame.pack(pady=20)

    text_vars = []
    buttons = []
    grid_values = [random.choice([0, 1]) for _ in range(25)]

    def disable_buttons():
        for btn in buttons:
            btn.config(state="disabled")

    def klikni(btn_text, btn, index):
        nonlocal score
        if btn_text.get() != "":
            return
        new_val = random.choice([0, 1])
        btn_text.set(str(new_val))
        if new_val == 0:
            status_label.config(text="❌ You lost!")
            for i, (t, b) in enumerate(zip(text_vars, buttons)):
                if t.get() == "":
                    t.set(str(grid_values[i]))
                    b.config(bg="yellow")
            disable_buttons()
        else:
            score += 1
            score_label.config(text=f"Score: {score}")
            if score == sum(1 for v in grid_values if v == 1):
                status_label.config(text="🏆 You won!")
                disable_buttons()

    def reset():
        nonlocal grid_values, score
        grid_values = [random.choice([0, 1]) for _ in range(25)]
        score = 0
        score_label.config(text=f"Score: {score}")
        for btn_text, btn in zip(text_vars, buttons):
            btn_text.set("")
            btn.config(state="normal", bg="SystemButtonFace")
        status_label.config(text="")

    for r in range(5):
        for c in range(5):
            index = r * 5 + c
            btn_text = tk.StringVar()
            btn_text.set("")
            text_vars.append(btn_text)

            frame = tk.Frame(grid_frame, width=60, height=60)
            frame.grid(row=r, column=c, padx=5, pady=5)
            frame.pack_propagate(False)

            btn = tk.Button(frame, textvariable=btn_text,
                            command=lambda t=btn_text, i=index: klikni(t, buttons[i], i))
            btn.pack(fill="both", expand=True)

            buttons.append(btn)

    tk.Button(window, text="Reset", command=reset, font=("Arial", 14)).pack(pady=20)


def open_coin_game():
    game = tk.Toplevel(root)
    game.title("Coin Game")

    stav = 50
    history = []

    label = tk.Label(game, text="You start at 50", font=("Arial", 14))
    label.pack(pady=10)

    canvas = tk.Canvas(game, width=180, height=120)
    canvas.pack()

    history_label = tk.Label(game, text="History: -", font=("Arial", 12), wraplength=300, justify="left")
    history_label.pack(pady=5)

    def flip():
        nonlocal stav, history
        coin = random.choice([-10, 10])
        stav += coin
        history.append(coin)
        canvas.delete("all")
        canvas.create_oval(20, 20, 160, 160, fill="yellow")
        canvas.create_text(90, 50, text=f"Flip: {coin}", font=("Arial", 14, "bold"))
        canvas.create_text(90, 75, text=f"Score: {stav}", font=("Arial", 12))
        if stav <= 0:
            label.config(text="You skipped school!")
            button.config(state="disabled")
            reset_button.config(state="normal")
        elif stav >= 100:
            label.config(text="You attended class!")
            button.config(state="disabled")
            reset_button.config(state="normal")
        else:
            label.config(text="Continue...")
        history_label.config(text="History: " + ", ".join(map(str, history)))

    def reset():
        nonlocal stav, history
        stav = 50
        history = []
        label.config(text="You start at 50")
        history_label.config(text="History: -")
        button.config(state="normal")
        reset_button.config(state="disabled")
        canvas.delete("all")

    button = tk.Button(game, text="Flip", command=flip, font=("Arial", 14))
    button.pack(pady=5)

    reset_button = tk.Button(game, text="Reset", command=reset, font=("Arial", 14), bg="lightcoral", width=10, state="disabled")
    reset_button.pack(pady=5)


root = tk.Tk()
root.title("Assistant")
root.geometry("400x500")

menu_frame = tk.Frame(root)
menu_frame.pack(side="left", anchor="nw", padx=20, pady=20)

tk.Button(menu_frame, text="Seconds, minutes and hours", command=open_converter, font=("Arial", 18), width=24, height=2).pack(pady=10, anchor="w")
tk.Button(menu_frame, text="Calculator", command=open_calculator, font=("Arial", 18), width=12, height=2).pack(pady=10, anchor="w")
tk.Button(menu_frame, text="Please 1!", command=open_game_01, font=("Arial", 18), width=12, height=2).pack(pady=10, anchor="w")
tk.Button(menu_frame, text="Coin Game", command=open_coin_game, font=("Arial", 18), width=12, height=2).pack(pady=10, anchor="w")

root.mainloop()
