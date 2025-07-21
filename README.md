# YOLOv8 Live Object Detection with Flask and Docker

This project is a simple real-time object detection app using YOLOv8 and a webcam.  
It runs as a Flask web app and shows live detection results in the browser.  
You can also run it inside a Docker container for easy deployment.

## Features

- Real-time object/face detection
- Flask-based web interface
- Docker support for portability

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/yolov8-live-detection.git
cd yolov8-live-detection

2. Install requirements (for local setup)

pip install -r requirements.txt

Make sure you have a webcam connected.
3. Run the app

python app.py

Visit http://localhost:5000 in your browser to see the live detection.
Docker Usage

You can also run everything in a Docker container:

docker build -t yolov8-app .
docker run -p 5000:5000 --device=/dev/video0 yolov8-app

Make sure /dev/video0 is your camera device.
Project Structure

.
├── app.py              # Main Flask application
├── detect_utils.py     # Frame grabbing and YOLOv8 detection
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image build config
└── README.md

Notes

    This app uses a YOLOv8 model trained or downloaded from Ultralytics.

    It works with faces, people, or any objects the model is trained on.

License

This project is open-source and available under the MIT License.
Feel free to modify or use it in your own projects.
