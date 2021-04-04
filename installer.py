import PyInstaller.__main__

PyInstaller.__main__.run([
    'GUI.py',
    '--onefile',
    '--windowed',
    '--icon=ico.ico'
])
