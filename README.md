# YOLOv8 Flask Tabanlı Canlı Obje Tespiti

Bu proje, YOLOv8 modeli kullanarak gerçek zamanlı obje/yüz tespiti yapar ve Flask ile web üzerinden canlı görüntü sağlar.

## 🎯 Özellikler

- YOLOv8 (Ultralytics) ile gerçek zamanlı nesne/yüz tespiti
- Flask ile web arayüzü
- Kamera üzerinden canlı yayın
- Docker ile kolay dağıtım

## 🖼️ Arayüz Görünümü

Web arayüzü:

http://localhost:5000


![örnek](https://via.placeholder.com/720x400.png?text=Canl%C4%B1+Obje+Tespiti+%28Web+Aray%C3%BCz%C3%BC%29)

---

## 🧱 Proje Dizini

yolo-flask-app/
├── app.py # Flask uygulaması
├── detect_utils.py # Kamera ve YOLOv8 entegrasyonu
├── yolov8n.pt # YOLOv8 model dosyası
├── Dockerfile # Docker imajı için yapılandırma
├── requirements.txt # Python bağımlılıkları
└── README.md # Bu dosya


---

## ⚙️ Gereksinimler

- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- Flask

Tüm bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt

🚀 Uygulamayı Başlat

python app.py

Sonrasında tarayıcıdan şu adrese gir:

http://localhost:5000

🐳 Docker ile Çalıştırma

docker build -t yolo-flask-app .
docker run -p 5000:5000 --device=/dev/video0 yolo-flask-app

    --device=/dev/video0 kısmı, kamera erişimi için gereklidir.

📦 YOLOv8 Model Dosyası

Model dosyasını Ultralytics üzerinden indir:

from ultralytics import YOLO
YOLO('yolov8n.pt')  # otomatik indirir

Ya da manuel olarak yolov8n.pt dosyasını proje dizinine koy.
✍️ Yazılım Geliştirici

Alper Temizel
📫 GitHub: @alpertemizel
🧠 Kaynaklar

    Ultralytics YOLOv8 GitHub

    Flask Documentation

    OpenCV
