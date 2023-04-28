import pygame

pygame.mixer.init()
pygame.mixer.music.load('lagtrain2.mp3')


with open("frames6976.bin", "rb") as f:
    import serial
    import time

    ps = serial.Serial(
        port='COM3',
        baudrate=9600
    )

    time.sleep(2)

    pygame.mixer.music.play()
    for i in range(3777):
        ps.write(b'\x01')
        time.sleep(0.06635)
