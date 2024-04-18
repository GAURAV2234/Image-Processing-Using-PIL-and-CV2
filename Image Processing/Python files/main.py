import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import cv2
import numpy as np
from operations import *

def process_image(option, input_image_path):
    input_image = cv2.imread(input_image_path)

    if input_image is None:
        messagebox.showerror("Error", "Failed to load the input image.")
        return None, ""

    if option == 'Convert to Grayscale':
        processed_image = convert_to_grayscale(input_image_path)
        suffix = "_grayscale"
    elif option == 'Perform Edge Detection':
        processed_image = detect_edges(input_image_path)
        suffix = "_edge_detected"
    elif option == 'Enhance Image':
        processed_image = enhance_image(input_image_path)
        suffix = "_enhanced"
    elif option == 'Smooth Image':
        processed_image = smooth_image(input_image_path)
        suffix = "_smooth"
    elif option == 'Adjust Contrast':
        processed_image = adjust_contrast(input_image_path)
        suffix = "_contrast_adjusted"
    elif option == 'Denoise Image':
        processed_image = denoise_image(input_image_path)
        suffix = "_denoised"
    elif option == 'Deblur Image (Enhanced)':
        processed_image = deblur_image_enhanced(input_image_path)
        suffix = "_deblurred_enhanced"
    elif option == 'Histogram Equalization':
        processed_image = histogram_equalization(input_image_path)
        suffix = "_histogram_equalized"
    elif option == 'Sharpen Image (Enhanced)':
        processed_image = sharpen_image_enhanced(input_image_path)
        suffix = "_sharpened_enhanced"
    else:
        messagebox.showerror("Error", "Invalid operation selected.")
        return None, ""

    return processed_image, suffix


def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def save_image(output_image, suffix):
    output_directory = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if output_directory:
        output_image.save(output_directory)
        messagebox.showinfo("Success", f"Image saved as {output_directory}")

def execute_operation():
    input_image_path = input_entry.get()
    if not os.path.isfile(input_image_path):
        messagebox.showerror("Error", "Please select a valid image file.")
        return

    option = operation_combobox.get()
    output_image, suffix = process_image(option, input_image_path)
    if output_image is not None:
        save_image(output_image, suffix)

app = tk.Tk()
app.title("Image Processing App")

window_width = 600
window_height = 200
app.geometry(f"{window_width}x{window_height}")
app.configure(bg='white')

input_frame = ttk.Frame(app)
input_frame.pack(padx=10, pady=5, fill='x', expand=True)

input_label = ttk.Label(input_frame, text="Input Image:", background='white', foreground='black')
input_label.pack(side=tk.LEFT, padx=(0, 10))

input_entry = ttk.Entry(input_frame)
input_entry.pack(side=tk.LEFT, expand=True, fill='x')

select_button = ttk.Button(input_frame, text="Select", command=select_image)
select_button.pack(side=tk.LEFT, padx=(10, 0))

operation_frame = ttk.Frame(app)
operation_frame.pack(padx=10, pady=5, fill='x', expand=True)

operation_label = ttk.Label(operation_frame, text="Operation:", background='white', foreground='black')
operation_label.pack(side=tk.LEFT, padx=(0, 10))

operation_options = ['Convert to Grayscale', 'Perform Edge Detection', 'Enhance Image', 'Smooth Image', 'Adjust Contrast', 'Denoise Image', 'Deblur Image (Enhanced)', 'Histogram Equalization', 'Sharpen Image (Enhanced)']
operation_combobox = ttk.Combobox(operation_frame, values=operation_options, state="readonly")
operation_combobox.current(0)
operation_combobox.pack(side=tk.LEFT, expand=True, fill='x')

execute_button = ttk.Button(app, text="Execute", command=execute_operation)
execute_button.pack(pady=10)

app.mainloop()
