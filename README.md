# installation
linux *git clone https://github.com/williamaerus/python-weather*

windows *unzip the file and run from terminal*
# configuration
to make this script work you have to connect to this website and start a free account https://openweathermap.org/api then go to *my API keys"* and copy it

then edit the code and change the variable API_KEY = "" at line 4 with API_KEY = "your API"

CHANGE THE API KEY IN BOTH FILES(MAIN AND ADVANCED)!!!

ps: you may not have installed the requests repository the command to download it is *pip install requests*
pps: probably not even the json repository the command for this one is *pip install json*

# differences between main and advanced

in the main file the script shows: *coords weather temperature*

in the advanced file the script shows: *coords weather temperature humidity pressure wind_speed timezone* 

# how to use it

STANDARD VERSION

you can start the standard version from the terminal with 

*python3 main.py* on linux or 

*python main.py* on windows

then write the name of the city that you want to check (not all cities are listed) and the game is done you have the weather info displayed directly on your terminal

ADVANCED VERSION

you can start the advanced version from the terminal with 

*python3 main.py* on linux or

*python main.py* on windows

then write the name of the city that you want to check (not all cities are listed) and the game is done you have the weather info displayed directly on your terminal
