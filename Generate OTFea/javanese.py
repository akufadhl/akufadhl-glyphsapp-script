#MenuTitle: Javanese
__doc__="""
Auto Generate Opentype feature for Javanese script
"""

import re
font = Glyphs.font

belowFormsGroup = ['a-java.below', 'ai-java.below', 'e-java.below', 'iKawi-java.below', 'i-java.below', 'ii-java.below', 'ka-java.below', 'ka-java.below.base', 'kaSasak-java.below', 'kaSasak-java.below.base', 'kaMurda-java.below', 'ga-java.below', 'gaMurda-java.below', 'nga-java.below', 'ca-java.below', 'ca-java.below.short', 'ca_pengkal-java.below', 'ca_suku-java.below', 'caMurda-java.below', 'ja-java.below', 'ja_suku-java.below', 'nyaMurda-java.below', 'tta-java.below', 'tta_pengkal-java.below', 'tta_suku-java.below', 'ttaMahaprana-java.below', 'ttaMahaprana_suku-java.below', 'dda-java.below', 'dda_suku-java.below', 'ddaMahaprana-java.below', 'naMurda-java.below', 'ta-java.below', 'taMurda-java.below', 'ta-java.below.base', 'da-java.below', 'daMahaprana-java.below', 'na-java.below', 'na_suku-java.below', 'ba-java.below', 'baMurda-java.below', 'ma-java.below', 'ma_suku-java.below', 'ya-java.below', 'ra-java.below', 'raAgung-java.below', 'la-java.below', 'la-java.below.base', 'wa-java.below', 'wa_suku-java.below', 'saMurda-java.below', 'ngaLelet-java.below', 'ngaLeletRaswadi-java.below', 'o-java.below', 'u-java.below', 'nyaMurda-java.below.alt', 'ba-java.below.alt', 'pengkal-java.below', 'la-java.below2', 'nya-java.below.alt', 'pa-java.below.alt', 'paMurda-java.below.alt', 'saMahaprana-java.below.alt', 'sa-java.below.alt', 'ha-java.below.alt', 'paCerek-java.below.alt', 'nyaMurda-java.below.alt', 'ba-java.below.alt']

def fea_blwf(font):
	pasGlyphs = ['ka-java.below', 'kaSasak-java.below', 'kaMurda-java.below', 'ga-java.below', 'gaMurda-java.below', 'nga-java.below', 'ca-java.below', 'caMurda-java.below', 'ja-java.below', 'nyaMurda-java.below', 'tta-java.below', 'ttaMahaprana-java.below', 'dda-java.below', 'ddaMahaprana-java.below', 'naMurda-java.below', 'ta-java.below', 'taMurda-java.below', 'da-java.below', 'daMahaprana-java.below', 'na-java.below', 'ba-java.below', 'baMurda-java.below', 'ma-java.below', 'ya-java.below', 'ra-java.below', 'raAgung-java.below', 'la-java.below', 'wa-java.below', 'saMurda-java.below', 'ngaLelet-java.below', 'ngaLeletRaswadi-java.below', 'a-java.below', 'iKawi-java.below', 'i-java.below', 'ii-java.below', 'u-java.below', 'e-java.below', 'ai-java.below', 'o-java.below']
	
	pangkon = "pangkon-java"
	
	lookup = "lookup pasanganForm {\n"
	
	for g in pasGlyphs:
		if (g and pangkon) in font.glyphs:
			baseGlyph = g.replace(".below","")
			if baseGlyph in font.glyphs:
				lookup += f"\tsub {pangkon} {baseGlyph} by {g};\n"

	lookup += "} pasanganForm;"

	return lookup

def below_shapes(font):
	belowGlyphs = ["cakra-java.below","cakra_suku-java.below","suku-java.below","sukuMendut-java.below","keret-java.below","wa-java.below2","la-java.below2","cakra-java.below.001","cakra-java.below.002","pengkal-java.below","pengkal_suku-java.below","pengkal_sukuMendut-java.below","pengkal_keret-java.below"]
	
	lookup = "lookup belowShapes {\n"
	for g in belowGlyphs:
		baseGlyph = re.sub(r"(\.below|\.below2)|(base)","", g )
		if (g and baseGlyph) in font.glyphs:
			lookup += f"\tsub @belowForms {baseGlyph}' by {g};\n"
	
	lookup += "} belowShapes;"

	print(lookup)
	return lookup

