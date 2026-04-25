# Building a tic tac toe game environment for 
# 

import gymnasium as gym
import numpy as np 

class TicTacToe(gym.Env):
    def __init__(self, render_mode=None):
        self.observation_space = gym.spaces.Box(-1, 1, shape = (9,), dtype=np.int32 )
        self.action_space = gym.spaces.Discrete(9)
        self.render_mode = render_mode
        self.board = np.zeros(9, dtype=np.int32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.board = np.zeros(9, dtype=np.int32)
        observation = self.board
        info = {}
        if self.render_mode == "human":
            self.render()
        return observation, info 

    def render(self):
        print(self.board.reshape((3,3)))

    def close(self):
        pass

    def step(self, action):
        if self.board[action] != 0:
            return self.board, -10, True, False, {"msg": "Illegal move"}
        self.board[action] = 1

        terminated, reward = self._check_game_over()
        


    def _check_game_over(self):
        places =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]
        for place in places:
            if self.board[place[0]] == self.board[place[1]] == self.board[place[1]] != 0:
                # if 1, agent wins, 0 opponent wins
                return True, (1 if self.board[combo[0]] == 1 else -1)    
    
        if 0 not in self.board:
            return True, 0 # no moves draw 
    
        return False, 0. # no reward

game = TicTacToe(render_mode="human")
game.render()
