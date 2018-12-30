try:
    sys.stdout.close()
except:
    pass
try:
    sys.stderr.close()
except:
    pass


#import pyglet
#pyglet.options['audio'] = ('pulse', 'silent')
import pyglet.media

player = pyglet.media.Player()
player.queue(pyglet.media.load("http://www.stephaniequinn.com/Music/Allegro%20from%20Duet%20in%20C%20Major.mp3") )
player.play()
except IOError as e:
    print e.strerror()
