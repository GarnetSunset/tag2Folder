@echo off
pip install --quiet -r requirements.txt
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-latest-win64-static.zip', 'ffmpeg.zip')"
Powershell.exe -executionpolicy remotesigned -File  unZip.ps1
del ffmpeg.zip
