#!/usr/bin/python3



import jk_tokenizingparsing

import json






FILE_PATH = "tokenize_json.json"


textConverterMgr = jk_tokenizingparsing.TextConverterManager()
textConverterMgr.register(jk_tokenizingparsing.Convert4HexToUnicode())

with open(FILE_PATH, "r") as f:
	tokenizer = jk_tokenizingparsing.fromJSON(textConverterMgr, json.load(f))





for t in tokenizer.tokenize("{'a':123}"):
	print(t)




