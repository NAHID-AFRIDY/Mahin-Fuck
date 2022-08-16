import os, platform
os.system('git pull')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import a
    menu()
elif bit == '32bit':
    import a
    menu()
