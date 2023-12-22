# Pygame-CE Template

Basic [pygame-ce](https://pyga.me) template with prewritten boilerplate, useful classes, and build/upload scripts.

## Features:
- Game state save/load (TODO)
- Scene system (TODO)
- Utilities script: (TODO)
  - Image, sound, and font loading functions
  - Image and audio caching functions (TODO) 
  - Text rendering function
- Premade build script for Windows and Web (through [pygbag](https://pypi.org/project/pygbag))
- Fast uploading to [itch.io](https://itch.io) through [butler](https://itch.io/docs/butler).

## Workflow:
### Setup:
1. Create new repo from this template and clone to your computer.
2. Create virtual environment (Build script assumes folder is called `.venv`)
3. Install required dependencies with pip (`pip install -r requirements.txt`)

### Programming
1. TODO

### Running
1. Navigate to the template folder from the command line and run `py main.py`

### Building and Uploading
1. Run `build` on the command line to build to a Windows executable in `/dist`
2. Run `py build2web.py` on the command line to build to a play-in-browser package in `/build/web/build/web`
3. Run `*WIP` to upload to itch.io with butler (requires itch account and butler being installed)