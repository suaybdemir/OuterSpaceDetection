# Outer Space Detection Management System

This project creating as to analyze space objects which depends on detection, classification and analysis of what there is in the input.

## ✨ How it will work?
1. User phone or ESP32-CAM take photos (in this stage telephone phone or potent images like university instances or in journal etc.), from space.
2. Photos gonna sent **.NET Core backend**.
3. With **OpenCV** bright points (starts, planets , meteors ...) detects.
4. **Own SpaceObjectsDetection AI**, stars being classified and like brightness, distance datas being analyzed.
5. Conclusion : we can look results from **in mobile or web interface**.

## 🛠️ Requirements
- **Phone or ESP32-CAM** (Better if it supports long exposure)
- **.NET Core Backend**
- **OpenCV (C# Wrapper)**
- **Python**
- **Mobile or Web Interface**

## 🔄 Installation
1. **Install Backend Dependencies**
   ```sh
   dotnet restore
   ````
2. **Start AI Service**
   - Sent photos to AI and take from **Phyton**.
3. **Run Backend**
   ```sh
   dotnet run
   ```
4. **Run Frontend**
   ```sh
   ng serve
   ```
5. **Send Photos from Embeeded or Dynamic System as to look**

## 🌐 EXAMPLE API USAGE (Yet not ready to use!)
**Star Analyze API:**
```http
POST /api/stars/analyze
Content-Type: multipart/form-data
```
Body: `image: {sky photo}`

Response:
```json
{
  "star_type": "Red Giant",
  "brightness": "100.000 Lux",
  "distance": "412 Light Years"
}
```

