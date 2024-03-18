# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['G:/PycharmProjects/mp4-to-gif/main.py'],
    pathex=[],
    binaries=[],
    datas=[('G:/PycharmProjects/mp4-to-gif/Style.kv', '.'), ('G:/PycharmProjects/mp4-to-gif/Yooopy.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Video to Gif',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['G:\\PycharmProjects\\mp4-to-gif\\Yooopy.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Video to Gif',
)
