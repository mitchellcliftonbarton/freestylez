import os, sys, random, pyglet
from random import shuffle
from random import randint
from threading import Timer
from pyglet.window import key
import subprocess

# basic app info

pyglet.options['audio'] = ('openal', 'silent')
window = pyglet.window.Window(width=640, height=640)
window.set_caption('F R E E S T Y L E Z')
pic1 = pyglet.resource.image('grad.jpg')
pic2 = pyglet.resource.image('grad-2.jpg')
picz = [pic1, pic2]

@window.event
def on_draw():
    window.clear()
    random.choice(picz).blit(0, 0)

# rapperz

rapperz = ['Alex ', 'Agnes ', 'Kathy ', 'Bruce ', 'Fred ', 'Junior ', 'Princess ',
           'Vicki ', 'Ralph ', 'Victoria ']

# Words to use in freestyle

hype = ['about to break it down', 'about to drop some bars', 'lay down the beat', 'drop the beat', 'drop it', 'lets go', 'spin it', 'lay it down', 'pass the mic']
greetings = ['hello,', 'yo', 'yo,', 'what up', 'what up,', 'sup', 'sup', 'yep', 'hi', 'whats happening', 'whats happening,', 'whats up', 'whats up', 'yeah', 'yeah,', 'hey', 'hey,', 'uh', 'uh huh', 'yup']
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
r13 = ['ballin', 'balling', 'balla', 'calling', 'callin', 'stallin', 'crawling', 'impala', 'falling', 'apalling', 'shot callin', 'folly', 'trolly']

# themes

sports = ['ball', 'dunk', 'shoot', 'sports', 'basket', 'basketball', 'baseball', 'football', 'quarterback', 'coach', 'player', 'game', 'points', 'score', 'play', 'playing', 'soccer', 'slam dunk']
fruits = ['banana', 'orange', 'apple', 'pineapple', 'tangerine', 'melon', 'watermelon', 'grape', 'fruit', 'grapefruit', 'lemon', 'lime', 'cherry', 'strawberry', 'raspberry', 'blueberry']
veggies = ['veggies', 'vegetable', 'carrot', 'tomato', 'lettuce', 'broccoli', 'asparagus', 'pepper', 'mushroom']
art = ['paint', 'paper', 'canvas', 'pen', 'pencil', 'collage', 'collab', 'piece', 'art', 'photo', 'photograph']
landscape = ['river', 'mountain', 'plain', 'hill', 'lake', 'stream', 'rock', 'tree', 'bush', 'plant', 'flower', 'valley']
mystical = ['dragon', 'werewolf', 'wizard', 'godzilla', 'zombie', 'witch', 'dinosaur', 't rex', 'monster', 'alien', 'u f o', 'lifeform']
cars = ['audi', 'porsche', 'benz', 'mercedes', 'land rover', 'range rover', 'ferrari', 'chevy', 'subaru', 'race car', 'dragster']
animals = ['monkey', 'aardvark', 'elephant', 'tiger', 'lion', 'gazelle', 'eagle', 'spider', 'bug', 'bird', 'fish', 'shark', 'whale', 'gorilla']
thug = ['boss', 'old school', 'bawse', 'gangsta', 'fly', 'amigo', 'homy', 'friend', 'hero', 'champion', 'dawg', 'bro', 'brother', 'sister', 'mister', 'pal', 'dude', 'unstoppable']
geo = ['USA', 'south america', 'north america', 'canada', 'mexico', 'chile', 'europe', 'africa', 'asia', 'polynesia', 'china', 'antarctica', 'states', 'region', 'country', 'city', 'town']
cities = ['salt lake', 'LA', 'los angeles', 'new york', 'NY', 'atlanta', 'chicago', 'toronto', 'tokyo', 'london', 'madrid', 'rome', 'berlin', 'sao paolo', 'seattle', 'san fran', 'paris', 'egypt', 'hong kong']
countries = ['united states', 'england', 'italy', 'france', 'argentina', 'germany', 'japan', 'korea', 'new zealand', 'australia', 'russia', 'south africa', 'ghana', 'colombia', 'brazil']
money = ['dollar', 'dollar bills', 'cash', 'yo', 'coins', 'cents', 'pounds', 'euros', 'green', 'yen', 'pesos', 'benjamins', 'franklins', 'millions', 'mill', 'paper']
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'white', 'black', 'brown', 'orange', 'teal', 'burnt siena', 'yellow ochre', 'gray', 'navy', 'gold', 'silver', 'platinum', 'metallic', 'flourescent']
brands = ['google', 'facebook', 'twitter', 'nike', 'snapchat', 'insta', 'tumblr', 'adidas', 'jordan', 'supreme', 'undefeated', 'hundreds', 'vans', 'new era', 'levis', 'uni qlo', 'bape', 'ice cream', 'billionaire boys club']
shoes = ['air max', 'spizike', 'air force one', 'dunks', 'high tops', 'slip ons', 'sandals', 'foam posite', 'superstars', 'nikes', 'jordans']
bling = ['chain', 'necklace', 'two finger ring', 'piece', 'bling', 'jewels', 'watch', 'accessories', 'snap back', 'fitted', 'belt buckle', 'pin', 'rope']
teams = ['yankees', 'dodgers', 'red sox', 'lakers', 'yo', 'celtics', 'jazz', 'warriors', 'sonics', 'giants', 'mets', 'broncos', 'raiders', 'patriots', 'redskins', 'bills', 'cowboys']
mrthug = ['shorty', 'shawty', 'grill', 'dough', 'dime', 'bread', 'hustle', 'O G', 'beef', 'street cred', 'rep', 'ill', 'afro', 'cray']
marks = ['squiggle', 'circle', 'square', 'rectangle', 'pentagon', 'octogon', 'line', 'splotch', 'stain', 'cube', 'pyramid', 'box', 'crate']
chips = ['doritos', 'cheetos', 'lays', 'sour cream and onion', 'barbecue', 'tortilla chips', 'fritos', 'potato chips', 'cheddar', 'salt and vinegar', 'spicy nacho', 'nacho']
mrp = ['got money', 'got cheese', 'bling bling', 'yo', 'gold chain', 'gold and a pager', 'dont mess with me', 'i got it locked down', 'so fresh', 'so clean', 'i got it on lockdown', 'you cant believe this', 'half man half amazing']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'party', 'party time', 'hard in the paint', 'dance party', 'week', 'year', 'month', 'birthday']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
exp = ['you wouldnt believe', 'cant compete', 'cant believe it', 'you better believe it', 'ahh yeahh', 'oh yeah', 'thats right', 'how I do', 'dont trip', 'on point', 'yes sir']
mrsports = ['pass', 'give and go', 'overlap', 'run', 'i got hops', 'jumping', 'layup', 'three pointer', 'jumpshot', 'fade away', 'buzzer beater', 'underdog', 'rainbow', 'home run', 'ground rule double']
comp = ['im like', 'im like a', 'like a', 'i be like', 'like im', 'like im gonna', 'comparable to a', 'im all like', 'i be all', 'like its gonna', 'like its a', 'its like']
disgust = ['yuck', 'ew', 'gross', 'phew', 'sick', 'nasty', 'sick nasty', 'disgusting', 'stinky', 'smelly', 'dirty', 'yo', 'yeahh man']
bounce = ['bounce with it', 'let it bump', 'let it bounce', 'stacking money', 'put your hands up', 'if you feeling the beat', 'bounce with the beat', 'put your hands up in the sky', 'get your hands up']
bounce2 = ['if you dig it', 'what you saying', 'let me know', 'if you feel the vibe', 'listen up', 'listen close', 'hear me', 'started from the bottom', 'can you dig it', 'can i kick it', 'kicking it', 'made it to the top']

