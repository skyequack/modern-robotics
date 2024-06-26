import tkinter as tk

def get_values():
    values = []
    for i in range(6):
        row_values = []
        for j in range(6):
            row_values.append(entry_boxes[i*6 + j].get())
        values.append(row_values)
    print(values)

root = tk.Tk()
root.title("Grid of Input Boxes")

# Create 36 entry boxes in a 6x6 grid
entry_boxes = []
for i in range(6):
    for j in range(6):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j, padx=5, pady=5)
        entry_boxes.append(entry)

# Button to get values
btn_get_values = tk.Button(root, text="Get Values", command=get_values)
btn_get_values.grid(row=6, columnspan=6, pady=10)

root.mainloop()
