import winsound, sys

path = ".\\sound\\{}"
sounds = ['can_they_do_this.wav', 'come_out.wav', 'do_you_wanna.wav', 'eagle.wav', 'i_want_turn.wav', 'play_time.wav', 'this_is_fun.wav', 'final_sound']

def beep(audio):
    winsound.PlaySound(path.format(audio), winsound.SND_FILENAME)
