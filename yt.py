# pip install yt-dlp

# Install chocolatey

# Set-ExecutionPolicy Bypass -Scope Process -Force; `
# [System.Net.ServicePointManager]::SecurityProtocol = `
# [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
# iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install ffmpeg
# choco install ffmpeg -y

# pip install yt-dlp

import subprocess; 

subprocess.run(["yt-dlp","-f","bv*+ba/b","-o","%(title)s.%(ext)s","https://www.youtube.com/watch?v=xOccYkgRV4Q&list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH&index=30"])
