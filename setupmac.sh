#!/bin/bash

# Update and install dependencies
brew update
brew install openssl readline sqlite3 xz zlib
brew install lzma

# Install pyenv
curl https://pyenv.run | bash

# Set up pyenv environment variables
echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bash_profile

# Source the profile to set environment variables in the current shell session
source ~/.bash_profile

# Install Python 3.11.9 and set as global version
pyenv install 3.11.9
pyenv global 3.11.9

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Set up Poetry environment variables
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

# Configure Poetry
poetry config virtualenvs.in-project true

# Install Ollama
brew install pciutils
curl -fsSL https://ollama.com/install.sh | sh

# Set up Ollama environment variables
echo 'export OLLAMA_DEBUG=1' >> ~/.bash_profile
source ~/.bash_profile

# Enable and start Ollama service
# macOS doesn't use systemctl, using launchctl for example or simply run as a background process
# Assuming there is an Ollama binary available in the path
# ollama serve > ollama.log 2>&1 &
tmux new-session -d -s ollama_session 'ollama serve > ollama.log 2>&1'

# Pull models with Ollama
sleep 2
ollama pull mistral
ollama pull nomic-embed-text

# Install PrivateGPT
# git clone https://github.com/zylon-ai/private-gpt
cd private-gpt  # Ensure this is the correct path to the cloned repository
pyenv local 3.11.9
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant"
pip install requests
pip install tqdm

# Set up PrivateGPT environment variables
echo 'export PGPT_PROFILES=ollama' >> ~/.bash_profile
source ~/.bash_profile

# Run PrivateGPT
make run