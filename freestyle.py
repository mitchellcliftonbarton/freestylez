#importing things

import os
import sched, time
import random
from random import shuffle
from random import randint
import pyglet

pyglet.options['audio'] = ('openal', 'silent')

# Words to use in freestyle

greetings = ['hello', 'what up', 'sup', 'yep', 'hi', 'whats happening', 'whats up', 'yeah', 'hey', 'uh', 'uh huh', 'yup']
be = ['is', 'was', 'will be', 'is not', 'was not', 'will not be', 'will never be', 'never was', 'never is', 'always is', 'always will be']
r1 = ['mic', 'like', 'spike', 'bike', 'pike', 'turnpike', 'ride', 'slide', 'tide', 'pie', 'my', 'cry', 'tie', 'sty', 'pry', 'dry']

wordz = [greetings, be, r1]

# beatz

song1 = pyglet.media.load('beats/heart-of-the-city.mp3')
song2 = pyglet.media.load('beats/breathe.mp3')
player = pyglet.media.Player()

# Play beatz

def beatz():
    # os.system('find beats | gshuf | while read; do echo "$REPLY"; afplay "$REPLY"; wait; done')
    playlist = [song1, song2]
    shuffle(playlist)
    player.queue(playlist[0])
    player.queue(playlist[1])
    player.play()
    print('playing beatz')

# Timer to say words

s = sched.scheduler(time.time, time.sleep)

# rapping function

def rap():
    # os.system('say ' + words[1])
    bar = ' '.join(random.choice(wordz[randint(0,2)]) for _ in range(randint(0,6)))
    # print (random.choice(greetings))
    os.system('say ' + bar)
    print(bar)
    s.enter(1, 1, rap, ())

s.enter(1, 1, rap, ())
beatz()
s.run()