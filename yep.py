import os, sys, random, pyglet
from random import shuffle
from random import randint
from threading import Timer
from pyglet.window import key

pyglet.options['audio'] = ('openal', 'silent')
window = pyglet.window.Window()

# window.set_visible(visible=False)
window.set_caption('F R E E S T Y L E Z')

song2 = pyglet.media.load('beats/hard-2.mp3')
song3 = pyglet.media.load('beats/drop-2.mp3')
player = pyglet.media.Player()

def beatz():
    playlist = [song2]
    # playlist = [song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16]
    # shuffle(playlist)
    player.queue(playlist[0])
    # player.queue(playlist[1])
    player.play()

@player.event
def on_player_eos():
    print('repeating')
    beatz()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('exiting')
        pyglet.app.exit()

# beatz()
# pyglet.app.run()
if __name__ == "__main__":
    beatz()
    pyglet.app.run()
