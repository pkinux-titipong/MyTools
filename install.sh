#!/bin/bash

INSTALL_PATH="/usr/local/share/mytools"
BIN_PATH="/usr/local/bin/mytools"

echo "Installing MyTools..."

# Create target directory
sudo mkdir -p "$INSTALL_PATH"

# Copy scripts
sudo cp mytools.py treemap.py webcheck.py "$INSTALL_PATH"

# Create shortcut in /usr/local/bin
echo '#!/bin/bash' | sudo tee "$BIN_PATH" > /dev/null
echo "python3 $INSTALL_PATH/main.py" | sudo tee -a "$BIN_PATH" > /dev/null

# Make it executable
sudo chmod +x "$BIN_PATH"

echo "Installation complete! Run 'mytools' from anywhere to start."
