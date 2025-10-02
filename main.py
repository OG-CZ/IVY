import os
import eel
from features import *

eel.init('www')

host = 'localhost'
port = 8000 

# try:
if not os.system(f'start msedge.exe --app="http://{host}:{port}/index.html"'):
	play_assistant_sound()

	eel.start(
	'index.html',
	options={
		'mode': None,      
		'host': host,
		'port': port,
		'chromeFlags': []
	},
	block=True
)
# except Exception as e:
# 	print("ERROR!!!!")
# 	print(e)

