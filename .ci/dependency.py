import os
import requests
import sys
from pyunpack import Archive
from urllib.request import urlretrieve
from enum import Enum

class toolType(Enum):
    ARIA2 = 1
    ARIANGWKE = 2
    FOUND = 3


def findPackageR(id_repo, p_name, tag_name=False, all_=False):
    for rawData in requests.get(f"https://api.github.com/repos/{id_repo}/releases").json():
        if tag_name:
            if rawData['tag_name'] != tag_name:
                continue

        for f in rawData['assets']:
            if p_name == f['browser_download_url'][-len(p_name):]:
                rawData['assets'] = f
                return f['browser_download_url'] if not all_ else rawData
    raise Exception(
        "not found or maybe api changed!\n Try again with Change packages name")


def isNotAvaCheck() -> toolType:
    if not os.path.exists('aria2/aria2c.exe'):
        print("Aria2 not found")
        return toolType.ARIA2
    elif not os.path.exists('AriaNgWke/AriaNg.exe'):
        print("AriaNgWke not found")
        return toolType.ARIANGWKE
    else:
        print("Both are found")
        return toolType.FOUND


def downloadAria2(isx64=True):
    fileName = 'aria2.zip'
    pType = '64' if isx64 else '32'
    doc = findPackageR(
        'aria2/aria2', f'-win-{pType}bit-build1.zip', all_=True
        )['assets']
    pUrl = doc['browser_download_url']
    print(pUrl)
    print('aria2 Downloading...')
    urlretrieve(pUrl,  fileName)
    print('aria2 Downloaded')

    print('aria2 extracting...')
    Archive(fileName).extractall(".")
    print('aria2 extracted')

    os.rename(doc['name'][:-4], 'aria2')
    os.remove(fileName)


def downloadAriangwke(isx64=True):
    fileName = 'ariangwke.7z'
    pType = '64' if isx64 else '32'
    pUrl = findPackageR('delphilite/AriaNgWke', f'-Win{pType}.7z')
    print(pUrl)
    print('ariangwke Downloading...')
    urlretrieve(pUrl,  fileName)
    print('ariangwke Downloaded')

    print('ariangwke extracting...')
    Archive(fileName).extractall("AriaNgWke", auto_create_dir=True)
    print('ariangwke extracted...')

    os.remove(fileName)


if __name__ == '__main__':
    isx64 = bool(int(sys.argv[1]))

    if isNotAvaCheck() == toolType.ARIA2:
        downloadAria2(isx64)
    
    if isNotAvaCheck() == toolType.ARIANGWKE:
        downloadAriangwke(isx64)

    r = isNotAvaCheck()
    if r == toolType.FOUND:
        print("Download successful")
    else:
        print("Download Unsuccessful")
        raise Exception('Error while downloading '+ r.value)