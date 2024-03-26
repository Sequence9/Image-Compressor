import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageCompressor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Compressor")
        self.geometry("400x400")
        self.resizable(False, False)

        self.input_image = None
        self.compressed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Select Image button
        select_button = tk.Button(self, text="Select Image", command=self.select_image)
        select_button.pack(pady=10)

        # Compression Algorithm dropdown
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("JPEG")
        algorithm_label = tk.Label(self, text="Compression Algorithm:")
        algorithm_label.pack()
        algorithm_dropdown = tk.OptionMenu(self, self.algorithm_var, "JPEG", "PNG", "WebP")
        algorithm_dropdown.pack()

        # Compression Quality slider
        self.quality_var = tk.DoubleVar()
        self.quality_var.set(90)
        quality_label = tk.Label(self, text="Compression Quality:")
        quality_label.pack()
        quality_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.quality_var)
        quality_slider.pack()

        # Compress button
        compress_button = tk.Button(self, text="Compress", command=self.compress_image)
        compress_button.pack(pady=10)

        # Image preview
        self.preview_label = tk.Label(self)
        self.preview_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
        if file_path:
            self.input_image = Image.open(file_path)
            self.update_preview()

    def compress_image(self):
        if self.input_image is None:
            messagebox.showerror("Error", "Please select an image first.")
            return

        quality = int(self.quality_var.get())
        algorithm = self.algorithm_var.get().lower()

        try:
            if algorithm == "jpeg":
                self.compressed_image = self.input_image.copy()
                self.compressed_image.save("compressed_image.jpg", format="JPEG", quality=quality)
            elif algorithm == "png":
                self.compressed_image = self.input_image.copy()
                self.compressed_image.save("compressed_image.png", format="PNG", optimize=True)
            elif algorithm == "webp":
                self.compressed_image = self.input_image.copy()
                self.compressed_image.save("compressed_image.webp", format="WebP", quality=quality)

            messagebox.showinfo("Success", "Image compressed successfully!")
            self.update_preview()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_preview(self):
        if self.compressed_image is not None:
            preview_image = self.compressed_image.copy()
        elif self.input_image is not None:
            preview_image = self.input_image.copy()
        else:
            return

        preview_image.thumbnail((300, 300))
        preview_photo = ImageTk.PhotoImage(preview_image)
        self.preview_label.configure(image=preview_photo)
        self.preview_label.image = preview_photo

if __name__ == "__main__":
    app = ImageCompressor()
    app.mainloop()