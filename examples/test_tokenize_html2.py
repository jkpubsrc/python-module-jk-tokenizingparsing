#!/usr/bin/python3



import os
import sys

import jk_tokenizingparsing

import json






FILE_PATH = "tokenize_html.json"

p = input("Enter file or directory path containing many HTML files: ")

textConverterMgr = jk_tokenizingparsing.TextConverterManager()
textConverterMgr.register(jk_tokenizingparsing.Convert4HexToUnicode())

with open(FILE_PATH, "r") as f:
	tokenizer = jk_tokenizingparsing.fromJSON(textConverterMgr, json.load(f))



def processFile(filePath:str, tokenizer):
	entryName = os.path.basename(filePath)

	with open(filePath, "r") as f:
		fileContent = f.read()

	bSuccess = False
	try:
		for t in tokenizer.tokenize(fileContent, sourceID=entryName):
			pass
		bSuccess = True
	except:
		pass

	if bSuccess:
		print("SUCCESS: " + entryName)
	else:
		print("ERROR encountered tokenizing file: " + entryName)
		print()
		try:
			for t in tokenizer.tokenize(fileContent, sourceID=entryName):
				print(t)
		except jk_tokenizingparsing.ParserErrorException as ee:
			print()
			ee.print()
			print()
#




if os.path.isdir(p):
	for entryName in os.listdir(p):
		filePath = os.path.join(p, entryName)
		if os.path.isfile(filePath):
			processFile(filePath, tokenizer)

elif os.path.isfile(p):
	processFile(p, tokenizer)

else:
	print("ERROR: No such file or directory: " + p)








