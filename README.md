## Music Downloader
Simple and configurable CLI app for downloading YouTube videos.

### Requirements
 - Python 3.6.x-3.9.x
 - make

### Quick start:
 - cmd: `make quick.start`
 - cmd: `make run`

### Setup (Windows)
 - cmd: `py -m venv .venv`
 - cmd: `.venv\Scripts\activate`
 - cmd: `pip install -r requirements.txt`
 - adjust config.json file to your needs
 - cmd: `py src/app.py`

### Confiuration
 - `baseUrl` - url to the source channel videos
 - `quality` - quality (=size) of downloaded videos: 0 - 128bps, 1 - 256 bsp
 - `downloadDepth` - number of pixels to be scrolled in total in order to load more videos
 - `downloadDepthStep` - number of pixels to be scrolled at once in order to load more videos
 - `downloadDepthStepWaitTime` - number of seconds required for more videos to load
 - `downloadDelay` - optional interval between each download
 - `maxWaitTime` - maximum number of seconds required for a website to load
 - `skip` - number of skipped videos
 - `take` - target number of downloaded videos
