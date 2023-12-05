# Final Project Report

* Student Name: Yumei Wang
* Github Username: mammon0120
* Semester: Fall 2023
* Course: 5001


## Description 
General overview of the project, what you did, why you did it, etc. 
1. General Overview
This is a board game. The board initially has 30 squares, including a starting point and an end point.
At the beginning of the game, player has 100 HP(health points) and start at the starting point on the board.
Player rolls a die to determine the number of squares to move forward.
During the movement, certain squares on the board may trigger rewards or penalties, either reducing the player's HP or causing the player to move forward or backward. 
If a player successfully reaches the endpoint before his HP reaches 0, he wins the game. 
If a player's HP decrease to 0 before reaching the endpoint, the game is lost.
2. Program Structure
The program consists of a total of 4 code files, each serving different functionalities.
  （1) game_view.py
This is the main file for running this game, containing the core part of the code.
   (2)game_run.py
This file includes the setting part of functions required for various game operations, playing a supportive role in the game's execution.
   (3)game_setting.py
In this file, I define a Class Player to store the player's information and create methods to adjust player's HP and position.
   (4)test_game_setting.py
It's the test function of game_setting.py
3. TXT Files Introduction
   (1)game_history.txt
This txt file is used to store the previous game's information.
If a player chooses to save the unfinished game progress in the middle of the game, the information will be stored in this file.
If the next game starts, and the player wants to continue the previous game, the record in this file will be read.
If the player wants to start a new game, or if a game session ends, the data in this file will be cleared.
   (2)trigger_setting.txt
During the game, certain squares on the board may trigger rewards or penalties. These setting information are stored in this file.
   (3)help_message.txt
I store the help and instructional information for this game in a separate file due to its length.
   (4)test_setting.txt
The test cases for function load_setting.
   (5)test_history_1.txt & test_history_2.txt
Test cases for function load_history.
   (6)test_record_1.txt & test_record_2.txt
Test records of functions and Class Player.


## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 


## Installation Instructions
Players of this game don't need to install any other libraries.


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 


### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)


## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 


> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.