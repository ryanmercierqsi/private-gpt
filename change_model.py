import yaml
import sys
import os

def update_ollama_llm_model(file_path, new_model):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    if 'ollama' in data and 'llm_model' in data['ollama']:
        data['ollama']['llm_model'] = new_model
    else:
        print(f"'ollama' or 'llm_model' not found in {file_path}")
        return

    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)

    print(f"Updated 'llm_model' to '{new_model}' in {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python change_model.py <new_model>")
        sys.exit(1)

    new_model = sys.argv[1]

    settings_files = ['settings.yaml', 'settings-ollama.yaml']
    for settings_file in settings_files:
        update_ollama_llm_model(os.path.join(sys.path[0], settings_file), new_model)