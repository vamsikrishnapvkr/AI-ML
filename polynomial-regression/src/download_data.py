import os
import subprocess

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
    
    # unzip
    subprocess.run(["unzip", "data/raw/train.csv.zip", "-d", "data/raw"])

if __name__ == "__main__":
    download_kaggle_dataset()