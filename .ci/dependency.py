import os
import requests
import sys
from pyunpack import Archive
from urllib.request import urlretrieve
from enum import Enum

class NamePathTool:
    def __init__(self, name:str, path:str) -> None:
        self.name = name
        self.path = path

class toolTypeUI(Enum):
    NOTFOUND = NamePathTool('Not', '.')
    ARIANGWKE = NamePathTool('AriaNgWKE', 'tools/AriaNgWke/AriaNg.exe')
    ARIANNATIVE = NamePathTool('AriaNg Native', 'tools/AriaNgNative/AriaNg Native.exe')
    ARIANG = NamePathTool('Ariang', 'tools/AriaNg/index.html')

class toolType(Enum):
    ARIA2 = 1
    ARIANGWKE = 2
    FOUND = 3
    ARIANGNATIVE = 4
    ARIANG = 5


def findPackageR(id_repo, p_name, tag_name=False, all_=False):
    for _ in range(2):
        getData = requests.get(f"https://api.github.com/repos/{id_repo}/releases")
        if getData.ok:
            try:
                for rawData in getData.json():
                    if tag_name:
                        if rawData['tag_name'] != tag_name:
                            continue

                    for f in rawData['assets']:
                        if p_name == f['browser_download_url'][-len(p_name):]:
                            rawData['assets'] = f
                            return f['browser_download_url'] if not all_ else rawData
            except:
                continue
            raise Exception(
                f"{id_repo}/{p_name} Not found or maybe api changed!\n Try again with Change packages name")


def isNotAvaCheck():
    if not os.path.exists('tools/aria2/aria2c.exe'):
        print("Aria2 not found")
        return toolType.ARIA2
    elif not os.path.exists(toolTypeUI.ARIANGWKE.value.path):
        print("AriaNgWke not found")
        return toolType.ARIANGWKE
    elif not os.path.exists(toolTypeUI.ARIANNATIVE.value.path):
        print("ARIAN NATIVE not found")
        return toolType.ARIANGNATIVE
    elif not os.path.exists(toolTypeUI.ARIANG.value.path):
        print("ARIANG not found")
        return toolType.ARIANG
    else:
        print("All found")
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
    Archive(fileName).extractall("tools/")
    print('aria2 extracted')

    os.rename('tools/'+doc['name'][:-4], 'tools/aria2')

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
    Archive(fileName).extractall("tools/AriaNgWke", auto_create_dir=True)
    print('ariangwke extracted...')

    os.remove(fileName)

def downloadAriangNative(isx64=True):
    fileName = 'ariangnative.7z'
    pType = '64' if isx64 else '86'
    pUrl = findPackageR('mayswind/AriaNg-Native', f'-Windows-x{pType}.7z')
    print(pUrl)
    print('ariang native Downloading...')
    urlretrieve(pUrl,  fileName)
    print('ariang native Downloaded')

    print('ariang native extracting...')
    Archive(fileName).extractall("tools/AriaNgNative", auto_create_dir=True)
    print('ariang native extracted...')

    os.remove(fileName)

def downloadAriang():
    fileName = 'ariang.zip'
    pUrl = findPackageR('mayswind/AriaNg', '-AllInOne.zip')
    print(pUrl)
    print('ariang Downloading...')
    urlretrieve(pUrl,  fileName)
    print('ariang Downloaded')

    print('ariang extracting...')
    Archive(fileName).extractall("tools/AriaNg", auto_create_dir=True)
    print('ariang extracted...')

    os.remove(fileName)


if __name__ == '__main__':
    isx64 = bool(int(sys.argv[1]))
    uiClient = 0
    try:
        uiClient = int(sys.argv[2])
    except:
        pass
    os.makedirs('tools', exist_ok=True)
    if isNotAvaCheck() == toolType.ARIA2:
        downloadAria2(isx64)
    
    if uiClient == 0:
        downloadAriangwke(isx64)
    elif uiClient == 1:
        downloadAriangNative(isx64)
    elif uiClient == 2:
        downloadAriang()