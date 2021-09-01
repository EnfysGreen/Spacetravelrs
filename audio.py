from kivy.core.audio import SoundLoader


def init_audio(self):
    self.sound_begin = SoundLoader.load("audio/begin.wav")
    # self.sound_galaxy = SoundLoader.load("audio/galaxy.wav")
    self.sound_gameover_impact = SoundLoader.load("audio/gameover_impact.wav")
    self.sound_gameover_voice = SoundLoader.load("audio/gameover_voice.wav")
    self.sound_music1 = SoundLoader.load("audio/SUN_IN_A_IDEA.mp3")
    self.sound_restart = SoundLoader.load("audio/restart.wav")

    self.sound_music1.volume = 0.25
    self.sound_begin.volume = .1
    # self.sound_galaxy.volume = .25
    self.sound_gameover_voice.volume = .1
    self.sound_restart.volume = .1
    self.sound_gameover_impact.volume = .06
