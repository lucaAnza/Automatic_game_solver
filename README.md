# What is "Automatic Game Solver"

It a software that is able to autonomously play an online game, using pixel analisys and decision making algoritms.
It is a 100% *Python* software.

## Dependencies

· Windows 10/11  
· Python ( v > 3.0)  
· Bluestacks -> [Bluestacks download](https://www.bluestacks.com/it/index.html)  
· Pip3 package manager  

  
  
## Main features ( Refers to V4 )

### 1. Pixel analisys

Made with OpenCV, is able to recognise the different between object in a specific set.

<img src = "media/pixel_analisys.png" width="35%"></img>

### 2. Game solver

Algorithm that takes an input matrix of objects and returns the best move.

```mermaid
graph LR;
    A(Input) -- Matrix --> Algoritm;
    Algoritm -- Moves --> B(Output)
```

### 3. Game controller

Create macro, using *pyautogui*, that can make the moves in the game.

![GIF](media/gif.mp4)

### 4. Notification interface

Using Discord Webhook the bot is able to update his status.  




## Modules interaction

· Each module is called from Main.py

```mermaid
sequenceDiagram
Bluestacks instance ->> analyseBot.py: Screenshot.png
Note right of Bluestacks instance: Screen made by<br><screenBot.py>

analyseBot.py->>solverBot.py: Int matrix[]
Note right of solverBot.py: solverBot try to<br>Understand the best<br>moves to do.
solverBot.py-->> analyseBot.py:Moves
Note right of analyseBot.py: Moves is launched<br>from <game_controller.py>
analyseBot.py-->>Bluestacks instance: Moves
Note right of Bluestacks instance: Every 2k iteration<br>is sent a discord webhook<br>by <webhook.py>

```

