# Pygame-CE Template

Basic [pygame-ce](https://pyga.me) template with prewritten boilerplate, useful classes, and build/upload scripts.

## Features:
- Scene/Gameobject system (TODO)
- Game state save/load (TODO)
- Utilities script: (TODO)
  - Image, sound, and font loading functions
  - Image and audio caching functions (TODO) 
  - Text rendering function
- Premade build scripts for building to executable/play-in-browser bundle (with [PyInstaller](https://pyinstaller.org)/[Pygbag](https://pypi.org/project/pygbag))
- Fast uploading to [itch.io](https://itch.io) with [butler](https://itchio.itch.io/butler)

## Workflow:
### Setup:
1. Create new repo from this template and clone to your computer
2. Create virtual environment (Build script assumes folder is called `.venv`)
3. Install required dependencies with pip (`python -m pip install -r requirements.txt`)
4. Change settings in `src/config.py` if needed

### Programming
1. TODO

### Building and Uploading
1. Configure `build2exe.py` and `build2web.py`
2. Run `build2exe.py` to build to an executable in `/dist`
3. Run `build2web.py` to build to a play-in-browser package in `/build/web/build/web`
4. Run `itch_upload.py` to upload the game to itch.io with butler ([Documentation](https://itchio.itch.io/butler))
