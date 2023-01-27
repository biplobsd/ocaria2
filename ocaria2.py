import multiprocessing
import signal
import subprocess
import os
import functools
from enum import Enum
from multiprocessing import Process
from urllib import request
from urllib import error


class toolTypeUI(Enum):
    NOTFOUND = '-1'
    ARIANGWKE = 'AriaNg'
    ARIANNATIVE = 'AriaNg Native'


def checkFontend():
    if os.path.exists('tools/AriaNgWke/AriaNg.exe'):
        print("AriaNgWke not found")
        return toolTypeUI.ARIANGWKE
    elif os.path.exists('tools/AriaNgNative/AriaNg Native.exe'):
        print("AriaNgNative not found")
        return toolTypeUI.ARIANNATIVE
    else:
        return toolTypeUI.NOTFOUND


def run_arianative():
    print("ariangnative")
    cwd = os.path.join('tools', 'AriaNgNative')
    subprocess.Popen(["AriaNg Native"], cwd=cwd, shell=True)


def run_ariangwke():
    cwd = os.path.join('tools', 'AriaNgWke')
    subprocess.Popen(["AriaNg"], cwd=cwd, shell=True)


def run_aria2c():
    OUTPUT_DIR = os.path.join(os.getcwd(), 'downloads')
    cwd = os.path.join('tools', 'aria2')
    try:
        with request.urlopen("https://trackerslist.com/best_aria2.txt") as url:
            trackers = url.read().decode()
    except error.URLError:
        print("Unable to set torrent trackerslist")
        trackers = ''

    cmdC = fr'cd {cwd} &&' \
        r"aria2c --enable-rpc --rpc-listen-port=6800 -D " \
        fr"-d {OUTPUT_DIR} " \
        r"-j 20 " \
        r"-c " \
        fr"--bt-tracker={trackers} " \
        r"--bt-request-peer-speed-limit=0 " \
        r"--bt-max-peers=0 " \
        r"--seed-ratio=0.0 " \
        r"--max-connection-per-server=10 " \
        r"--min-split-size=10M " \
        r"--follow-torrent=mem " \
        r"--disable-ipv6=true " \
        r"--user-agent=Transmission/2.77 --peer-agent=Transmission/2.77 " \
        r"--peer-id-prefix=-TR2770- " \
        r"--split=20 "
    try:
        os.system(cmdC)
    except KeyboardInterrupt:
        print("Kill by user")


def signal_handler(r, signum, frame):
    if r == toolTypeUI.ARIANNATIVE:
        print('No need to force kill '+r.value)
        return
    os.system(fr"taskkill /F /IM AriaNg Native.exe")
    print(f"{r.value} stopped")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    aria2cP = Process(target=run_aria2c)
    aria2cP.start()

    r = checkFontend()
    signal.signal(signal.SIGINT, functools.partial(signal_handler, r))

    if r == toolTypeUI.ARIANGWKE:
        ariangwkeP = Process(target=run_ariangwke)
        ariangwkeP.start()
        ariangwkeP.join()
    elif r == toolTypeUI.ARIANNATIVE:
        ariangnativeP = Process(target=run_arianative)
        ariangnativeP.start()
        ariangnativeP.join()
    else:
        raise Exception("No fontend ui found")

    aria2cP.join()
