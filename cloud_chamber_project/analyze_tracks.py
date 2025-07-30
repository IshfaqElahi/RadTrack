import cv2
import numpy as np
import pandas as pd
from tkinter import Tk, filedialog, messagebox

# === Image Upload Dialog ===
def upload_img_dialog():
    root = Tk()
    root.withdraw()  # Hide main window
    messagebox.showinfo("Upload", "Please upload the picture you want to analyze.")
    file_path = filedialog.askopenfilename(
        title="Select image for analysis",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tif;*.tiff")]
    )
    root.destroy()
    return file_path

# === Load Excel Data ===
df = pd.read_excel("sources.xlsx")

# Normalize for comparison
df['Source'] = df['Source (Isotope)'].str.extract(r'([A-Za-z0-9\-]+)').iloc[:, 0].str.strip().str.lower()
df['Emissions'] = df['Main Emitted Particle(s)'].str.lower().str.replace(r'[^\w, ]', '', regex=True).str.split(',')

# === User Input Section ===
user_source = input("Enter the source used in the image (e.g., Sr-90): ").strip().lower()
user_emission = input("Enter the main emitted particle (e.g., beta): ").strip().lower()

# === Check Validity ===
match = df[df['Source'] == user_source]
if match.empty or user_emission not in [e.strip() for e in match['Emissions'].values[0]]:
    print("❌ Error: Please check your source or emission type. They do not match the known data.")
    exit()

print("✅ Source and emission validated.")

# === Image Upload Popup ===
image_path = upload_img_dialog()
if not image_path:
    print("❌ No image selected. Exiting.")
    exit()
print("Analyzing...")

# === Image Processing ===
image = cv2.imread(image_path)
if image is None:
    print(f"❌ Error: Could not load image '{image_path}'")
    exit()

output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Color codes
colors = {"alpha": (0, 0, 255), "beta": (0, 255, 0), "muon": (255, 0, 255)}

# Classify and draw
for contour in contours:
    area = cv2.contourArea(contour)
    length = cv2.arcLength(contour, False)
    if area > 150:
        label = "alpha"
    elif 50 < area <= 150:
        label = "beta"
    elif area <= 50 and length > 100:
        label = "muon"
    else:
        continue
    cv2.drawContours(output, [contour], -1, colors[label], 2)

# Legend box
cv2.rectangle(output, (10, 10), (270, 120), (30, 30, 30), -1)
cv2.putText(output, "Legend (Approx)", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
cv2.putText(output, "Alpha - Red", (15, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.55, colors["alpha"], 2)
cv2.putText(output, "Beta  - Green", (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.55, colors["beta"], 2)
cv2.putText(output, "Muon  - Magenta", (15, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.55, colors["muon"], 2)

# Save & Show
combined = cv2.hconcat([image, output])
cv2.imwrite("tracks_comparison.jpg", combined)
print("✅ Saved: tracks_comparison.jpg")

cv2.imshow("Original vs Detected Tracks", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
