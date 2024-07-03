import requests
import os
import time
import argparse

def main(api_ip):
    # Directory containing the PDF files
    dirname = os.path.dirname(__file__)
    directory = os.path.join(dirname, 'data')

    # List all files in the directory
    file_paths = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.pdf')]

    # Define API endpoint (replace with your vastai IP address)
    api_endpoint = "/v1/ingest/file"
    api_url = f"http://{api_ip}{api_endpoint}"

    headers = {
        'Content-Type': 'multipart/form-data'
    }

    print("ingesting files")

    start_time = time.time()

    # Prepare files dictionary for multipart/form-data
    for idx, file_path in enumerate(file_paths):
        files = {}
        files['file'] = open(file_path, 'rb')

        # Send POST request with files as multipart/form-data
        response = requests.post(api_url, headers, files=files)

        # Check if request was successful
        if response.status_code == 200:
            # print(response.json())
            # print(os.path.basename(file_path) + " successfully ingested")
            pass
        else:
            print(f"Error occurred: {response.status_code} - {response.text} with file: {os.path.basename(file_path)}")

    ingestion_time = time.time() - start_time
    print("Ingestion time: " + ingestion_time)

    # Close file handles
    for file_handle in files.values():
        file_handle.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest PDF files to the specified API.')
    parser.add_argument('api_ip', type=str, help='API IP address')
    args = parser.parse_args()
    main(args.api_ip)