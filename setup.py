import os
import subprocess

# Update package lists and install required packages
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "-y", "make", "build-essential", "libssl-dev", "zlib1g-dev",
                "libbz2-dev", "libreadline-dev", "libsqlite3-dev", "wget", "curl", "llvm", "libncursesw5-dev",
                "xz-utils", "tk-dev", "libxml2-dev", "libxmlsec1-dev", "libffi-dev", "liblzma-dev", "lzma"])

# Install pyenv
subprocess.run(["curl", "-fsSL", "https://pyenv.run", "-o", "pyenv-installer.sh"])
subprocess.run(["bash", "pyenv-installer.sh"])

# Install Python 3.11.9 using pyenv
subprocess.run(["pyenv", "install", "3.11.9"])
subprocess.run(["pyenv", "global", "3.11.9"])

# Install poetry
subprocess.run(["curl", "-sSL", "https://install.python-poetry.org", "-o", "poetry-installer.sh"])
subprocess.run(["python3", "poetry-installer.sh"])

# Configure poetry
subprocess.run(["poetry", "config", "virtualenvs.in-project", "true"])

# Install pciutils
subprocess.run(["sudo", "apt-get", "-y", "install", "pciutils"])

# Install Ollama
subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh", "-o", "ollama-installer.sh"])
subprocess.run(["sh", "ollama-installer.sh"])
subprocess.run(["sudo", "systemctl", "enable", "ollama"])

# Start Ollama service using Popen in a subshell
ollama_command = "ollama serve > ollama.log 2>&1"
subprocess.Popen(ollama_command, shell=True, executable="/bin/bash")

# Pull required repositories
subprocess.run(["ollama", "pull", "mistral"])
subprocess.run(["ollama", "pull", "nomic-embed-text"])

# Set up environment
subprocess.run(["pyenv", "local", "3.11.9"])
subprocess.run(["poetry", "install", "--extras", "ui llms-ollama embeddings-ollama vector-stores-qdrant"])

# Run make command to start
subprocess.run(["make", "run"])