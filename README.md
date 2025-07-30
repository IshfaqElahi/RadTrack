**🔬 radiation_track_detect**<br>
A heuristic image processing algorithm that detects and classifies radiation particle tracks — such as alpha, beta, and muon — from cloud chamber images. This project uses OpenCV for contour-based analysis and validates the source-emitter pair using an external Excel file.
<br>

**📌 Features**<br>
🖼️ Upload any cloud chamber image via a simple GUI.<br>
🧠 Classify tracks as alpha (red), beta (green), and muon (magenta) using contour area and shape heuristics.<br>
📄 Validate radiation source-emitter pair using a reference Excel file (sources.xlsx).<br>
🖍️ Visualizes results with labeled tracks and a legend.<br>
📸 Saves a side-by-side comparison of the original and processed image.<br>


**🧪 Example Use Case**<br>
You built a cloud chamber and took a photo of the tracks.<br>
You know the radioactive source used (e.g., Sr-90) and its emitted particle (e.g., Beta).<br>
You launch this tool, upload the image, and input the source and emitter.<br>
The tool verifies the input against the reference file.<br>
The program highlights tracks based on contour shape and size and saves the result.<br>

**📂 Project Structure**<br>
cloud_chamber_project/<br>
├── analyze_tracks.py<br>
├── sources.xlsx<br>
├── tracks_comparison.jpg<br>
└── README.md<br>


**🚀 How to Run**<br>
git clone: https://github.com/IshfaqElahi/radiation_track_detect.git<br>
cd radiationtrackdetect<br>

2. Create and activate a virtual environment (optional but recommended)<br>
python -m venv myenv<br>
myenv\Scripts\activate  # Windows<br>

3. Install dependencies<br>
pip install opencv-python pandas openpyxl numpy<br>

4. Run the main script<br>
python analyze_tracks.py<br>


**📥 Dependencies**<br>
  opencv-python<br>
  pandas<br>
  openpyxl<br>
  numpy<br>
  tkinter (comes with Python)<br>


**🧠 Classification Logic (Heuristic Rules)**
| Particle | Track Features               | Color      |
| -------- | ---------------------------- | ---------- |
| Alpha    | High area, thick and slow    | 🔴 Red     |
| Beta     | Medium area, thin and curved | 🟢 Green   |
| Muon     | Long and straight, low area  | 🟣 Magenta |


**📘 Source Validation**<br>
The tool uses a file named sources.xlsx containing valid pairs of radioactive sources and their emitted particles. If the user enters an invalid combination, the program stops with an error message.<br>

**🛠️ TODO / Future Improvements** <br>
	Improve accuracy using machine learning (e.g., CNN).<br>
	Support for gamma rays and neutron tracks.<br>
	CLI and web interface options.<br>


**📸 Sample Output**!

A side-by-side image is saved as tracks_comparison.jpg, showing original and detected particle tracks with labeled colors.

[tracks_comparison](https://github.com/user-attachments/assets/c6d4e162-620d-4993-bf1b-a2e3a4e90094)


