from flask import Flask, Response, render_template_string
from detect_utils import get_frame

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>YOLOv8 Canlı Tespit</title>
</head>
<body>
    <h1>Canlı Yüz/Nesne Tespiti</h1>
    <img src="{{ url_for('video_feed') }}" width="720" />
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
