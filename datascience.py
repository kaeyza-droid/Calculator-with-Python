import tkinter as tk
import math

# -----------------------------
# Fungsi untuk perhitungan
# -----------------------------
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = screen.get()
            # Ganti simbol agar bisa dieksekusi Python
            expression = expression.replace("^", "**")
            expression = expression.replace("√", "math.sqrt")
            expression = expression.replace("π", "math.pi")
            expression = expression.replace("e", "math.e")

            # Perhitungan ilmiah
            result = eval(expression)
            screen.set(round(result, 10))
        except Exception:
            screen.set("Error")

    elif text == "C":
        screen.set("")
    elif text == "⌫":
        screen.set(screen.get()[:-1])
    elif text == "sin":
        try:
            val = float(screen.get())
            if mode.get() == "DEG":
                val = math.radians(val)
            screen.set(round(math.sin(val), 10))
        except:
            screen.set("Error")
    elif text == "cos":
        try:
            val = float(screen.get())
            if mode.get() == "DEG":
                val = math.radians(val)
            screen.set(round(math.cos(val), 10))
        except:
            screen.set("Error")
    elif text == "tan":
        try:
            val = float(screen.get())
            if mode.get() == "DEG":
                val = math.radians(val)
            screen.set(round(math.tan(val), 10))
        except:
            screen.set("Error")
    elif text == "log":
        try:
            val = float(screen.get())
            screen.set(round(math.log10(val), 10))
        except:
            screen.set("Error")
    elif text == "ln":
        try:
            val = float(screen.get())
            screen.set(round(math.log(val), 10))
        except:
            screen.set("Error")
    elif text == "Rad/Deg":
        if mode.get() == "RAD":
            mode.set("DEG")
        else:
            mode.set("RAD")
    else:
        screen.set(screen.get() + text)

# -----------------------------
# Tampilan GUI
# -----------------------------
root = tk.Tk()
root.title("Kalkulator Ilmiah Python")
root.geometry("420x650")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

mode = tk.StringVar(value="DEG")  # Mode: DEG / RAD
screen = tk.StringVar()

entry = tk.Entry(
    root, textvar=screen, font=("Consolas", 26),
    bg="#2b2b2b", fg="white", bd=10, relief=tk.FLAT, justify="right"
)
entry.pack(fill=tk.X, ipadx=8, pady=20, padx=10)

# Mode tampilan di atas
mode_label = tk.Label(root, textvariable=mode, bg="#1e1e1e", fg="#00ffae", font=("Consolas", 12))
mode_label.pack(anchor="e", padx=20)

# -----------------------------
# Tombol kalkulator
# -----------------------------
button_texts = [
    ["C", "⌫", "(", ")", "/"],
    ["7", "8", "9", "*", "%"],
    ["4", "5", "6", "-", "^"],
    ["1", "2", "3", "+", "="],
    ["0", ".", "√(", "π", "e"],
    ["sin", "cos", "tan", "log", "ln"],
    ["Rad/Deg"]
]

for row in button_texts:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for text in row:
        b = tk.Button(
            frame, text=text,
            font=("Consolas", 18, "bold"),
            bg="#3c3f41", fg="white",
            activebackground="#0078D7", activeforeground="white",
            relief=tk.FLAT, padx=10, pady=15
        )
        b.pack(side=tk.LEFT, expand=True, fill="both")
        b.bind("<Button-1>", click)

# -----------------------------
# Jalankan aplikasi
# -----------------------------
root.mainloop()
