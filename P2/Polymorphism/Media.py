class MP3File:
    def play(self):
        print("Playing audio: Decoding MP3 stream...")

class MP4File:
    def play(self):
        print("Playing video: Rendering H.264 video stream...")

class Guitar:
    def play(self):
        print("Strumming strings...")

def start_media(media_object):
    media_object.play()

mp3 = MP3File()
mp4 = MP4File()
gibson = Guitar()

start_media(mp3)
start_media(mp4)
start_media(gibson) # as Guitar has play() so start_media() doesn't make difference