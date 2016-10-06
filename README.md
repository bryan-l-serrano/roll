# roll

roll.py is a a program that allows you to "roll" many sided dice through the command line

you can do this with 

chmod +x roll.p

"./roll.py x " will roll an x sided dice and return the outcome of the dice roll so
./roll.py 20 would roll a d20

"./roll.py x y" will print the result of rolling x y-sided dice, so
"./roll.py 5 6" would roll 5d6's and return their total. 

additionally you can have the program return all of the values of the dice rolls with
"./roll.py x y z" where z can be anything. for example the output of "./roll.py 4 6 print" might be:

3
1
4
5
13

where 3,1,4, and 5 ar ethe dice rolls and 13 is the total of the dice rolls

I've started working on a D&D campaign recently, so i wrote this to assist in the many dice rolls that have to be made.
