#!/bin/bash

INSTALL_PATH="/usr/local/share/mytools"
BIN_PATH="/usr/local/bin/mytools"

echo "Uninstalling MyTools..."

# ลบไฟล์และโฟลเดอร์โปรแกรม
if [ -d "$INSTALL_PATH" ]; then
    sudo rm -rf "$INSTALL_PATH"
    echo "Removed $INSTALL_PATH"
else
    echo "$INSTALL_PATH does not exist"
fi

# ลบคำสั่งใน /usr/local/bin
if [ -f "$BIN_PATH" ]; then
    sudo rm "$BIN_PATH"
    echo "Removed $BIN_PATH"
else
    echo "$BIN_PATH does not exist"
fi

echo "Uninstall complete!"
