pyinstaller main.py -F --noconfirm --log-level=WARN ^
--add-data "assets;assets" --add-data "data;data" ^
-n "PygameCE-Template" ^
-p ".venv\Lib\site-packages" % change this path depending on where your venv is % ^
--noconsole -i "assets\images\sample.jpg"