# Pokemon Battle Sim (python)

This is a text based Pokemon battling simulator, as obvious as that is by now. This program takes elements from both the mainline games and the trading card game, so it ends up being its own thing, in a way.

Fight with various trainers. If you're up for the challenge, take on the 8 gym leaders and meet with the champion. Bill will (try to) help you along the way.

(currently a big work in progress)


## FAQ

#### How many pokemon/trainers are there?

There are about 7 pokemon and only 3 trainers currently, 2 normal and one gym leader. More will be added in the future. Currently unused, but the JSON data exists for them.

#### Why?

why not?



## Authors

- Cleo C


## Files
#### battlesim.py
Where all the fun happens.  
The main program is composed of two parts: python and JSON. The reason I went with JSON is that it's easier to store data.  
#### pkmn.json
All the Pokemon data is store here, their names, types, and such. Instead of 4, I limited their movesets to 3 to balance it out a little bit. Each pokemon has two offending moves and one move that will either increase their stat or decrease their opponents stats, and apply status.
#### dialogue.json
This stores data on what all the characters say depending on what situation they're in, as well as check if they are a gym leader or not. The current plan is to also use this to assign them Pokemon. 
#### logFile.json
Keeps track on all your wins, loses, badges, etc. It is updated each time you sucessfully complete a battle.
