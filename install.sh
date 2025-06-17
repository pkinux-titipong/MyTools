#!/bin/bash

INSTALL_PATH="/usr/local/share/mytools"
BIN_PATH="/usr/local/bin/mytools"

echo "Installing MyTools..."

# สร้างโฟลเดอร์โปรแกรม
sudo mkdir -p "$INSTALL_PATH"

# สร้าง virtual environment ใน INSTALL_PATH
echo "Creating Python virtual environment..."
sudo python3 -m venv "$INSTALL_PATH/venv"

# อัพเกรด pip และติดตั้ง dependencies ผ่าน venv
echo "Installing Python dependencies (beautifulsoup4, requests) in venv..."
sudo "$INSTALL_PATH/venv/bin/pip" install --upgrade pip
sudo "$INSTALL_PATH/venv/bin/pip" install beautifulsoup4 requests

# คัดลอกไฟล์ Python ไปไว้ที่ INSTALL_PATH
sudo cp main.py calculator.py tic_tac_toe.py "$INSTALL_PATH"

# สร้างคำสั่ง 'mytools' ที่รัน main.py ผ่าน venv python
echo '#!/bin/bash' | sudo tee "$BIN_PATH" > /dev/null
echo "source $INSTALL_PATH/venv/bin/activate && python $INSTALL_PATH/main.py" | sudo tee -a "$BIN_PATH" > /dev/null

# ตั้งสิทธิ์รันให้ command
sudo chmod +x "$BIN_PATH"

echo "Installation complete! Run 'mytools' from anywhere to start."
