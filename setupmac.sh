#!/bin/bash

# Setup homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo -e 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
echo -e 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zprofile

# Update and install dependencies
brew update
brew install openssl readline sqlite3 xz zlib
brew install tmux

# Install pyenv
brew install pyenv

# Set up pyenv environment variables
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/. zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zprofile

# Source the profile to set environment variables in the current shell session
exec "$SHELL"

# Install Python 3.11.9 and set as global version
pyenv install 3.11.9
pyenv global 3.11.9

# Install Poetry
brew install poetry

# Set up Poetry environment variables
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zprofile
exec "$SHELL"

# Configure Poetry
poetry config virtualenvs.in-project true

# Install Ollama
brew install ollama

# Set up Ollama environment variables
echo 'export OLLAMA_DEBUG=1' >> ~/.zshrc
echo 'export OLLAMA_DEBUG=1' >> ~/.zprofile
exec "$SHELL"

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
echo 'export PGPT_PROFILES=ollama' >> ~/.zshrc
echo 'export PGPT_PROFILES=ollama' >> ~/.zprofile
exec "$SHELL"

# Run PrivateGPT
make run