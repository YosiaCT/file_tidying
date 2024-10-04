import os
import shutil

def organize_files(folder_path):
    """Mengorganisir file dalam folder berdasarkan jenis file."""
    # Membuat folder target jika belum ada
    folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Music': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv'],
    }

    for folder, extensions in folders.items():
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    # Memindahkan file berdasarkan jenis file
    for filename in os.listdir(folder_path):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in folders.items():
            if file_extension in extensions:
                shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, folder, filename))
                print(f'Memindahkan {filename} ke {folder}.')

def main():
    folder_path = input("Masukkan path folder yang ingin dibersihkan: ")
    organize_files(folder_path)

if __name__ == "__main__":
    main()
