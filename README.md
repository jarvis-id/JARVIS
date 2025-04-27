<div align="center">
  <img src="assets/logo.png" alt="JARVIS Logo" width="200">
</div>

<div align="center">
  <h1 style="color:#0366d6; margin-bottom:10px">
    J.A.R.V.I.S.
  </h1>
  <p style="color:#58a6ff" align="center">Just A Rather Very Intelligent System</p>
</div>

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
  ![License](https://img.shields.io/badge/License-MIT-green)
  ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

</div>

<p align="center">
  <a href="./README-en.md">
    <img src="https://img.shields.io/badge/Translate%20to %20English%20Version-%E2%86%92-blue" alt="Translate English Version">
  </a>
</p>

Sebuah asisten AI berbasis suara dan GUI yang terinspirasi oleh J.A.R.V.I.S. dari Iron Man, dibangun dengan Python dan model bahasa lokal (LLM).

## 🚀 Fitur Utama
- Interaksi suara dengan wake word "Jarvis"
- Antarmuka GUI modern menggunakan PyQt5
- Dukungan model lokal (Llama 3 8B Instruct)
- Integrasi browser dan YouTube
- Multi-theme (dark/light mode)

## 📦 Struktur Proyek
```
JARVIS/
├── gpt4all/              # Model AI lokal
│   └── Meta-Llama-3-8B-Instruct.Q4_0.gguf
├── assets/               # Aset gambar dan ikon
├── core/                 # Modul inti
│   ├── commands.py       # Sistem perintah
│   ├── hardware.py       # Kontrol hardware
│   ├── jarvis_ai.py      # Inti AI
│   └── voice.py          # Pemrosesan suara
├── gui/                  # Antarmuka pengguna
│   ├── app.py            # Aplikasi utama
│   └── themes.py         # Sistem tema
├── config.py             # Konfigurasi
├── main.py               # Entry point
└── requirements.txt      # Dependensi
```

## ⚙️ Instalasi
1. **Clone repositori**:
   ```bash
   git clone https://github.com/jarvis-id/JARVIS.git
   cd JARVIS
   ```

2. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download model LLM**:
   - Letakkan file model `Meta-Llama-3-8B-Instruct.Q4_0.gguf` di folder `gpt4all/`
   - Atau jalankan:
     ```bash
     python -m gpt4all download Meta-Llama-3-8B-Instruct.Q4_0.gguf --path gpt4all/
     ```

## 🖥️ Menjalankan
```bash
python main.py
```

## ⚙️ Konfigurasi
Sesuaikan pengaturan di `config.py`:
```python
CONFIG = {
    "user_name": "Master",          # Nama pengguna
    "hotword": "jarvis",            # Wake word
    "voice_enabled": True,          # Aktifkan suara
    "theme": "dark",                # Tema default
    "default_browser": "chrome",    # Browser default
    # ... dan lainnya
}
```

## 📌 Persyaratan Sistem
- Python 3.10+
- RAM 8GB+ (16GB direkomendasikan)
- GPU dengan dukungan CUDA (opsional)
- Sistem Operasi: Windows/Linux/macOS

## 🤖 Model AI yang Didukung
- Meta-Llama-3-8B-Instruct.Q4_0.gguf (default)
- Dapat menambahkan model GGUF lainnya ke folder `gpt4all/`

## 📄 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE.txt).

---

> **Catatan**: Proyek ini dalam pengembangan aktif. Kontribusi dipersilakan!
```

### Fitur README.md ini:
1. **Struktur Proyek** yang jelas sesuai dengan hasil optimasi Anda
2. **Instalasi** yang mudah dengan opsi download model otomatis
3. **Konfigurasi** yang sesuai dengan file `config.py`
4. **Catatan khusus** tentang model AI dan persyaratan sistem
5. **Responsif** dengan emoji dan formatting yang baik

Anda bisa menyesuaikan bagian:
- Logo (dengan mengubah path gambar)
- Link repository GitHub
- Lisensi jika berbeda
- Tambahan fitur khusus lainnya
