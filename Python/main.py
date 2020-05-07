from node import *
import maze as mz
import score
import interface
import time

import numpy as np
import pandas
import time
import sys
import os


def main():
    maze = mz.Maze("data/small_maze.csv")
    point = score.Scoreboard("data/UID.csv", "team_NTUEE", sys.argv[1])
    interf = interface.interface()
    # TODO : Initialize necessary variables

    if (sys.argv[1] == '0'):
        print("Mode 0: for treasure-hunting with rule 1")
        # TODO : for treasure-hunting with rule 1, which encourages you to hunt as many scores as possible
        maze.getStartPoint()
        while len(maze.deadend) != 0:
            path = maze.strategy(maze.now)
            direct = []
            while len(path) != 0:
                direct.append(maze.getAction(maze.now))
            message_L = []
            while len(direct) != 0:
                message.append(interf.save_action(direct.pop(0)))
            message = ''.join(message_L)
            interf.send_action(message)

            while True:
                receive = interf.SyrialReadString()
                if receive == '':
                    pass
                else:
                    UID = interf.get_UID()
                    point.add_UID(UID)
                    point.getCurrentScore()
                    break

    elif (sys.argv[1] == '1'):
        print("Mode 1: for treasure-hunting with rule 2")
        # TODO : for treasure-hunting with rule 2, which requires you to hunt as many specified treasures as possible
        maze.getStartPoint()
        while len(point.sequence) != 0:
            path = maze.strategy_2(maze.now, point.sequence.pop(0))
            direct = []
            while len(path) != 0:
                direct.append(maze.getAction(maze.now))
            message_L = []
            while len(direct) != 0:
                message.append(interf.save_action(direct.pop(0)))
            message = ''.join(message_L)
            interf.send_action(message)

            while True:
                receive = interf.SyrialReadString()
                if receive == '':
                    pass
                else:
                    UID = interf.get_UID()
                    point.add_UID(UID)
                    point.getCurrentScore()
                    break



        
    elif (sys.argv[1] == '2'):
        print("Mode 2: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        while True:
            
            print(interf.get_message())
        

if __name__ == '__main__':
    main()
