**🔬 RadiationTrackDetect**
A heuristic image processing algorithm that detects and classifies radiation particle tracks — such as alpha, beta, and muon — from cloud chamber images.<br> This project uses OpenCV for contour-based analysis and validates the source-emitter pair using an external Excel file.
<br>

**📌 Features**
🖼️ Upload any cloud chamber image via a simple GUI.<br>
🧠 Classify tracks as alpha (red), beta (green), and muon (magenta) using contour area and shape heuristics.<br>
📄 Validate radiation source-emitter pair using a reference Excel file (sources.xlsx).<br>
🖍️ Visualizes results with labeled tracks and a legend.<br>
📸 Saves a side-by-side comparison of the original and processed image.<br>


**🧪 Example Use Case**<br>
You built a cloud chamber and took a photo of the tracks.<br>

You know the radioactive source used (e.g., Sr-90) and its emitted particle (e.g., Beta).<br>

You launch this tool, upload the image, and input the source and emitter.

The tool verifies the input against the reference file.

The program highlights tracks based on contour shape and size and saves the result.


**📂 Project Structure**
cloud_chamber_project/
├── analyze_tracks.py
├── sources.xlsx
├── tracks_comparison.jpg
└── README.md


**🚀 How to Run**
git clone: https://github.com/IshfaqElahi/radiationtrackdetect.git
cd radiationtrackdetect

2. Create and activate a virtual environment (optional but recommended)
python -m venv myenv
myenv\Scripts\activate  # Windows

3. Install dependencies
pip install opencv-python pandas openpyxl numpy

4. Run the main script
python analyze_tracks.py


**📥 Dependencies**
  opencv-python
  pandas
  openpyxl
  numpy
  tkinter (comes with Python)


**🧠 Classification Logic (Heuristic Rules)**
| Particle | Track Features               | Color      |
| -------- | ---------------------------- | ---------- |
| Alpha    | High area, thick and slow    | 🔴 Red     |
| Beta     | Medium area, thin and curved | 🟢 Green   |
| Muon     | Long and straight, low area  | 🟣 Magenta |


**📘 Source Validation**
The tool uses a file named sources.xlsx containing valid pairs of radioactive sources and their emitted particles. If the user enters an invalid combination, the program stops with an error message.


**🛠️ TODO / Future Improvements**
Improve accuracy using machine learning (e.g., CNN).
Support for gamma rays and neutron tracks.
CLI and web interface options.


**📸 Sample Output**
A side-by-side image is saved as tracks_comparison.jpg, showing original and detected particle tracks with labeled colors.


