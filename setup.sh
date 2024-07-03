#!/bin/bash

# Update and install dependencies
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
sudo apt-get install -y lzma

# Install pyenv
curl https://pyenv.run | bash

# Set up pyenv environment variables
echo -e 'export PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'eval "$(pyenv init --path)"\neval "$(pyenv init -)"' >> ~/.bashrc

# Source the temporary file to set environment variables in the current shell session
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# Install Python 3.11.9 and set as global version
pyenv install 3.11.9
pyenv global 3.11.9

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Set up Poetry environment variables
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/.local/bin:$PATH"

# Configure Poetry
poetry config virtualenvs.in-project true

# Install Ollama
sudo apt-get -y install pciutils
curl -fsSL https://ollama.com/install.sh | sh

# Set up Ollama environment variables
echo 'export OLLAMA_DEBUG=1' >> ~/.bashrc
export OLLAMA_DEBUG=1

# Enable and start Ollama service
systemctl enable ollama
tmux new-session -d -s ollama_session 'ollama serve > ollama.log 2>&1'

# Pull models with Ollama
sleep 2
ollama pull mistral
ollama pull nomic-embed-text

# Install PrivateGPT
git clone https://github.com/zylon-ai/private-gpt
cd private-gpt
pyenv local 3.11.9
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant"

# Set up PrivateGPT environment variables
echo 'export PGPT_PROFILES=ollama' >> ~/.bashrc
export PGPT_PROFILES=ollama

# Run PrivateGPT
make run