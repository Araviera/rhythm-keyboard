
# Rhythm-keyboard


this python command-line tool listens to the sound of your mac then turns on/off the keyboard LED depending on the level of voulme playing, would look cool in things like [music](https://www.youtube.com/watch?v=dQw4w9WgXcQ).


## Usage
head to [releases](https://github.com/MomenBreuer/rhythm-keyboard/releases) then head to the latest version and click on `rhythm.keyboard.zip` to downlaod the tool.

after downloading the tool extract the zip file and open the termnial inside the path of the extracted folder and run

`pip install -r requirements.txt`

if did not work for some reason, then try

`pip3 install -r requirements.txt`

that will download the needed python libraries for the python code to run.

after that run
`python rhythm_keyboard.py` to run the program, if did not work try 
`python3 rhythm_keyboard.py`.

the program will run forever until the user either close the terminal window or press `⌘+z` in terminal window.


tested with gaming keyboard that uses the scroll key to turn on/off RGB/LED

this is still a pretty much a beta tool, more features and GUI is planned for the future.
##
Special thanks to [damieng](https://github.com/damieng) for helping me making this project possible, go check his work!
