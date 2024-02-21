import os
import zipfile

import requests

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    os.makedirs("downloads", exist_ok=True)
    for uri in download_uris:
        print(f"Downloading {uri}")
        try:
            response = requests.get(uri)
            with open(f'downloads/{uri.split("/")[-1]}', "wb") as file:
                file.write(response.content)
            print(f"Downloaded {uri}")

            # unzip
            with zipfile.ZipFile(f'downloads/{uri.split("/")[-1]}', "r") as zip_ref:
                zip_ref.extractall("downloads")

        except Exception as e:
            print(f"Failed to download {uri}", e)

        # break


if __name__ == "__main__":
    main()
