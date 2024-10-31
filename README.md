
# Env-Req-Merge-Tool

## 簡介 (Introduction)
`Env-Req-Merge-Tool` 是一個簡單的 Python 工具，用於合併 Conda 環境檔案 (`environment.yml`) 和 Pip 需求檔案 (`requirements.txt`)，並生成一個綜合的 `combined_requirements.txt`，方便管理和部署環境。

## 功能 (Features)
- 讀取 `environment.yml` 中 Conda 套件和版本資訊。
- 讀取 `requirements.txt` 中 Pip 套件和版本資訊。
- 將兩者的依賴合併為 `combined_requirements.txt`，避免重複並保留所有的版本資訊。

## 使用方法 (How to Use)
1. 克隆此儲存庫：
   ```sh
   git clone https://github.com/Yucheng0208/Env-Req-Merge-Tool.git
   ```
2. 將 `environment.yml` 和 `requirements.txt` 放置在儲存庫根目錄。
3. 執行合併程式：
   ```sh
   python merge_dependencies.py
   ```
4. 合併完成後，將在目前目錄生成 `combined_requirements.txt`。

## 依賴 (Dependencies)
- Python 3.x
- pyyaml

## 參與貢獻 (Contributing)
歡迎提出 Issues 或 Pull Requests，幫助改進此工具。

## 授權 (License)
此儲存庫使用 MIT 授權，詳情請參閱 [LICENSE](./LICENSE) 檔案。

---

## Introduction
`Env-Req-Merge-Tool` is a simple Python tool for merging Conda environment files (`environment.yml`) and Pip requirements files (`requirements.txt`) into a unified `combined_requirements.txt`, making environment management and deployment more convenient.

## Features
- Reads Conda packages and versions from `environment.yml`.
- Reads Pip packages and versions from `requirements.txt`.
- Combines both sets of dependencies into `combined_requirements.txt`, avoiding duplicates and preserving all version information.

## How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/Yucheng0208/Env-Req-Merge-Tool.git
   ```
2. Place `environment.yml` and `requirements.txt` in the repository root.
3. Run the merge script:
   ```sh
   python merge_dependencies.py
   ```
4. The combined requirements will be saved as `combined_requirements.txt` in the current directory.

## Dependencies
- Python 3.x
- pyyaml

## Contributing
Feel free to open Issues or Pull Requests to help improve this tool.

## License
This repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Pendahuluan
`Env-Req-Merge-Tool` adalah alat Python sederhana untuk menggabungkan file lingkungan Conda (`environment.yml`) dan file persyaratan Pip (`requirements.txt`) ke dalam satu file `combined_requirements.txt`, memudahkan manajemen dan penerapan lingkungan.

## Fitur
- Membaca paket Conda dan versinya dari `environment.yml`.
- Membaca paket Pip dan versinya dari `requirements.txt`.
- Menggabungkan keduanya ke dalam `combined_requirements.txt`, menghindari duplikasi dan mempertahankan semua informasi versi.

## Cara Menggunakan
1. Clone repositori ini:
   ```sh
   git clone https://github.com/Yucheng0208/Env-Req-Merge-Tool.git
   ```
2. Tempatkan file `environment.yml` dan `requirements.txt` di root repositori.
3. Jalankan script penggabungan:
   ```sh
   python merge_dependencies.py
   ```
4. Persyaratan gabungan akan disimpan sebagai `combined_requirements.txt` di direktori saat ini.

## Ketergantungan
- Python 3.x
- pyyaml

## Kontribusi
Jangan ragu untuk membuka Issues atau Pull Requests untuk membantu meningkatkan alat ini.

## Lisensi
Repositori ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](./LICENSE) untuk detail lebih lanjut。
