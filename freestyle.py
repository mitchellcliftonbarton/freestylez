#importing things

import os, sys, random, pyglet
from random import shuffle
from random import randint
from threading import Timer

pyglet.options['audio'] = ('openal', 'silent')

#rapperz

# rapperz = ['Alex', 'Agnes', 'Kathy', 'Bruce', 'Fred', 'Junior', 'Princess', 'Vicki', 'Ralph', 'Victoria']

# Words to use in freestyle
hype = ['about to break it down', 'about to drop some bars', 'lay down the beat', 'drop the beat', 'drop it', 'lets go', 'spin it', 'lay it down']
greetings = ['hello,', 'what up', 'what up,', 'sup', 'sup', 'yep', 'hi', 'whats happening', 'whats happening,', 'whats up', 'whats up', 'yeah', 'yeah,', 'hey', 'hey,', 'uh', 'uh huh', 'yup']
be = ['is', 'was', 'will be', 'is not', 'was not', 'will not be', 'will never be', 'never was', 'never is', 'always is', 'always will be', 'I am', 'I be', 'we be', 'they be']
r1 = ['mic', 'like', 'spike', 'bike', 'pike', 'turnpike', 'ride', 'slide', 'tide', 'pie', 'my', 'cry', 'tie', 'sty', 'pry', 'dry']
r2 = ['tree', 'me', 'tee', 'see', 'plea', 'treat', 'meet', 'seat', 'feat', 'beat', 'beats', 'meats', 'pleat', 'treat', 'pee', 'dee', 'flee']
r3 = ['rock', 'mock', 'tock', 'sock', 'clock', 'knock', 'hard knock', 'socks', 'block', 'blocks', 'pot', 'trot', 'sought']
r4 = ['bark', 'mark', 'spark', 'stark', 'park', 'lark', 'dark', 'fart', 'part', 'apart', 'dart', 'mart', 'cart', 'tart']
r5 = ['thug', 'mug', 'tug', 'rug', 'snug', 'pug', 'slug', 'plug', 'sun', 'ton', 'run', 'spun', 'done', 'fun', 'won']
r6 = ['cat', 'tat', 'tats', 'mat', 'rat', 'splat', 'tap', 'nap', 'rap', 'rapping', 'pat', 'gnat', 'slap', 'trap', 'map', 'sap', 'dat', 'spat', 'bat', 'tap']
r7 = ['spit', 'knit', 'bit', 'sit', 'pit', 'mit', 'never quit', 'quit', 'tip', 'sip', 'dip', 'fit', 'equip', 'equipped', 'rip', 'ripped']
r8 = ['train', 'main', 'cane', 'rain', 'sane', 'plain', 'bane', 'dane', 'profane', 'propane', 'wane', 'sprain', 'crane', 'explain', 'twain']
r9 = ['got', 'rot', 'not', 'spot', 'pop', 'top', 'sop', 'mop', 'crop', 'bop', 'beep bop', 'beep', 'bought', 'caught', 'dot']
r10 = ['ready', 'steady', 'spaghetti', 'teddy', 'petty', 'yeti', 'many', 'confetti', 'penny', 'pennies', 'benny']
r11 = ['find', 'wind', 'rewind', 'kind', 'mind', 'bind', 'rind', 'blind', 'twine', 'mine', 'sign', 'wine', 'time', 'rhyme', 'rhymes']
r12 = ['rollin', 'bowlin', 'patrol', 'rovin', 'roving', 'rolling', 'riding', 'cruising', 'sliding', 'slipping', 'tripping', 'trip']

# themes
sports = ['ball', 'sports', 'basket', 'basketball', 'baseball', 'football', 'quarterback', 'coach', 'player', 'game', 'points', 'score', 'play', 'playing', 'soccer']
fruits = ['banana', 'orange', 'apple', 'pineapple', 'tangerine', 'melon', 'watermelon', 'grape', 'fruit', 'grapefruit', 'lemon', 'lime', 'cherry', 'strawberry', 'raspberry', 'blueberry']
veggies = ['veggies', 'vegetable', 'carrot', 'tomato', 'lettuce', 'broccoli', 'asparagus', 'pepper', 'mushroom']
art = ['paint', 'paper', 'canvas', 'pen', 'pencil', 'collage', 'collab', 'piece', 'art', 'photo', 'photograph']
landscape = ['river', 'mountain', 'plain', 'hill', 'lake', 'stream', 'rock', 'tree', 'bush', 'plant', 'flower', 'valley']
mystical = ['dragon', 'werewolf', 'wizard', 'godzilla', 'zombie', 'witch', 'dinosaur', 't rex', 'monster', 'alien', 'u f o', 'lifeform']
cars = ['audi', 'porsche', 'benz', 'mercedes', 'land rover', 'range rover', 'ferrari', 'chevy', 'subaru', 'race car', 'dragster']
animals = ['monkey', 'aardvark', 'elephant', 'tiger', 'lion', 'gazelle', 'eagle', 'spider', 'bug', 'bird', 'fish', 'shark', 'whale', 'gorilla']

wordz = [greetings, be, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, sports, fruits, veggies, art, landscape, mystical, cars, animals]

# beatz

song2 = pyglet.media.load('beats/breathe.mp3')
song3 = pyglet.media.load('beats/everything.mp3')
song4 = pyglet.media.load('beats/jazz.mp3')
song5 = pyglet.media.load('beats/electric.mp3')
song6 = pyglet.media.load('beats/preservation.mp3')
song7 = pyglet.media.load('beats/88.mp3')
song8 = pyglet.media.load('beats/93.mp3')
song9 = pyglet.media.load('beats/cream.mp3')
song10 = pyglet.media.load('beats/drop.mp3')
song11 = pyglet.media.load('beats/far.mp3')
song12 = pyglet.media.load('beats/knock.mp3')
song13 = pyglet.media.load('beats/ny.mp3')
song14 = pyglet.media.load('beats/ready.mp3')
song15 = pyglet.media.load('beats/welcome.mp3')
song16 = pyglet.media.load('beats/what.mp3')
player = pyglet.media.Player()

# Play beatz

def beatz():
    playlist = [song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16]
    shuffle(playlist)
    player.queue(playlist[0])
    player.queue(playlist[1])
    player.queue(playlist[2])
    player.queue(playlist[3])
    player.queue(playlist[4])
    player.queue(playlist[5])
    player.queue(playlist[6])
    player.queue(playlist[7])
    player.queue(playlist[8])
    player.queue(playlist[9])
    player.queue(playlist[10])
    player.queue(playlist[11])
    player.queue(playlist[12])
    player.queue(playlist[13])
    player.queue(playlist[14])
    player.play()
    print('playing beatz')

# rapping function

barLen = list(range(1,10))

# print(barLen)

# lead = random.choice(rapperz)

timez = [.5, .75, 1.0, 1.5, 2.0]

def rap():
    # rando1 = randint(0,4)
    bar = ' '.join(random.choice(wordz[randint(0,21)]) for _ in range(random.choice(barLen)))
    # os.system('say -v ' + lead + ' ' + bar)
    os.system('say ' + bar)
    print(bar)
    sys.stdout.flush()
    t = Timer(random.choice(timez), rap)
    t.start()
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
