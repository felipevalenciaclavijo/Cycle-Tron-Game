# Cycle
Cycle is a game where players try to cut each other off using cycles that leave a trail behind them.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

python3 -m pip install raylib

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 snake 

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:

root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
    +-- casting           
      +-- actor                     (traits to use for actors)
      +-- cast                      (keeps track of what is in play)
      +-- food  CHANGE?             ()
      +-- score                     (keeps track of score)
      +-- cycle                     (creates cycles)
    +-- directing         
      +-- director                  (director of game)
    +-- scripting
      +-- action
      +-- control_actors_action     (controls snake)
      +-- draw_actors_action        (create actors in game space)
      +-- handle_collisions_action  (control what happens when when things collide)
      +-- move_actors_action        (control movement in game space)
      +-- script                    (keep track of actions)
    +-- services
      +-- keyboard_service          (gets player input for movement)
      +-- video_service             (draws game on screen)
    +-- shared
      +-- color                     (sets colors & opacity)
      +-- point                     (provides info about where actors are located)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)


## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
## Authors
*Logan Andrus lbandrus@byui.edu
*Keeley Imlah wil11070@byui.edu
*Felipe Valencia fevacla@byui.edu
*Kathryn Thompson thompson21057@byui.edu
*Morgan Luke morganluke@byui.edu

*Team 9 CSE-210 Winter 2022