#BLWS FEATURE
def below_base(font):
	belowBase = ["ka-java.below.base","kaSasak-java.below.base","ta-java.below.base","la-java.below.base","ba-java.below.base","la-java.below2.base"]
	
	factor = ['suku-java.below', 'wa-java.below2', 'la-java.below2', 'cakra-java.below', 'cakra-java.below.001', 'cakra-java.below.002', 'keret-java.below', 'pengkal-java.below', 'pengkal-java.below.base']

	baseG = []
	for g in belowBase:
		baseGlyph = g.replace(".base","")
		if (g and baseGlyph) in font.glyphs:
			baseG.append(baseGlyph)
	
	lookup = "lookup belowBase {\n\tsub [" + ' '.join(baseG) + "]' [" + ' '.join(factor) + "] by [" + ' '.join(belowBase) + "];\n} belowBase;"
	
	print(lookup)
	return lookup

def below_pasLiga(font):
	ligaBelow = ['ca_suku-java.below', 'ca_sukuMendut-java.below', 'ca_keret-java.below', 'caMurda_suku-java.below', 'caMurda_sukuMendut-java.below', 'caMurda_keret-java.below', 'ja_suku-java.below', 'ja_sukuMendut-java.below', 'ja_keret-java.below', 'tta_suku-java.below', 'tta_sukuMendut-java.below', 'tta_keret-java.below', 'ttaMahaprana_suku-java.below', 'ttaMahaprana_sukuMendut-java.below', 'ttaMahaprana_keret-java.below', 'dda_suku-java.below', 'dda_sukuMendut-java.below', 'dda_keret-java.below', 'da_suku-java.below', 'da_sukuMendut-java.below', 'da_keret-java.below', 'na_suku-java.below', 'na_sukuMendut-java.below', 'na_keret-java.below', 'nyaMurda_suku-java.below', 'nyaMurda_sukuMendut-java.below', 'nyaMurda_keret-java.below', 'ma_suku-java.below', 'ma_sukuMendut-java.below', 'ma_keret-java.below', 'wa_suku-java.below', 'wa_sukuMendut-java.below', 'wa_keret-java.below', 'taMurda_suku-java.below', 'taMurda_sukuMendut-java.below', 'taMurda_keret-java.below']
	
	lookup = "lookup belowPasLiga {\n"
	for g in ligaBelow:
		baseGlyph = g.split("_")
		firstCombo = f"{baseGlyph[0]}-java.below"
		secondCombo = f"{baseGlyph[1]}"
		
		if (firstCombo and secondCombo) in font.glyphs:
			lookup += f"\tsub {firstCombo} {secondCombo} by {g};\n"
	
	lookup += "} belowPasLiga;"
	
	print(lookup)
	return lookup

def fea_pstf(font):
	postPas = ['jaMahaprana-java.post', 'nya-java.post', 'pa-java.post', 'paMurda-java.post', 'saMahaprana-java.post', 'sa-java.post', 'ha-java.post', 'paCerek-java.post']
	pangkon = "pangkon-java"
	
	lookup = "lookup postForms {\n"
	for g in postPas:
		baseGlyph = g.replace(".post","")
		if (g and pangkon) in font.glyphs:
			lookup += f"\tsub {pangkon} {baseGlyph} by {g};\n"
	
	lookup += "} postForms;"
	
	print(lookup)
	return lookup

def fea_pengkalLiga(font):
	postLiga = ["pengkal_suku-java","pengkal_sukuMendut-java","pengkal_keret-java","pengkal_suku-java.below","pengkal_sukuMendut-java.below","pengkal_keret-java.below"]
	
	lookup = "lookup postLiga02 {\n"
	for g in postLiga:
		splitList = g.split("_")
		newList = []
		for a in splitList:
			if "-java" not in a:
				a = f"{a}-java"
			newList.append(a)
		lookup += f"\tsub {' '.join(newList)} by {g};\n"
	
	lookup += "} postLiga02;"
	
	return lookup
	
