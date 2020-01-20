#!/usr/bin/python3



import jk_tokenizingparsing

import json






FILE_PATH = "tokenize_html.json"


textConverterMgr = jk_tokenizingparsing.TextConverterManager()
textConverterMgr.register(jk_tokenizingparsing.Convert4HexToUnicode())

with open(FILE_PATH, "r") as f:
	tokenizer = jk_tokenizingparsing.fromJSON(textConverterMgr, json.load(f))





for t in tokenizer.tokenize("""
<!doctype html>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<!-- This is a comment -->
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="css/styles.css?v=1.0">
  	</head>
	<body>
		<hr/>
		<script src="js/scripts.js"></script>
		<h1>Heading 1</h1>
		<p>
			Test
			< img src = "bla" width = "abc" height = 123 important />
		</p>
	</body>
</html>
"""):
	print(t)




