# Pygame-CE Template

Basic [pygame-ce](https://pyga.me) template with prewritten boilerplate, useful classes, and build/upload scripts.

Intended for use in game jams.

## Features:
- Highly configurable from `src/config.py`
- Scene/Entity system (TODO)
- Data/Settings save/load (TODO)
- Utilities script: (TODO)
  - Image, sound, and font loading
  - Image and audio caching (TODO) 
  - Basic text rendering
- Premade build scripts for building to executable/play-in-browser bundle 
with [PyInstaller](https://pyinstaller.org)/[Pygbag](https://pypi.org/project/pygbag)
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
1. Navigate to the project's root folder
2. Run `python -m bundle.to_exe` to build to an executable in `/dist`
3. Run `python -m bundle.to_web` to build to a play-in-browser package in `/build/web/build/web`
4. Instead of typing these commands, you can set up run configurations in IDEs such as PyCharm to make building more convenient

### Uploading to itch.io (optional)
1. [Register](https://itch.io/register) or [login](https://itch.io/login) to an itch.io account
2. [Create a new project](https://itch.io/game/new)
3. Install [butler](https://itchio.itch.io/butler) and add its folder to PATH
4. On the command line, login to butler with your itch account
5. Run `python -m bundle.upload_to_itch` to upload built files to itch.io
6. Customise your page
