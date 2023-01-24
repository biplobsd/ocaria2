# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ocaria2.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ocaria2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir='tools',
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

## move dependency
import shutil,os
toolsAria2='dist/tools/aria2'
if not os.path.exists(toolsAria2):
    shutil.copytree('aria2', toolsAria2)
toolsAriaNgWke='dist/tools/AriaNgWke'
if not os.path.exists(toolsAriaNgWke):
    shutil.copytree('AriaNgWke', toolsAriaNgWke)
