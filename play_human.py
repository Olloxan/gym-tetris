
"""A script to play the environment with a keyboard."""
import os

from gym.utils.play import play
import gym_tetris


# return a sorted tuple instead of a sorted list
sorted_tuple = lambda x: tuple(sorted(x))


# create a directory to write screen captures to
output_dir = 'screen_capture'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Mapping of buttons on the NES joy-pad to keyboard keys
down =  ord('s')
left =  ord('a')
right = ord('d')
rot_l = ord('q')
rot_r = ord('e')


# A mapping of pressed key combinations to discrete actions in action space
keys_to_action = {
    (): 0,
    (left, ): 1,
    (right, ): 2,
    (down, ): 3,
    (rot_l, ): 4,
    (rot_r, ): 5,
    sorted_tuple((left, down, )): 6,
    sorted_tuple((right, down, )): 7,
    sorted_tuple((left, rot_l, )): 8,
    sorted_tuple((right, rot_l, )): 9,
    sorted_tuple((left, rot_r, )): 10,
    sorted_tuple((right, rot_r, )): 11,
}


# Create the environment and play the game.
env = gym_tetris.make('Tetris-v0')
play(env, keys_to_action=keys_to_action, fps=25)