# random things

gadgets = ['helicopter', 'airplane', 'up high', 'in the sky', 'flying', 'submarine', 'truck', 'motorcycle', 'rocket', 'spaceship', 'fighter jet', 'tank', 'bicycle', 'trike']
clothes = ['slippers', 'sweats', 'polo', 'button up', 'dress', 'skirt', 't shirt', 'tall tee', 'linen', 'cotton blend', 'socks', 'cleats', 'boots', 'bracelet', 'belt']
js = ['jordan ones', 'jordan twos', 'jordan threes', 'jordan fours', 'jordan fives', 'jordan sixes', 'jordan sevens', 'jordan eights', 'jordan nines', 'jordan tens', 'jordan elevens', 'jordan twelves', 'jordan thirteens', 'jordan fourteens']
jstype = ['true blue', 'elephant print', 'infared', 'original', 'on ice', 'mint condition', 'retro', 'colorway', 'deadstock', 'shrink wrapped', 'flight club', 'sneakers', 'sneaker head']
sneak = ['aglets', 'beaters', 'hype beast', 'flip flop', 'hype', 'jumpman', 'lows', 'mids', 'air jordan', 'player edition', 'sample', 'boutique', 'style', 'mags']
mexp = ['for real', 'for sure', 'of course', 'there it is', 'laid it down', 'seriously', 'are you kidding', 'for serious', 'dont mess', 'dont hate', 'haters', 'brush your shoulders off']
yuup = ['how gangster is that', 'limited quantity', 'wack', 'thats wack', 'thats dope', 'dope', 'rock it', 'lame', 'rope', 'posers', 'posters', 'hating', 'make it']
yuup2 = ['swag', 'swagger', 'steeze', 'cool', 'hard to believe', 'got game', 'graphics in your fade', 'flat top', 'loser', 'mustache', 'beard', 'sideburns', 'ear ring']
rapM = ['bars', 'on the beat', 'bass line', 'chorus', 'lines', 'rhymes', 'smooth flow', 'flow', 'rhythm', 'tempo', 'poet', 'poetry', 'poetic justice', 'space jam']
masfoods = ['salad', 'steak', 'bacon', 'eggs', 'almonds', 'cashews', 'berry', 'candy', 'chocolate', 'peanut butter', 'food', 'treats']
word = ['word up', 'in the hood', 'from the hood', 'hood forever', 'cops', 'neighborhood', 'broadway', 'courtside', 'concrete jungle', 'melting pot', 'hip hop']
word2 = ['gamble', 'got that cash', 'cash under the mattress', 'cars', 'gang', 'crew', 'holla', 'holla back', 'rap star', 'ball player', 'limelight']
blah = ['water bottle', 'butter', 'cash money', 'pringles', 'gym shorts', 'necklace', 'ring', 'rock on', 'so sick', 'holla at me', 'bro']
connect = ['its a', 'feeling like a', 'acting like a', 'got rhymes like a', 'got rhymes like', 'got skills like', 'so sick like im', 'you can call me', 'you can say im']

