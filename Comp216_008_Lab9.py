import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import Canvas, messagebox

# Data Generator from Lab 6
class DataGenerator:
    def __init__(self):
        pass

    def _generate_random(self, n_samples):
        return np.random.rand(n_samples)

    @property
    def generated_data(self):
        n_samples = 20 # changed the number of samples to 20
        random_values = self._generate_random(n_samples)
        m = 21  # range of output values
        c = 18  # minimum value
        output = (m-c) * random_values + c
        return output

    def plot_data(self):
        data = self.generated_data
        fig, ax = plt.subplots(figsize=(40, 6))
        plt.plot(data)
        plt.title('Generated Data')
        plt.xlabel('Index')
        plt.ylabel('Temperature')
        plt.show()


# DisplayApp class
class DisplayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Temperature Display App")

        # Create a list of 20 values using the generator class
        self.value_generator = DataGenerator()
        self.values = self.value_generator.generated_data

        self.range = 0

        # Initialize the UI
        self.init_ui()

    def init_ui(self):
        # Create a canvas to draw the rectangles and lines
        self.canvas = Canvas(self.root, width=300, height=200, bg="white")
        # Create text input for data range
        self.entry_label = tk.Label(self.root, text="Data Range:")
        self.entry_label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.update_button = tk.Button(self.root, text="Update Data", command=self.update_data)
        self.update_button.pack()
        # show the data range
        self.range_label = tk.Label(self.root, text=f"Data Range: {self.range} - {self.range + 5}")
        self.range_label.pack()
        self.canvas.pack()

        # Draw the rectangles and lines
        self.draw_rectangles_and_lines()

    def update_data(self):
        self.canvas.delete("all")
        if int(self.entry.get()) < 0 or int(self.entry.get()) > 20:
            messagebox.showerror("Input Error", "Please enter a valid number between 0 and 20.")
            return
        self.range = int(self.entry.get())
        self.range_label.config(text=f"Data Range: {self.range} - {self.range + 5}")
        self.draw_rectangles_and_lines()

    def draw_rectangles_and_lines(self):
        # Implement drawing logic for rectangles and lines based on the values
        spacing = 10  # Spacing between rectangles
        rect_width = 25  # Width of each rectangle

        top_points = []

        for i in range(5):
            x_pos1 = 50 + i * (rect_width + spacing)
            x_pos2 = x_pos1 + rect_width

            # Draw the gauge background
            self.canvas.create_rectangle(x_pos1, 20, x_pos2, 200, fill="light grey")

            # Calculate the height of the vertical bar based on temperature
            bar_height = (self.values[self.range + i] - 18) / 3 * 180

            # Calculate the top y-coordinate of the rectangles
            rect_top_y = 200 - float(bar_height)

            # Draw the rectangles
            self.canvas.create_rectangle(x_pos1, rect_top_y, x_pos2, 200, fill="green")

            top_points.append((x_pos1 + rect_width/2, rect_top_y))

        # Draw the lines
        self.canvas.create_line(top_points, fill="red")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DisplayApp()
    app.run()
