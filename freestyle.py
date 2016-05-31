#importing things

import os
import sched, time

# Words to use in freestyle

words = ['hello', 'what up babe']

# Timer to say words

s = sched.scheduler(time.time, time.sleep)
def rap():
    os.system('say ' + words[1])
    print words[1]
    s.enter(1, 1, rap, ())

s.enter(1, 1, rap, ())
s.run()