#!/bin/bash

sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev lzma
curl https://pyenv.run | bash
pyenv install 3.11.9
pyenv global 3.11.9
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
sudo apt-get -y install pciutils
curl -fsSL https://ollama.com/install.sh | sh
systemctl enable ollama
tmux new-session -d -s ollama_session 'ollama serve > ollama.log 2>&1';
ollama pull mistral
ollama pull nomic-embed-text
cd private-gpt
pyenv local 3.11.9
poetry install --extras "ui llms-ollama embeddings-ollama vector-stores-qdrant"
make run