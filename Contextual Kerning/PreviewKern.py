#MenuTitle: Preview Kerning List
__doc__="""
Preview Kerning List
"""

import vanilla
import base64
import traceback
import re

font = Glyphs.font

class kernList:
	def __init__(self):
		self.w = vanilla.Window((400,100), "Kerning List", minSize=(400,100))
		self.masterIndex = 0
		columnDescriptions = [
			dict(
                identifier="id",
                title="id",
                sortable=True
            ),
            dict(
                identifier="affected",
                title="affected",
                sortable=True
            ),
            dict(
                identifier="affecting",
                title="affecting",
                sortable=True
            ),
            dict(
                identifier="value",
                title="value",
                sortable=True,
                editable=True
            )
            ]
		self.w.kernList = vanilla.List(
			"auto",
			items = self.kerningList(self.masterIndex),
			columnDescriptions = columnDescriptions,
			selectionCallback = self.clickCallback,
			editCallback = self.editKernValue
		)
		self.w.language = vanilla.PopUpButton('auto', ['javanese', 'kawi'])
		self.w.masterSelect = vanilla.PopUpButton("auto", self.getMaster(), callback=self.getMasterId)
		
		rules = [
		    # Vertical
		    "H:|-[kernList(>=550)]-|",
		    "H:|-[language]-|",
		    "H:|-[masterSelect]-|",
		    "V:|-[kernList(>=150)]-[language]-[masterSelect]-|"
		]
		self.w.addAutoPosSizeRules(rules)
		self.w.open()
	
	def getMaster(self):
		masters = []
		for master in font.masters:
			masters.append(master.name)
		return masters
	
	def clickCallback(self, sender):
		listId = sender.getSelection()
		kernList = sender.get()
		kernDict = kernList[listId[0]]
		affected = [x for x in kernDict['affected'].split(" ")]
		affecting = [x for x in kernDict['affecting'].split(" ")]
		value = kernDict['value']
		
		text = ""
		for x in affected:
			for y in affecting:
				if self.w.language.getItem() == 'javanese':
					print(f"/ka-java/suku-java/{x}{self.belowSplitter(y,'javanese')}/ka-java/la-java")
					text += f"/ka-java/suku-java/{x}{self.belowSplitter(y,'javanese')}/ka-java/la-java"
				elif self.w.language.getItem() == 'kawi':
					print(f"/ka-kawi/vowelU-kawi/{x}{self.belowSplitter(y,'kawi')}/la-kawi/ka-kawi")
					text += f"/ka-kawi/vowelU-kawi/{x}{self.belowSplitter(y,'kawi')}/la-kawi/ka-kawi"

		font = Glyphs.font
		if font.currentTab:
			font.currentTab.text = text
			PreviewTextWindow.open()
			PreviewTextWindow.text = font.currentTab.text
			PreviewTextWindow.fontSize = 150
			self.w.makeKey()
		else:
			font.newTab(text)
			PreviewTextWindow.open()
			font = PreviewTextWindow.font
			print(self.w.masterSelect.get())
			PreviewTextWindow.text = font.currentTab.text
			PreviewTextWindow.fontSize = 150
			self.w.makeKey()
			
	def belowSplitter(self, glyphname, lang):
		text = ""
		if lang == 'kawi':
			glyph = f"/{glyphname}"
			listHold = glyph.split('.')
			print(listHold)
			listHold.pop()
			print(listHold)
			listHold.insert(0, '/virama-kawi')
			print(listHold)
			text = "".join(listHold)
			
		if lang == 'javanese':
			listHold = glyphname.split('_')
			print(listHold)
			newList = []
			for x in listHold:
				replaced = x.replace('Pas', '-java')
				newString = re.sub(r"|\.alt|\.below2|.base|.below|.001|.002?", "", replaced)
				newList.append("/" + newString)
			newList.insert(0, '/pangkon-java')
			text = "".join(newList)
		return text
	
	def editKernValue(self, sender):
		try:
			listId = sender.getSelection()[0]
			kernList = sender.get()
			masterIndex = self.w.masterSelect.get()
			value = int(kernList[listId]['value'])
			kernId = kernList[listId]['id']
			font.masters[masterIndex].setNumberValueValue_forName_(value, kernId)
			font.features.update()
		except:
			print(traceback.format_exc())

	def getMasterId(self, sender):
		try:
			self.masterIndex = sender.get()
			items = self.kerningList(self.masterIndex)
			self.w.kernList.set(items)
			font = PreviewTextWindow.font
			instanceNames = [instance.name for instance in font.instances]
			regularIndex = instanceNames.index(sender.getItem())
			PreviewTextWindow.instanceIndex = regularIndex
		except:
			print(traceback.format_exc())
			
	def decodeBase64(self, base64String):
		base64_bytes = base64String.encode('utf-8')
		name_bytes = base64.b64decode(base64_bytes)
		name = name_bytes.decode('utf-8')
	
		return name
		
	def kerningList(self, masterIndex):
		items = []
		for i, a in enumerate(font.numbers):
			if a:
				name_decoded = self.decodeBase64(a.name)
				print(name_decoded)
				names = name_decoded.split("_")
				affected = names[0]
				print(names)
				affecting = names[1]
				newDict = dict(
					id = a.name,
					affected = affected,
					affecting = affecting,
					value = font.masters[self.masterIndex].numberValueValueForName_(a.name)
				)
				items.append(newDict)
		return items

if font:
	kernList()
else:
	print('Open Font')