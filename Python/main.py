from node import *
import maze as mz
import score
import interface
import time
import threading

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
        message_L = []
        direct_L = []
        while len(maze.deadend) != 0:
            path = maze.strategy(maze.now)
            while len(path) != 0:
                direct_L.append(maze.getAction(maze.now_d, maze.now, path.pop(0)))
            
        while len(direct_L) != 0:
            message_L.append(interf.save_action(direct_L.pop(0)))
            
        message = ''.join(message_L)
        interf.send_action(message)
        
        while True:
            UID = interf.get_UID()
            if UID != 0:
                point.add_UID(UID)
                point.getCurrentScore()

    elif (sys.argv[1] == '1'):
        print("Mode 1: for treasure-hunting with rule 2")
        # TODO : for treasure-hunting with rule 2, which requires you to hunt as many specified treasures as possible
        maze.getStartPoint()
        message_L = []
        direct_L = []
        while len(point.sequence) != 0:
            path = maze.strategy_2(maze.now, point.sequence.pop(0))
            while len(path) != 0:
                direct_L.append(maze.getAction(maze.now_d, maze.now, path.pop(0)))
        while len(direct_L) != 0:
            message_L.append(interf.save_action(direct_L.pop(0)))
        
        message = ''.join(message_L)
        interf.send_action(message)   

        while True:
            UID = interf.get_UID()
            if UID != 0:
                point.add_UID(UID)
                point.getCurrentScore()



        
    elif (sys.argv[1] == '2'):
        print("Mode 2: Self-testing mode.")
        # TODO: You can write your code to test specific function.
        time.sleep(1)
        interf.send_action('goe')
        #readThread = threading.Thread(target=interf.get_UID())
        #readThread.setDaemon(True)
        #readThread.start()
        while True:
            mes = input()
            interf.send_action(mes)
        

if __name__ == '__main__':
    main()
