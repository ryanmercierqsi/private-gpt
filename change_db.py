import yaml
import argparse

def update_yaml(file_path, host=None, port=None):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)

    if host and port:
        config['qdrant']['host'] = host
        config['qdrant']['port'] = port
        config['qdrant'].pop('path', None)  # Remove the path key if present
    else:
        config['qdrant']['path'] = 'local_data/private_gpt/qdrant'
        config['qdrant'].pop('host', None)  # Remove the host key if present
        config['qdrant'].pop('port', None)  # Remove the port key if present

    with open(file_path, 'w') as file:
        yaml.safe_dump(config, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update settings with provided host and port')
    parser.add_argument('--host', type=str, help='Host for qdrant')
    parser.add_argument('--port', type=str, help='Port for qdrant')

    args = parser.parse_args()

    update_yaml("settings-ollama.yaml", args.host, args.port)
    update_yaml("settings.yaml", args.host, args.port)