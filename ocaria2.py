import multiprocessing
import signal
import subprocess
import os
from multiprocessing import Process
from urllib import request
from urllib import error


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
    os.system(cmdC)


def signal_handler(sig, frame):
    os.system("taskkill /F /IM AriaNg.exe")
    print("AriaNg stopped")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    ariangwkeP = Process(target=run_ariangwke)
    aria2cP = Process(target=run_aria2c)

    # starting process
    aria2cP.start()
    ariangwkeP.start()

    signal.signal(signal.SIGINT, signal_handler)

    # joining for end
    aria2cP.join()
    ariangwkeP.join()