def fea_postLigaBelow(font):
	postLiga = ["ca_pengkal-java.below","ca_pengkal_suku-java.below","ca_pengkal_sukuMendut-java.below","caMurda_pengkal-java.below","caMurda_pengkal_suku-java.below","caMurda_pengkal_sukuMendut-java.below","ja_pengkal-java.below","ja_pengkal_suku-java.below","ja_pengkal_sukuMendut-java.below","nyaMurda_pengkal-java.below","nyaMurda_pengkal_suku-java.below","nyaMurda_pengkal_sukuMendut-java.below","da_pengkal-java.below","da_pengkal_suku-java.below","da_pengkal_sukuMendut-java.below","na_pengkal-java.below","na_pengkal_suku-java.below","na_pengkal_sukuMendut-java.below","tta_pengkal-java.below","tta_pengkal_suku-java.below","tta_pengkal_sukuMendut-java.below","ttaMahaprana_pengkal-java.below","ttaMahaprana_pengkal_suku-java.below","ttaMahaprana_pengkal_sukuMendut-java.below","dda_pengkal-java.below","dda_pengkal_suku-java.below","dda_pengkal_sukuMendut-java.below","taMurda_pengkal-java.below","taMurda_pengkal_suku-java.below","taMurda_pengkal_sukuMendut-java.below","ma_pengkal-java.below","ma_pengkal_suku-java.below","ma_pengkal_sukuMendut-java.below","wa_pengkal-java.below","wa_pengkal_suku-java.below","wa_pengkal_sukuMendut-java.below"]
	
	lookup = "lookup postLiga01 {\n"
	for g in postLiga:
		splitList = g.split("_")
		newList = []
		for a in splitList:
			if '-java' not in a:
				a = f"{a}-java.below"
			newList.append(a)
		
		lookup += f"\tsub {' '.join(newList)} by {g};\n"
	
	lookup += "} postLiga01;"

	print(lookup)
	return lookup

def fea_topMarksLiga(font):
	topMarksLiga = ["cecakTelu_panyangga-java","cecakTelu_cecak-java","cecakTelu_wulu-java","cecakTelu_wuluMelik-java","cecakTelu_pepet-java","cecakTelu_layar-java","cecakTelu_wulu_panyangga-java","cecakTelu_wulu_layar-java","cecakTelu_wuluMelik_panyangga-java","cecakTelu_wuluMelik_layar-java","cecakTelu_pepet_panyangga-java","cecakTelu_pepet_layar-java","cecakTelu_wulu_cecak-java","cecakTelu_wuluMelik_cecak-java","cecakTelu_pepet_cecak-java","wulu_cecak-java","wulu_panyangga-java","wulu_layar-java","wuluMelik_cecak-java","wuluMelik_panyangga-java","wuluMelik_layar-java","pepet_cecak-java","pepet_panyangga-java","pepet_layar-java","layar_cecak-java","layar_cecakTelu-java","layar_panyangga-java"]
	
	lookup = "lookup topMarksLiga {\n"
	for g in topMarksLiga:
		splitList = g.split("_")
		newList = []
		for a in splitList:
			if "-java" not in a:
				a = f"{a}-java"
			newList.append(a)
		lookup += f"\tsub {' '.join(newList)} by {g};\n"
		
	lookup += "} topMarksLiga;"
	
	return lookup
	
#FEATURE GENERATION
def gen_blws(font):
	belowShapes = below_shapes(font)
	belowBase = below_base(font)
	belowPasLiga = below_pasLiga(font)
	
	feature = GSFeature('blws', "")
	feature.code += belowShapes + "\n"
	feature.code += belowBase + "\n"
	feature.code += belowPasLiga
	
	return feature
	
def gen_blwf(font):
	blwfLookup = fea_blwf(font)
	feature = GSFeature('blwf', blwfLookup)
	
	print(feature)
	return feature

def gen_pstf(font):
	pstfLookup = fea_pstf(font)
	ligaPstfLookup = fea_postLiga(font)
	
	feature = GSFeature('pstf', "")
	feature.code += pstfLookup + "\n"
	
	return feature

def gen_psts(font):
	ligaPstfLookup = fea_postLigaBelow(font)
	pengkalLiga = fea_pengkalLiga(font)
	
	feature = GSFeature('psts', "")
	feature.code += ligaPstfLookup + "\n"
	feature.code += pengkalLiga
	
	return(feature)
def gen_abvs(font):
	topMarksLiga = fea_topMarksLiga(font)
	
	feature = GSFeature('abvs', "")
	feature.code += topMarksLiga + "\n"
	
	return feature
	
def gen_features(font):
	
	if not font.classes['belowForms']:
		font.classes.append(GSClass('belowForms', ' '.join(belowFormsGroup)))
		
	features = [gen_abvs(font), gen_blwf(font), gen_blws(font), gen_pstf(font), gen_psts(font)]
	
	for feature in features:
		print(feature.name)
		if not font.features[feature.name]:
			font.features.append(feature)
		
		if font.features[feature.name]:
			font.features[feature.name].code = feature.code

gen_features(font)