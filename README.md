# Final Project Report

* Student Name: Yumei Wang
* GitHub Username: mammon0120
* Semester: Fall 2023
* Course: 5001


## Description
1. General Overview
This is a board game. The board initially has 30 squares, including a starting point and an end point.
At the beginning of the game, player has 100 HP(health points) and start at the starting point on the board.
Player rolls a die to determine the number of squares to move forward.
During the movement, certain squares on the board may trigger rewards or penalties, either reducing the player's HP or causing the player to move forward or backward. 
If a player successfully reaches the endpoint before his HP reaches 0, he wins the game. 
If a player's HP decrease to 0 before reaching the endpoint, the game is lost.
2. Program Structure
The program consists of a total of 4 code files, each serving different functionalities.
   (1) game_view.py
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
Test cases for function load_setting.
   (5)test_history_1.txt & test_history_2.txt
Test cases for function load_history.
   (6)test_record_1.txt & test_record_2.txt
Test records of functions and Class Player.


## Key Features
1. I use Class to create Player type to store player's information, and establish methods to record and modify the player's HP and position.
2. I store the configuration information for rewards and penalties in a txt file.
Each time the game starts, this txt file is read and a dictionary is created to store the information, using key value pairs to record what each square corresponds to in terms of rewards or penalties.
3. If the player quits the game in the middle, he can choose to save this unfinished game, and at the beginning of the next game, he can choose whether to continue the previous game.
If he inputs 'Y' for yes, the game history will be read and he can continue playing. 
If he inputs other words, the game history will be cleared, and the player can start a new game.
If a game progresses to the end, the game history will be cleared.
If the game history is empty but the player choose to continue playing, the error message will be showed and the player need to start a new game.
4. I use a while loop to run this game. As long as the player does not input 'Q', the game will continue.
5. I simulate the result of rolling the dice by returning a random number between 1 and 6 through a function. Based on the dice value, the player moves a corresponding number of squares.
After each move, the game checks whether the player's current square triggers a reward or penalty. If it does, the game invokes methods from Class Player to adjust the player's HP or position.
Then the game checks whether the player's HP is less or equal to 0 or position is greater or equal to 30. If it is, then game ends.


## Guide
You can just run the 'game_view.py', then game will start.


## Installation Instructions
Players of this game don't need to install any other libraries.


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.
file name: game_view.py
```python
# ask the player if he wants to continue the previous game
check_load = input(ASK_LOAD)

# if yes, load the game history file and create the player information
if check_load == 'Y':
  # check if there is a game history
  if game_run.load_history():
      name, game_hp, position = game_run.load_history()
      player = Player(name, game_hp, position)
  else:
      # if something wrong with the file, start a new game
      player = check_start()
else:
  # if no, clean game history and get ready to start a new game
  game_run.clean_history()
  player = check_start()
```
At the beginning of the game, the player can choose whether continue playing the previous game. If he input yes, then I need to check if there exist a game record.
If there is, then the game history will be read. If there isn't, then an error message must be showed and the player need to start a new game.
If the player want to start a new game, the old game record will be cleared.

file name: game_view.py
```python
 # now check whether a reward or penalty is triggered
if player.position in setting:
    # if it does, find out the type and the value and print it out
    trigger = setting[player.position].split(" ")
    trigger_type = trigger[0]
    value = int(trigger[1])
    print_trigger(trigger_type, value)
    # adjust the player's HP or position
    if trigger_type == "hp":
        player.change_hp(value)
    elif trigger_type == "position":
        player.change_position(value)
else:
    print("-----Nothing Happened-----")
```
'setting' is the name of a dictionary. After each move, I need to check whether the player triggers a reward or penalty.
If the value of player's position is in the key values of the dictionary, then return the value of the key.
Then according to the type and value of this trigger, adjust the player's HP or position.


### Major Challenges
At the beginning, I was hesitant about how to set up rewards and penalties in the game. I can use a series of if statements, such as if the player reaches a certain square, then display a reward.
However, it's really a bad design and needs a lot of work, making it less conductive to later modifications.
After some thought, I decided to use a dictionary. Its key-value pairs can efficiently express the association between a square and its corresponding reward or penalty.
Additionally, I use a text file to store the setting information. Reading the file only at the start of the game makes it easily modify settings and avoid unnecessary storage memory.


## Example Runs
I documented running the project in the following file:
(1)documented_run_1.txt 
In this example, the player quits the game in the middle of the game and save the progress.
(2)documented_run_2.txt
In this example, the player continue playing the previous unfinished game and wins.
(3)documented_run_3.txt
In this example, the player starts a new game and plays till game ends.


## Testing
I use doctest to test my functions and use unittest to test the Class Player. The outputs are in the following files:
(1)test_record_1.txt
(2)test_game_setting.py and test_record_2.txt


> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
If I had more time, I would make this game more complex and exciting. For example, I might create a visualized version.


## Final Reflection
In this semester, I've learned the basics of the Python programming language. Now, I can use Python to create simple programs and apply it to solve mathematical problems in my 5002 course, significantly improving the efficiency and accuracy of calculations.
In the upcoming period, I plan to dedicate more time to deepen my understanding of Python by apply it to real-world projects, integrating theoretical knowledge with practical applications.
I believe that continuous coding practice is essential for mastering programming skills rather than just reading books.
In the next semester, I'm going to learn Java and C, and I believe that the foundation laid through Python learning will be beneficial for my future study.