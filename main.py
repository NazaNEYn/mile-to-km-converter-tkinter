from tkinter import *

BG_COLOR = "#f0f0f0"
ACCENT_COLOR = "#2a628f"

window = Tk()
window.title("Mile to Km Converter")
window.config(pady=50, padx=80, bg=BG_COLOR)

# Configure columns 0 and 2 to absorb extra space for better centering
window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=1)


def miles_to_km(event=None):
    """
    Converts miles to kilometers and updates the output label.

    Handles ValueError exceptions if the user enters non-numeric input.
    """
    try:
        miles = float(entry.get())
        km = miles * 1.60934
        label_convert.config(text=f"{km:.2f}", fg="darkgreen")
    except ValueError:
        label_convert.config(text="ERROR", fg="red")


window.bind("<Return>", miles_to_km)
# --- WIDGETS ---

# Entry Box (Input)
entry = Entry(width=10, font=("Helvetica", 12))
entry.grid(column=1, row=0)

# "Miles" Label
label_miles = Label(text="Miles", font=("Helvetica", 12), bg=BG_COLOR)
label_miles.grid(column=2, row=0)

# "Is equal to" Label
label_equal = Label(text="Is equal to", font=("Helvetica", 12), bg=BG_COLOR)
label_equal.grid(column=0, row=1, pady=10, sticky="e")

# Output Label
label_convert = Label(
    text="0",
    font=("Helvetica", 14, "bold"),
    width=8,
    bg="white",
    fg="darkgreen",
)
label_convert.grid(column=1, row=1, padx=10, pady=10, sticky="w")

# "Km" Label
label_km = Label(text="Km", font=("Helvetica", 12), bg=BG_COLOR)
label_km.grid(column=2, row=1)


# Button
button = Button(
    text="Calculate",
    command=miles_to_km,
    font=("Helvetica", 12, "bold"),
    bg=ACCENT_COLOR,
    fg="white",
    relief="flat",  # A flatter look is often considered more modern
)
button.grid(column=1, row=2, pady=15)

window.mainloop()
