#importing things

import os, sys, random, pyglet
# import sched, time
from random import shuffle
from random import randint
from threading import Timer

pyglet.options['audio'] = ('openal', 'silent')

#rapperz

# rapperz = ['Alex', 'Agnes', 'Kathy', 'Bruce', 'Fred', 'Junior', 'Princess', 'Vicki', 'Ralph', 'Victoria']

# Words to use in freestyle
hype = ['about to break it down', 'about to drop some bars', 'lay down the beat', 'drop the beat', 'drop it', 'lets go']
greetings = ['hello', 'what up', 'sup', 'yep', 'hi', 'whats happening', 'whats up', 'yeah', 'hey', 'uh', 'uh huh', 'yup']
be = ['is', 'was', 'will be', 'is not', 'was not', 'will not be', 'will never be', 'never was', 'never is', 'always is', 'always will be']
r1 = ['mic', 'like', 'spike', 'bike', 'pike', 'turnpike', 'ride', 'slide', 'tide', 'pie', 'my', 'cry', 'tie', 'sty', 'pry', 'dry']
r2 = ['tree', 'me', 'tee', 'see', 'plea', 'treat', 'meet', 'seat', 'feat', 'beat', 'beats', 'meats', 'pleat', 'treat', 'pee', 'dee', 'flee']
r3 = ['rock', 'mock', 'tock', 'sock', 'clock', 'knock', 'hard knock', 'socks', 'block', 'blocks', 'pot', 'trot', 'sought']
r4 = ['bark', 'mark', 'spark', 'stark', 'park', 'lark', 'dark', 'fart', 'part', 'apart', 'dart', 'mart', 'cart', 'tart']

wordz = [greetings, be, r1, r2, r3]

# beatz

song1 = pyglet.media.load('beats/heart-of-the-city.mp3')
song2 = pyglet.media.load('beats/breathe.mp3')
song3 = pyglet.media.load('beats/everything.mp3')
song4 = pyglet.media.load('beats/jazz.mp3')
song5 = pyglet.media.load('beats/electric.mp3')
player = pyglet.media.Player()

# Play beatz

def beatz():
    playlist = [song1, song2, song3, song4, song5]
    shuffle(playlist)
    player.queue(playlist[0])
    player.queue(playlist[1])
    player.queue(playlist[2])
    player.queue(playlist[3])
    player.queue(playlist[4])
    player.play()
    print('playing beatz')

# rapping function

barLen = list(range(1,10))

# print(barLen)

# lead = random.choice(rapperz)

def rap():
    # rando1 = randint(0,4)
    bar = ' '.join(random.choice(wordz[randint(0,4)]) for _ in range(random.choice(barLen)))
    # os.system('say -v ' + lead + ' ' + bar)
    os.system('say ' + bar)
    print(bar + ' rap1')
    sys.stdout.flush()
    t = Timer(1.0, rap)
    t.start()

# def rap2():
#     rando1 = randint(0,2)
#     bar = ' '.join(random.choice(wordz[rando1]) for _ in range(2))
#     os.system('say ' + bar)
#     print(bar + ' rap2')
#     sys.stdout.flush()
#     t = Timer(1.5, random.choice(rapping))
#     t.start()

# def rap3():
#     rando1 = randint(0,2)
#     bar = ' '.join(random.choice(wordz[rando1]) for _ in range(3))
#     os.system('say ' + bar)
#     print(bar + ' rap2')
#     sys.stdout.flush()
#     t = Timer(1.5, random.choice(rapping))
#     t.start()

# rapping = [rap, rap2, rap3]
def freestyle():
    beatz()
    t = Timer(1.5, rap)
    t.start()

def hypeIt():
    # bar = ' '.join(random.choice(wordz[rando1]) for _ in range(random.choice(barLen)))
    # os.system('say -v ' + lead + ' ' + random.choice(hype))
    os.system('say ' + random.choice(hype))
    freestyle()

hypeIt()

