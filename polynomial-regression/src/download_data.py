import os
import subprocess
import zipfile

def download_kaggle_dataset():
    os.makedirs("data/raw", exist_ok=True)

    command = [
        "kaggle",
        "competitions",
        "download",
        "-c",
        "house-prices-advanced-regression-techniques",
        "-p",
        "data/raw"
    ]

    subprocess.run(command)
    
    # unzip any zip files in data/raw
    for file in os.listdir("data/raw"):
        if file.endswith(".zip"):
            zip_path = os.path.join("data/raw", file)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall("data/raw")
            os.remove(zip_path)  # remove the zip after extracting

if __name__ == "__main__":
    download_kaggle_dataset()