from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['entalpia.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['sqlite3'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
a.datas += [('Code\entalpia.kv','E:\\Works\\tesis\\termo\\app\\entalpia\entalpia.kv','DATA')]
a.datas += [('database\database.sqlite3', 'E:\\Works\\tesis\\termo\\app\\entalpia\\database', 'DATA')]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Nox_LVTE',
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
    icon=['img\\utelvte.png'],
)

coll = COLLECT(
    exe,
    Tree('E:\\Works\\tesis\\termo\\app\\entalpia\\'),
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Nox_LVTE',
)
