import os
import threading as th
from time import sleep
import pygame


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("./yq.wav")
    pygame.mixer.music.play()


def start_seewo():
    sleep(16)
    os.system("D:\\EasiNote5\\swenlauncher\\swenlauncher.exe")
    sleep(10)


if __name__ == "__main__":
    play = th.Thread(target=play_sound)
    seewo_start = th.Thread(target=start_seewo)
    play.start()
    seewo_start.start()
    play.join()
    seewo_start.join()