wordz = [greetings, be, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13,
         sports, fruits, veggies, art, landscape, mystical, cars, animals, thug,
         geo, cities, countries, money, colors, brands, shoes, bling, teams, mrthug,
         marks, chips, mrp, days, months, exp, mrsports, comp, disgust, bounce, bounce2,
         gadgets, clothes, js, jstype, sneak, mexp, yuup, yuup2, rapM, masfoods, word, word2,
         blah, connect]

# songs

song2 = pyglet.resource.media('beats/breathe.mp3', streaming=False)
song3 = pyglet.resource.media('beats/everything.mp3', streaming=False)
song4 = pyglet.resource.media('beats/jazz.mp3', streaming=False)
song5 = pyglet.resource.media('beats/electric.mp3', streaming=False)
song6 = pyglet.resource.media('beats/preservation.mp3', streaming=False)
song7 = pyglet.resource.media('beats/88.mp3', streaming=False)
song8 = pyglet.resource.media('beats/93.mp3', streaming=False)
song9 = pyglet.resource.media('beats/cream.mp3', streaming=False)
song10 = pyglet.resource.media('beats/drop.mp3', streaming=False)
song11 = pyglet.resource.media('beats/far.mp3', streaming=False)
song12 = pyglet.resource.media('beats/knock.mp3', streaming=False)
song13 = pyglet.resource.media('beats/ny.mp3', streaming=False)
song14 = pyglet.resource.media('beats/ready.mp3', streaming=False)
song15 = pyglet.resource.media('beats/welcome.mp3', streaming=False)
song16 = pyglet.resource.media('beats/what.mp3', streaming=False)
song17 = pyglet.resource.media('beats/saliva.mp3', streaming=False)
player = pyglet.media.Player()

# function that shuffles and plays songs

def beatz():
    playlist = [song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16, song17]
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
    player.queue(playlist[13])
    player.queue(playlist[14])
    player.queue(playlist[15])
    player.play()

# repeat event for beatz function

def on_player_eos():
    print('repeating')
    beatz()

player.push_handlers(on_player_eos)

# rapping stuff

barLen = list(range(1,10))
swTm = [30.0, 45.0, 60.0, 20.0, 75.0, 80.0]
timez = [.5, .75, 1.0, 1.5, 1.75]
rates = ['175', '175', '100', '50', '175', '210', '300', '150', '70', '175', '200', '60', '175', '175', '175']
lead = random.choice(rapperz)
barTimer = None
r = None

# closing event function

def close():
    r.terminate()
    rapperTimer.cancel()
    barTimer.cancel()
    print('exiting')
    pyglet.app.exit()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        close()
    elif symbol == key.N:
        window.clear()
        random.choice(picz).blit(0, 0)

@window.event
def on_close():
    close()

# choosing rapper function

def choozRapper():
    global rapperTimer
    rapperTimer = Timer(random.choice(swTm), choozRapper)
    global lead
    lead = random.choice(rapperz)
    rapperTimer.start()

rapperTimer = Timer(random.choice(swTm), choozRapper)
rapperTimer.start()

# rapping function

def rap():
    global barTimer
    barTimer = Timer(random.choice(timez), rap)
    bar = ' '.join(random.choice(wordz[randint(0,58)]) for _ in range(random.choice(barLen)))
    global r
    r = subprocess.Popen('say -v ' + lead + '-r ' + random.choice(rates) + ' ' + bar, shell=True)
    r.wait()
    print(bar)
    sys.stdout.flush()
    barTimer.start()

def freestyle():
    beatz()
    t = Timer(1.5, rap)
    t.start()

def hypeIt():
    subprocess.run('say ' + random.choice(hype), shell=True)
    freestyle()


if __name__ == "__main__":
    hypeIt()
    pyglet.app.run()
