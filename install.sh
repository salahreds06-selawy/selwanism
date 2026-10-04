#!/bin/bash
# Selwanism Installer

echo "Installing Selwanism..."

if [ ! -f "sel" ]; then
    echo "Error: sel file not found!"
    exit 1
fi

chmod +x sel
sudo cp sel /usr/local/bin/sel

# Install cheatsheet data files to standard share directory
sudo mkdir -p /usr/share/selwanism/data/tools
sudo cp -r data/tools/*.json /usr/share/selwanism/data/tools/

echo "Installation complete!"
echo "Run 'sel -h' or 'sel nmap' to get started."
