<div align="center">
   
   # WGE
   
   **W**indows **G**amepad **E**mulator utility
   
   [![PYTHON](https://img.shields.io/badge/Language-PYTHON-497591?logo=python&logoColor=fff&style=for-the-badge)](https://en.wikipedia.org/)
   [![WINDOWS](https://img.shields.io/badge/OS-Windows-0078a4?logo=quarto&logoColor=fff&style=for-the-badge)](https://en.wikipedia.org/wiki/PHP)
    
</div>

<br>

# About
This python project is a simple wrapper ontop of [ViGemBus driver](https://github.com/nefarius/ViGEmBus) that allows HID emulation on Windows machines to emulate an XBOX360 controller and manipulate it via keyboard and mouse. Created for people that don't enjoy the idea of spending money on a gamepad to play certain games as well as for those who never had one and never wanted one in their possession.
Project was initially written years ago when I decided to play a very known game that only supports controller inputs and been rewritten to fix some major issues like input lag (thanks python), flexibility in customization and lack of some quality-of-life features like cursor hiding.

# Requirements:
| Prerequisite               | Description                      |
| -------------------------- | -------------------------------- |
| Windows                    | Operating System                 |
| Python 3.12                | Interpreter, tested only on 3.12 |
| ViGemBus driver            | Installed with [requirements.txt](requirements.txt) |
| Keyboard and mouse         | Obviously, right?                |

# Installation:
Step 1: Clone the project by either using git cli
```bash
git clone git@github.com:aASDa213ASD/WGE.git
```
or by downloading the source code directly

Step 2: Create virtual environment
```bash
cd WGE
python -m venv .env
```

Step 3: Activate virtual environment you've just created
```bash
.env\Scripts\activate
```

Step 3: Install prerequisites, that will install ViGemBus driver as well
```bash
pip install -r requirements.txt
```

# Configuration
All of the tinkering with your binds and gamepad button definitions will be happening in **[setting.py](common/settings.py)** file. I've spent some time writing this all down so you've got a decent chance to understand what goes where and why. In this file you are able to edit your **sensitivity**, **keybinds**, **mousebinds** and **invert direction of any axis** as well as redefine the **maximum possible stick position**.

# Usage
Either run `gamepad.bat` and it will activate virtual environment and launch the project for you, all you are left to do is to press your **[pause bind](common/settings.py#L68)** to unpase the gamepad and perhaps press your **[calibration bind](common/settings.py#L87)** to set the origin of right stick to current cursor position.

That's pretty much it, now you can point your gamepad to some program and use it as it was real.

Attention: In case you've created virtual environment with other name than `.env` change it in `.bat` file as well.

# Credits
[@Nefarius](https://github.com/nefarius) for his [ViGEmBus](https://github.com/nefarius/ViGEmBus) that allowed all of that to be crafted in the first place

[@yannbouteiller](https://github.com/yannbouteiller) for [vgamepad python package](https://github.com/yannbouteiller/vgamepad) on pypi that handles some dirty job talking to ViGemBus through python means

[@PRich57](https://github.com/PRich57) for showing a [good example](https://github.com/PRich57/windows-cursor-hiding-utility) of how one can hide a cursor on Windows system via user32.dll only
