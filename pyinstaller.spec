# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['NexusShare.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('uploads', 'uploads'),
        ('nexus_config.json', '.'),
        ('NexusShare.jpg', '.')
    ],
    hiddenimports=['customtkinter', 'PIL', 'qrcode'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='NexusShare',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # تغيير إلى True إذا أردت نافذة Console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='NexusShare.jpg'
)
