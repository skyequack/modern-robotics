# Only for use with rotational spatial joints

import tkinter as tk
from tkinter import ttk
import numpy as np

class ScrewAxisCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screw Axis Calculator")
        self.root.geometry("600x300")  # Set initial window size
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding=(20, 10))
        self.main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Position vector inputs
        self.position_label = ttk.Label(self.main_frame, text="Position Vector:")
        self.position_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.position_x_label = ttk.Label(self.main_frame, text="X:")
        self.position_x_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
        self.position_x_entry = ttk.Entry(self.main_frame, width=8, font=('Arial', 12))
        self.position_x_entry.grid(row=0, column=2, padx=5, pady=5)

        self.position_y_label = ttk.Label(self.main_frame, text="Y:")
        self.position_y_label.grid(row=0, column=3, padx=5, pady=5, sticky=tk.E)
        self.position_y_entry = ttk.Entry(self.main_frame, width=8, font=('Arial', 12))
        self.position_y_entry.grid(row=0, column=4, padx=5, pady=5)

        self.position_z_label = ttk.Label(self.main_frame, text="Z:")
        self.position_z_label.grid(row=0, column=5, padx=5, pady=5, sticky=tk.E)
        self.position_z_entry = ttk.Entry(self.main_frame, width=8, font=('Arial', 12))
        self.position_z_entry.grid(row=0, column=6, padx=5, pady=5)

        # Axis of rotation selection
        self.axis_label = ttk.Label(self.main_frame, text="Axis of Rotation:")
        self.axis_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.axis_var = tk.StringVar()
        self.axis_var.set("X")  # Default selection

        self.axis_options = ttk.OptionMenu(self.main_frame, self.axis_var, "X", "X", "Y", "Z")
        self.axis_options.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.calculate_button = ttk.Button(self.main_frame, text="Calculate Screw Axis", command=self.calculate_screw_axis)
        self.calculate_button.grid(row=2, columnspan=7, padx=10, pady=15)

        self.result_label = ttk.Label(self.main_frame, text="Screw Axis:")
        self.result_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.result_text = tk.Text(self.main_frame, height=4, width=30, font=('Arial', 12))
        self.result_text.grid(row=3, column=1, columnspan=6, padx=10, pady=5, sticky=tk.W)

    def calculate_screw_axis(self):
        try:
            # Get position vector
            position_x = float(self.position_x_entry.get().strip())
            position_y = float(self.position_y_entry.get().strip())
            position_z = float(self.position_z_entry.get().strip())
            position = [position_x, position_y, position_z]

            # Get axis of rotation
            axis_selection = self.axis_var.get()
            axis_of_rotation = [1.0 if axis_selection == 'X' else 0.0,
                                1.0 if axis_selection == 'Y' else 0.0,
                                1.0 if axis_selection == 'Z' else 0.0]

            # Calculate screw axis
            screw_axis = self._calculate_screw_axis(position, axis_of_rotation)

            # Display result
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, self.format_screw_axis(screw_axis))

        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Error: Please enter valid numeric values.")

    def _calculate_screw_axis(self, position, axis_of_rotation):
        position = np.array(position)
        axis_of_rotation = np.array(axis_of_rotation)

        axis_of_rotation /= np.linalg.norm(axis_of_rotation)

        screw_axis = np.hstack((axis_of_rotation, np.cross(position, axis_of_rotation)))

        return screw_axis.tolist()

    def format_screw_axis(self, screw_axis):
        # Format the screw axis for display
        formatted_axis = ", ".join(f"{val:.4f}" for val in screw_axis)
        return formatted_axis


def main():
    root = tk.Tk()
    app = ScrewAxisCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
