# Image Compressor

Image Compressor is a small desktop GUI built with Python, Tkinter, and Pillow. Select an image, choose JPEG, PNG, or WebP output, adjust the quality setting, and preview the result.

## Features

- Select an image from the local file system
- Export as JPEG, PNG, or WebP
- Adjust JPEG and WebP quality with a slider
- Preview the selected or compressed image
- Safely convert transparent and palette images when exporting to JPEG

## Requirements

- Python 3
- Tkinter (included with most standard Python installations)
- Pillow

## Installation

```bash
git clone https://github.com/Sequence9/Image-Compressor.git
cd Image-Compressor
python -m pip install Pillow
```

## Run

Because the script filename contains a space, quote it when launching from a terminal:

```bash
python "Image Compressor.py"
```

## Usage

1. Click **Select Image** and choose a JPEG, PNG, or BMP file.
2. Choose the output format.
3. Set the desired quality for JPEG or WebP.
4. Click **Compress**.

The result is written to the current working directory as `compressed_image.jpg`, `compressed_image.png`, or `compressed_image.webp`. Running another compression with the same format replaces the previous output.
