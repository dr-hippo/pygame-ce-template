# Pygame-CE Template

Basic [pygame-ce](https://pyga.me) template with prewritten boilerplate, useful classes, and build/upload scripts.

Intended for use in game jams.

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

### Building
1. Run `src/_buildtools/build2exe.py` to build to an executable in `/dist`
2. Run `src/_buildtools/build2web.py` to build to a play-in-browser package in `/build/web/build/web`

### Uploading to itch.io (optional)
1. [Register](https://itch.io/register) or [login](https://itch.io/login) to an itch.io account
2. [Create a new project](https://itch.io/game/new)
3. Install [butler](https://itchio.itch.io/butler) and add its folder to PATH
4. On the command line, login to butler with your itch account
5. Run `src/_buildtools/itch_upload.py` to upload built files to itch.io
6. Customise your page
