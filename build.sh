pyinstaller main.py \
  --name "LagSwitch" \
  --icon "resources/icon.ico" \
  --add-data "resources/enable.mp3;resources" \
  --add-data "resources/disable.mp3;resources" \
  --add-data "config.json;." \
  --noconfirm \
  --optimize 2 \
  --uac-admin