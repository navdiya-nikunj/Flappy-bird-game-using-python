# Flappy bird game using pygame

## Video Demo:  https://youtu.be/eyVzFEjowOw


### Description:

By using python's pygame library create a 2D game name "flappy Bird".

In my `project.py` file i have imported necessary modules for the game. There is 5 function in the file all the details about file is given below.


`Global Declaration`

In global declaration part i have declared the global variables which we have to use in entire file.In global declaration part i have created two dictionaries to store the images and sounds for the game and plus i have created a screen using pygame module.

the images and sounds are located in img and sounds directory respectively.

`main Function`

In main function i am running an infinite loop which will run welcomescreen() and maingame() functions infinitely so that our images can become dynamic.


`welcomescreen function`

In this function i am running for loop to get events from the user, here i am putting three conditions

    - if user close the window or press Esc button on keyboard game will stop and program will exit
    - if user press any key except Esc then the game will start
    - if used don't do anything then i am showing the welcome image on screen

`maingame function`

This is the main function of the game so in starting i am declaring some variables which will be used furture. eg. score,player_x ..

So first i will get random pipe's cordinate to show the pipes on screen.
then i am sotring this cordinates in two dictionaries called upperpipes and lower pipes.

After that i am again geting events from the user and check if user want to exit and another condition is there that if player press UP Arrow key then it plays flap sound.

Next i am checking for crash using isCollide function.

After that i am moving pipes to left so it create dynamic effect and at the same time i am checking if pipe is out of screen then i am removing it from dictionary and adding a new pipe into dictionary.

At last i am printing the score using the numbers images in img directory.


`getrandompipe function`

This function will get two randome pipe using random library and some mathamatics, return the cordinates of them in list (lower and upper pipe)

```isCollide function```

Function return True if player hit the pipe

Thus function check for three condition.

    - if user touches the sky or ground then return true and play hit sound.
    - if user touches the upperpipes then return true and play hit sound.
    - if user touches the lowerpipe then return true and play hit sound.


#### How to play the gmae?

-  ```In this game player is a bird and it simply try to learn flying so when you press SPACE key or UP_ARROW key it will fly up.```

  [![welcome.png](https://i.postimg.cc/0yYv4N35/welcome.png)](https://postimg.cc/3kxz43Yz)

- ```During flying there are PIPE barriers which player have to cross.```

  [![Screenshot-2023-03-22-125926.png](https://i.postimg.cc/90yVjFMB/Screenshot-2023-03-22-125926.png)](https://postimg.cc/ZvYX8m69)

- ```If player got hit by barrier then GAME OVER.```

  [![Screenshot-270.png](https://i.postimg.cc/7PSyhhH3/Screenshot-270.png)](https://postimg.cc/jCq1ksJ2)


- ```if player pass the barrier then player got one point.```

  [![Screenshot-267.png](https://i.postimg.cc/mrPvs2pF/Screenshot-267.png)](https://postimg.cc/VScG918Y)



In my `test_project.py` file i have checked the functions using pytest.
## Thank You
