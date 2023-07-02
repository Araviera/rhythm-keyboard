# Rhythm-keyboard

This Python command-line tool listens to the sound of your Mac and turns the keyboard LED on/off depending on the volume level. It would look cool when playing [music](https://www.youtube.com/watch?v=dQw4w9WgXcQ). This tool utilizes keyboards that use the **Scroll Key** to turn on RGB. If your keyboard uses another key, it will not work. However, I may try to make them work in the future.

## Installation

To use this tool, you will need to install the following:

1. [Python3](https://www.python.org/downloads/).
2. A fake software audio device such as [BlackHole](https://github.com/ExistentialAudio/BlackHole), which is a free and open-source audio device that can be used as an input or output.
3. [LadioCast](https://apps.apple.com/eg/app/ladiocast/id411213048?mt=12), an app from the App Store.
4. [Homebrew](https://brew.sh)
5. latest version in [releases](https://github.com/MomenBreuer/rhythm-keyboard/releases). Click on `rhythm.keyboard.zip` to download the tool.

Extract the zip file

open the terminal windowinside the path of the extracted folder

run `brew install portaudio`

run `python3 -m pip install -r requirements.txt`. This will download the necessary Python libraries for the code to run.


## Usage

Go to System Settings > Sound, click on Output and select BlackHole, then click on Input and make it BlackHole.

![Screenshot 2023-07-01 at 9 15 31 PM](https://github.com/MomenBreuer/rhythm-keyboard/assets/108753652/550ae51e-0720-4cea-96f6-7f0988166e89)
![Screenshot 2023-07-01 at 9 24 28 PM](https://github.com/MomenBreuer/rhythm-keyboard/assets/108753652/b8439d27-cfc8-4a45-a56f-5ec789a5a981)

Launch the LadioCast app, click on Input 1 and select BlackHole, then select Main Output and select your output device. For example, I am connected to a Samsung SmartTV screen and my Mac sound is coming out from it.

![Screenshot 2023-07-01 at 9 26 05 PM](https://github.com/MomenBreuer/rhythm-keyboard/assets/108753652/48b7dee3-fb18-4e5f-a76c-780f4371b938)

Finally, to use the tool, run `python3 rhythm_keyboard.py`. The program will run indefinitely until the user either closes the terminal window or presses `ctrl+z` in the terminal window.

This tool has been tested with a gaming keyboard that uses the scroll key to turn on/off RGB/LED.

Please note that this is still a beta tool and more features and a GUI are planned for future releases.

## Acknowledgements

Special thanks to [damieng](https://github.com/damieng) for helping make this project possible. Be sure to check out his work!
The great developers of BlackHole, Python, Homebrew, and LadioCast to make such project possible!
