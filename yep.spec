# -*- mode: python -*-

block_cipher = None

added_files = [
            ('beats', 'beats'),
            ('imgs', 'imgs')
]


a = Analysis(['yep.py'],
             pathex=['/Users/mitchellbarton/workspace/freestylez'],
             binaries=None,
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='F R E E S T Y L E Z ( B A T T L E )',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='yep')
