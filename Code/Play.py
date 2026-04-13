import serial
import subprocess
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

video_path = "/home/justbuild/Downloads/video.mp4"

player = None
playing = False
start_time = None

while True:
    data = ser.readline().decode().strip()
    print(data)

    if data == "BOTH":
        if start_time is None:
            start_time = time.time()

        elif time.time() - start_time >= 5:
            # 5 seconds condition met

            if not playing:
                print("Playing Video")
                player = subprocess.Popen([
                    "cvlc", "--fullscreen", video_path
                ])
                playing = True

            else:
                print("Stopping Video")
                if player:
                    player.terminate()
                playing = False

            start_time = None  # reset after action

    else:
        start_time = None  # reset if condition breaks
