# YouTube-Downloader
A small Django webapp that downloads videos from YouTube, as well as audio.

# Running the webapp
I recommend using virtualenv to create a virtual environment, then installing django and yt_dlp.
I left out the secret key and allowed hosts in the settings file (located in [youtube_downloader/settings.py](youtube_downloader/settings.py)).
You would need to add your IP address or domain name, and some arbitrary secret key before running this.

```
virtualenv venv
source venv/bin/activate
pip install django yt_dlp
python manage.py runserver
```
