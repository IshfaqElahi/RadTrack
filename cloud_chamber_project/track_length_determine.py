import cv2
import numpy as np
from tkinter import Tk, filedialog
from PIL import Image, ImageDraw, ImageFont
import os

def add_legend(image):
    legend_height = 100
    legend_width = image.shape[1]  # match image width

    # Create a white canvas for the legend
    legend_img = Image.new("RGB", (legend_width, legend_height), "white")
    draw = ImageDraw.Draw(legend_img)

    # Use custom font if available
    font_path = "times.ttf"
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, 18)
    else:
        font = ImageFont.load_default()

    draw.text((10, 10), "Legend:", font=font, fill="black")
    draw.text((20, 40), "Alpha: Blue", font=font, fill="blue")
    draw.text((170, 40), "Beta: Green", font=font, fill="green")
    draw.text((320, 40), "Muon: Red", font=font, fill="red")

    legend_array = np.array(legend_img)
    return np.vstack((image, legend_array))

def calculate_length_in_mm(pixel_length, pixel_per_mm=10):
    return pixel_length / pixel_per_mm

def classify_track(length_mm):
    if length_mm < 5:
        return "alpha", (255, 0, 0)  # Blue
    elif length_mm < 15:
        return "beta", (0, 255, 0)  # Green
    else:
        return "muon", (0, 0, 255)  # Red

def main():
    # Open file dialog to select image
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])

    if not file_path:
        print("No file selected.")
        return

    image = cv2.imread(file_path)
    if image is None:
        print("Failed to load the image.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = image.copy()
    for cnt in contours:
        if cv2.contourArea(cnt) > 50:
            length = cv2.arcLength(cnt, True)
            length_mm = calculate_length_in_mm(length)

            track_type, color = classify_track(length_mm)
            cv2.drawContours(output, [cnt], -1, color, 2)

            # Label each track with its length in mm
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                label = f"{length_mm:.1f} mm"
                cv2.putText(output, label, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Add legend
    final_output = add_legend(output)

    # Save output
    output_filename = "radiation_tracks_annotated.jpg"
    cv2.imwrite(output_filename, final_output)
    print(f"✅ Saved: {output_filename}")

if __name__ == "__main__":
    main()
