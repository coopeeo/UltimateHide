import json
import hashlib
import os
import sys
import zipfile
import urllib.request
import re
from pathlib import Path
import subprocess



archive = zipfile.ZipFile('coopeeo.hideplus.geode', 'r')
eee = archive.open('changelog.md')
eeee = []
for eeeee in eee:
	eeee.append(eeeee.decode('utf-8'))

eeeeee = ''.join(eeee)

one = ('# ' + eeeee.split('##')[1]).replace((eeeee.split('##')[1]).split('\r')[0], 'What\'s New This Update')
two = json.loads(archive.read('mod.json'))["version"]

if os.getenv('GITHUB_OUTPUT'):
	with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:
		file.write(f'cl={one}\n')
if os.getenv('GITHUB_OUTPUT'):
	with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:
		file.write(f'version={two}\n')