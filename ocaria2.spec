# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ocaria2.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('aria2-1.36.0-win-64bit-build1', 'aria2-1.36.0-win-64bit-build1'),
         ('AriaNgWke-Win64', 'AriaNgWke-Win64')
    ],
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
    [],
    exclude_binaries=True,
    name='ocaria2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ocaria2',
)
