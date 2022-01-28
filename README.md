This script automates house buying in FF14. Includes random timing for peace of mind. Automatically stops and moves backwards when the house is sold so you don't look like a bot.

### Set up

1. Download and install Python - https://www.python.org/downloads/
    - Remember to select the checkbox "Add Python x.x to PATH"
3. Open Command Prompt as administrator
4. Install required packages
    - pip install pyautogui
    - pip install "opencv-python-headless<4.3"
5. Replace yes_button.png in images/ folder with your own screenshot
6. Open config.ini in a text editor and set ConfirmButton = whatever your 'Confirm' keybind is set to in-game. NUM0 by default.

### Usage

In Command Prompt
1. Navigate to folder:
    - cd <path_to_folder> 
        - for example: `cd C:\Users\username\Downloads\ffbuyhouse`
2. Stand in front of the placard and make sure nothing is selected.
3. Run:
    - python buyhouse.py
