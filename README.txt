Proje Adı: Exercise Detection
Bu proje, egzersizleri tanıyan bir model ve kamera üzerinden gerçek zamanlı olarak tanıma sağlayan bir uygulamayı içerir.

Başlama
Bu adımları takip ederek projeyi başka bir bilgisayarda çalıştırabilirsiniz.

Önkoşullar
Projeyi çalıştırmak için aşağıdaki yazılımların yüklü olması gerekir:
Python 3.x
TensorFlow
OpenCV
Kurulum

GitHub Repository'sini Klonlayın:
git clone https://github.com/berenttan/exercise-detection.git
cd exercise-detection

Sanal ortam oluşturun:
python -m venv venv

Sanal ortamı etkinleştirin:
Windows için:
venv\Scripts\activate
Unix veya MacOS için:
source venv/bin/activate

Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt

Jupyter Notebook kullanarak proje dosyasını açın:
jupyter notebook project.ipynb

Gerçek zamanlı egzersiz tanıma uygulamasını başlatın:
python camera.py