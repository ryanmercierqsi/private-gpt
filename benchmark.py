import requests
import os
import time
import argparse
from tqdm import tqdm

def main(api_ip):
    # Directory containing the PDF files
    dirname = os.path.dirname(__file__)
    directory = os.path.join(dirname, 'data')

    # List all files in the directory
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.pdf')]

    # Define API endpoint (replace with your vastai IP address)
    api_endpoint = "/v1/ingest/file"
    api_url = f"http://{api_ip}{api_endpoint}"

    log_file = 'benchmark.log'

    print("Ingesting Files ...")

    start_time = time.time()

    # Prepare files dictionary for multipart/form-data
    for file_path in tqdm(enumerate(file_paths), total=len(file_paths), desc="Ingesting files"):
        files = {}
        files['file'] = open(file_path, 'rb')

        # Send POST request with files as multipart/form-data
        response = requests.post(api_url, files=files)

        # Check if request was successful
        with open(log_file, 'a') as log:
            if response.status_code == 200:
                log.write(f"{os.path.basename(file_path)} successfully ingested\n")
            else:
                log.write(f"Error occurred: {response.status_code} - {response.text} with file: {os.path.basename(file_path)}\n")

        # Close file handles
        files['file'].close()

    ingestion_time = time.time() - start_time

    print(f"Ingestion time: {ingestion_time} seconds\n")
    with open(log_file, 'a') as log:
        log.write(f"Ingestion time: {ingestion_time} seconds\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest PDF files to the specified API.')
    parser.add_argument('api_ip', type=str, help='API IP address')
    args = parser.parse_args()
    main(args.api_ip)