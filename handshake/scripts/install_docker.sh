#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Update references
    sudo apt-get update -y

    # Remove previous docker
    sudo apt-get remove docker docker-engine docker.io containerd runc

    # Install dependencies
    sudo apt-get -y install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg

    # Add key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    # Add from stable
    echo \
        "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # Install
    sudo apt-get update
    sudo apt-get -y install docker-ce docker-ce-cli containerd.io

    # Install compose
    sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
else
    brew install --cask docker
fi
