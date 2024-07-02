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

# Update ~/.bashrc with pyenv configurations
os.system('echo \'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"\' >> ~/.bashrc')
os.system('echo \'eval "$(pyenv init --path)"\neval "$(pyenv init -)"\' >> ~/.bashrc')
os.system('exec "$SHELL"')

# Install Python 3.11.9 using pyenv
subprocess.run(["pyenv", "install", "3.11.9"])
subprocess.run(["pyenv", "global", "3.11.9"])

# Install poetry
subprocess.run(["curl", "-sSL", "https://install.python-poetry.org", "|", "python3", "-"])

# Update ~/.bashrc with poetry path
os.system('echo \'export PATH="$HOME/.local/bin:$PATH"\' >> ~/.bashrc')
os.system('exec "$SHELL"')

# Configure poetry
subprocess.run(["poetry", "config", "virtualenvs.in-project", "true"])

# Install pciutils
subprocess.run(["sudo", "apt-get", "-y", "install", "pciutils"])

# Install Ollama
subprocess.run(["curl", "-fsSL", "https://ollama.com/install.sh", "|", "sh"])
os.environ['OLLAMA_DEBUG'] = '1'
subprocess.run(["sudo", "systemctl", "enable", "ollama"])

# Start Ollama service using tmux
subprocess.run(["tmux", "new-session", "-d", "-s", "ollama_session", "'ollama serve > ollama.log 2>&1'"])

# Pull required repositories
subprocess.run(["ollama", "pull", "mistral"])
subprocess.run(["ollama", "pull", "nomic-embed-text"])

# Set up environment
subprocess.run(["pyenv", "local", "3.11.9"])
subprocess.run(["poetry", "install", "--extras", "ui llms-ollama embeddings-ollama vector-stores-qdrant"])
os.environ['PGPT_PROFILES'] = 'ollama'

# Run make command to start
subprocess.run(["make", "run"])