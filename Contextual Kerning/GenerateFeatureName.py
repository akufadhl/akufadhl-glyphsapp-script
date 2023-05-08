#MenuTitle: Generate Feature Name
__doc__="""
Change base64 names to regular names
"""
import base64
from pprint import pprint
import re
font = Glyphs.font

def decodeBase64(base64String):
	base64_bytes = base64String.encode('utf-8')
	name_bytes = base64.b64decode(base64_bytes)
	name = name_bytes.decode('utf-8')
	return name
	
def encodeBase64(name):
	name_bytes = name.encode('utf-8')
	base64_bytes = base64.b64encode(name_bytes)
	base64_name = base64_bytes.decode('utf-8')

	return base64_name

for a in font.numbers:
	oldName = a.name
	holder = decodeBase64(a.name)
	newName = re.sub(r"[_\-.\ ]",'',holder)
	a.name = newName


oldCode = font.features['kern'].code
regex = r"\${(.*?)}"
matches = re.findall(regex, oldCode)
newCode = ""
for match in matches:
	encoded = match
	decoded = decodeBase64(encoded)
	newName = re.sub(r"[_\-.\ ]","",decoded)
	print(newName)
	oldCode = oldCode.replace(encoded, newName)

if font.features['kern']:
	font.features['kern'].code = oldCode