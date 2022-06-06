import yt_dlp
import random
import os
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from django.core.files.temp import NamedTemporaryFile
from datetime import datetime

def index(request):
    return render(request, 'index.html', {})

def download(request):
    url     = request.POST['url']
    type    = request.POST['type'] 
    info    = {}    

    random.seed(datetime.now())
    filename = f"{settings.BASE_DIR}/videos/" + str(random.randint(0, 999))

    if type == 'audio':
        format = "bestaudio"
        
        opts = {
                'format': format,
                'outtmpl': f"{filename}.%(ext)s",
                'cookiefile': f"{settings.BASE_DIR}/cookies.txt",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
        }
        
        extension = '.mp3'
        filename  = filename + extension

    else:
        format = f"bestvideo[height<=?{type}]+bestaudio"

        opts = {
                'format': format,
                'outtmpl': f"{filename}.%(ext)s",
                'cookiefile': f"{settings.BASE_DIR}/cookies.txt",
                'postprocessors': [{
                    'key': 'FFmpegVideoRemuxer',
                    'preferedformat': 'mkv'
                }]
        }

        extension = '.mkv'
        filename = filename + extension  
    
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url)

    temp = NamedTemporaryFile()
    temp.write(open(filename, 'rb').read())
    os.remove(filename)

    return FileResponse(open(temp.name, 'rb'), filename=info['title'] + extension, as_attachment=True)
