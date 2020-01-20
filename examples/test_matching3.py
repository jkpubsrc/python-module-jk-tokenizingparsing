#!/usr/bin/python3



import jk_json
import jk_tokenizingparsing
from jk_tokenizingparsing.tokenmatching import *




TEXT = """CREATE TABLE archive (
	ar_id INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
	ar_namespace INTEGER NOT NULL default 0,
	ar_title TEXT  NOT NULL default '',
	ar_comment BLOB NOT NULL default '', -- Deprecated in favor of ar_comment_id
	ar_comment_id INTEGER  NOT NULL DEFAULT 0, -- ("DEFAULT 0" is temporary, signaling that ar_comment should be used)
	ar_user INTEGER  NOT NULL default 0, -- Deprecated in favor of ar_actor
	ar_user_text TEXT  NOT NULL DEFAULT '', -- Deprecated in favor of ar_actor
	ar_actor INTEGER  NOT NULL DEFAULT 0, -- ("DEFAULT 0" is temporary, signaling that ar_user/ar_user_text should be used)
	ar_timestamp BLOB NOT NULL default '',
	ar_minor_edit INTEGER NOT NULL default 0,
	ar_rev_id INTEGER  NOT NULL,
	ar_text_id INTEGER  NOT NULL DEFAULT 0,
	ar_deleted INTEGER  NOT NULL default 0,
	ar_len INTEGER ,
	ar_page_id INTEGER ,
	ar_parent_id INTEGER  default NULL,
	ar_sha1 BLOB NOT NULL default '',
	ar_content_model BLOB DEFAULT NULL,
	ar_content_format BLOB DEFAULT NULL
	)"""

TOKENS = jk_tokenizingparsing.Serializer.deserializeTokens([
	{"type":"w","text":"CREATE","lineNo":0,"charPos":0,"endLineNo":0,"endCharPos":6},
	{"type":"w","text":"TABLE","lineNo":0,"charPos":7,"endLineNo":0,"endCharPos":12},
	{"type":"w","text":"archive","lineNo":0,"charPos":13,"endLineNo":0,"endCharPos":20},
	{"type":"dbo","text":"(","lineNo":0,"charPos":21,"endLineNo":0,"endCharPos":22},
	{"type":"w","text":"ar_id","lineNo":1,"charPos":1,"endLineNo":1,"endCharPos":6},
	{"type":"w","text":"INTEGER","lineNo":1,"charPos":7,"endLineNo":1,"endCharPos":14},
	{"type":"w","text":"NOT","lineNo":1,"charPos":16,"endLineNo":1,"endCharPos":19},
	{"type":"w","text":"NULL","lineNo":1,"charPos":20,"endLineNo":1,"endCharPos":24},
	{"type":"w","text":"PRIMARY","lineNo":1,"charPos":25,"endLineNo":1,"endCharPos":32},
	{"type":"w","text":"KEY","lineNo":1,"charPos":33,"endLineNo":1,"endCharPos":36},
	{"type":"w","text":"AUTOINCREMENT","lineNo":1,"charPos":37,"endLineNo":1,"endCharPos":50},
	{"type":"dc","text":",","lineNo":1,"charPos":50,"endLineNo":1,"endCharPos":51},
	{"type":"w","text":"ar_namespace","lineNo":2,"charPos":1,"endLineNo":2,"endCharPos":13},
	{"type":"w","text":"INTEGER","lineNo":2,"charPos":14,"endLineNo":2,"endCharPos":21},
	{"type":"w","text":"NOT","lineNo":2,"charPos":22,"endLineNo":2,"endCharPos":25},
	{"type":"w","text":"NULL","lineNo":2,"charPos":26,"endLineNo":2,"endCharPos":30},
	{"type":"w","text":"default","lineNo":2,"charPos":31,"endLineNo":2,"endCharPos":38},
	{"type":"i","text":"0","lineNo":2,"charPos":39,"endLineNo":2,"endCharPos":40},
	{"type":"dc","text":",","lineNo":2,"charPos":40,"endLineNo":2,"endCharPos":41},
	{"type":"w","text":"ar_title","lineNo":3,"charPos":1,"endLineNo":3,"endCharPos":9},
	{"type":"w","text":"TEXT","lineNo":3,"charPos":10,"endLineNo":3,"endCharPos":14},
	{"type":"w","text":"NOT","lineNo":3,"charPos":16,"endLineNo":3,"endCharPos":19},
	{"type":"w","text":"NULL","lineNo":3,"charPos":20,"endLineNo":3,"endCharPos":24},
	{"type":"w","text":"default","lineNo":3,"charPos":25,"endLineNo":3,"endCharPos":32},
	{"type":"s","text":"","lineNo":3,"charPos":34,"endLineNo":3,"endCharPos":35},
	{"type":"dc","text":",","lineNo":3,"charPos":35,"endLineNo":3,"endCharPos":36},
	{"type":"w","text":"ar_comment","lineNo":4,"charPos":1,"endLineNo":4,"endCharPos":11},
	{"type":"w","text":"BLOB","lineNo":4,"charPos":12,"endLineNo":4,"endCharPos":16},
	{"type":"w","text":"NOT","lineNo":4,"charPos":17,"endLineNo":4,"endCharPos":20},
	{"type":"w","text":"NULL","lineNo":4,"charPos":21,"endLineNo":4,"endCharPos":25},
	{"type":"w","text":"default","lineNo":4,"charPos":26,"endLineNo":4,"endCharPos":33},
	{"type":"s","text":"","lineNo":4,"charPos":35,"endLineNo":4,"endCharPos":36},
	{"type":"dc","text":",","lineNo":4,"charPos":36,"endLineNo":4,"endCharPos":37},
	{"type":"w","text":"ar_comment_id","lineNo":5,"charPos":1,"endLineNo":5,"endCharPos":14},
	{"type":"w","text":"INTEGER","lineNo":5,"charPos":15,"endLineNo":5,"endCharPos":22},
	{"type":"w","text":"NOT","lineNo":5,"charPos":24,"endLineNo":5,"endCharPos":27},
	{"type":"w","text":"NULL","lineNo":5,"charPos":28,"endLineNo":5,"endCharPos":32},
	{"type":"w","text":"DEFAULT","lineNo":5,"charPos":33,"endLineNo":5,"endCharPos":40},
	{"type":"i","text":"0","lineNo":5,"charPos":41,"endLineNo":5,"endCharPos":42},
	{"type":"dc","text":",","lineNo":5,"charPos":42,"endLineNo":5,"endCharPos":43},
	{"type":"w","text":"ar_user","lineNo":6,"charPos":1,"endLineNo":6,"endCharPos":8},
	{"type":"w","text":"INTEGER","lineNo":6,"charPos":9,"endLineNo":6,"endCharPos":16},
	{"type":"w","text":"NOT","lineNo":6,"charPos":18,"endLineNo":6,"endCharPos":21},
	{"type":"w","text":"NULL","lineNo":6,"charPos":22,"endLineNo":6,"endCharPos":26},
	{"type":"w","text":"default","lineNo":6,"charPos":27,"endLineNo":6,"endCharPos":34},
	{"type":"i","text":"0","lineNo":6,"charPos":35,"endLineNo":6,"endCharPos":36},
	{"type":"dc","text":",","lineNo":6,"charPos":36,"endLineNo":6,"endCharPos":37},
	{"type":"w","text":"ar_user_text","lineNo":7,"charPos":1,"endLineNo":7,"endCharPos":13},
	{"type":"w","text":"TEXT","lineNo":7,"charPos":14,"endLineNo":7,"endCharPos":18},
	{"type":"w","text":"NOT","lineNo":7,"charPos":20,"endLineNo":7,"endCharPos":23},
	{"type":"w","text":"NULL","lineNo":7,"charPos":24,"endLineNo":7,"endCharPos":28},
	{"type":"w","text":"DEFAULT","lineNo":7,"charPos":29,"endLineNo":7,"endCharPos":36},
	{"type":"s","text":"","lineNo":7,"charPos":38,"endLineNo":7,"endCharPos":39},
	{"type":"dc","text":",","lineNo":7,"charPos":39,"endLineNo":7,"endCharPos":40},
	{"type":"w","text":"ar_actor","lineNo":8,"charPos":1,"endLineNo":8,"endCharPos":9},
	{"type":"w","text":"INTEGER","lineNo":8,"charPos":10,"endLineNo":8,"endCharPos":17},
	{"type":"w","text":"NOT","lineNo":8,"charPos":19,"endLineNo":8,"endCharPos":22},
	{"type":"w","text":"NULL","lineNo":8,"charPos":23,"endLineNo":8,"endCharPos":27},
	{"type":"w","text":"DEFAULT","lineNo":8,"charPos":28,"endLineNo":8,"endCharPos":35},
	{"type":"i","text":"0","lineNo":8,"charPos":36,"endLineNo":8,"endCharPos":37},
	{"type":"dc","text":",","lineNo":8,"charPos":37,"endLineNo":8,"endCharPos":38},
	{"type":"w","text":"ar_timestamp","lineNo":9,"charPos":1,"endLineNo":9,"endCharPos":13},
	{"type":"w","text":"BLOB","lineNo":9,"charPos":14,"endLineNo":9,"endCharPos":18},
	{"type":"w","text":"NOT","lineNo":9,"charPos":19,"endLineNo":9,"endCharPos":22},
	{"type":"w","text":"NULL","lineNo":9,"charPos":23,"endLineNo":9,"endCharPos":27},
	{"type":"w","text":"default","lineNo":9,"charPos":28,"endLineNo":9,"endCharPos":35},
	{"type":"s","text":"","lineNo":9,"charPos":37,"endLineNo":9,"endCharPos":38},
	{"type":"dc","text":",","lineNo":9,"charPos":38,"endLineNo":9,"endCharPos":39},
	{"type":"w","text":"ar_minor_edit","lineNo":10,"charPos":1,"endLineNo":10,"endCharPos":14},
	{"type":"w","text":"INTEGER","lineNo":10,"charPos":15,"endLineNo":10,"endCharPos":22},
	{"type":"w","text":"NOT","lineNo":10,"charPos":23,"endLineNo":10,"endCharPos":26},
	{"type":"w","text":"NULL","lineNo":10,"charPos":27,"endLineNo":10,"endCharPos":31},
	{"type":"w","text":"default","lineNo":10,"charPos":32,"endLineNo":10,"endCharPos":39},
	{"type":"i","text":"0","lineNo":10,"charPos":40,"endLineNo":10,"endCharPos":41},
	{"type":"dc","text":",","lineNo":10,"charPos":41,"endLineNo":10,"endCharPos":42},
	{"type":"w","text":"ar_rev_id","lineNo":11,"charPos":1,"endLineNo":11,"endCharPos":10},
	{"type":"w","text":"INTEGER","lineNo":11,"charPos":11,"endLineNo":11,"endCharPos":18},
	{"type":"w","text":"NOT","lineNo":11,"charPos":20,"endLineNo":11,"endCharPos":23},
	{"type":"w","text":"NULL","lineNo":11,"charPos":24,"endLineNo":11,"endCharPos":28},
	{"type":"dc","text":",","lineNo":11,"charPos":28,"endLineNo":11,"endCharPos":29},
	{"type":"w","text":"ar_text_id","lineNo":12,"charPos":1,"endLineNo":12,"endCharPos":11},
	{"type":"w","text":"INTEGER","lineNo":12,"charPos":12,"endLineNo":12,"endCharPos":19},
	{"type":"w","text":"NOT","lineNo":12,"charPos":21,"endLineNo":12,"endCharPos":24},
	{"type":"w","text":"NULL","lineNo":12,"charPos":25,"endLineNo":12,"endCharPos":29},
	{"type":"w","text":"DEFAULT","lineNo":12,"charPos":30,"endLineNo":12,"endCharPos":37},
	{"type":"i","text":"0","lineNo":12,"charPos":38,"endLineNo":12,"endCharPos":39},
	{"type":"dc","text":",","lineNo":12,"charPos":39,"endLineNo":12,"endCharPos":40},
	{"type":"w","text":"ar_deleted","lineNo":13,"charPos":1,"endLineNo":13,"endCharPos":11},
	{"type":"w","text":"INTEGER","lineNo":13,"charPos":12,"endLineNo":13,"endCharPos":19},
	{"type":"w","text":"NOT","lineNo":13,"charPos":21,"endLineNo":13,"endCharPos":24},
	{"type":"w","text":"NULL","lineNo":13,"charPos":25,"endLineNo":13,"endCharPos":29},
	{"type":"w","text":"default","lineNo":13,"charPos":30,"endLineNo":13,"endCharPos":37},
	{"type":"i","text":"0","lineNo":13,"charPos":38,"endLineNo":13,"endCharPos":39},
	{"type":"dc","text":",","lineNo":13,"charPos":39,"endLineNo":13,"endCharPos":40},
	{"type":"w","text":"ar_len","lineNo":14,"charPos":1,"endLineNo":14,"endCharPos":7},
	{"type":"w","text":"INTEGER","lineNo":14,"charPos":8,"endLineNo":14,"endCharPos":15},
	{"type":"dc","text":",","lineNo":14,"charPos":16,"endLineNo":14,"endCharPos":17},
	{"type":"w","text":"ar_page_id","lineNo":15,"charPos":1,"endLineNo":15,"endCharPos":11},
	{"type":"w","text":"INTEGER","lineNo":15,"charPos":12,"endLineNo":15,"endCharPos":19},
	{"type":"dc","text":",","lineNo":15,"charPos":20,"endLineNo":15,"endCharPos":21},
	{"type":"w","text":"ar_parent_id","lineNo":16,"charPos":1,"endLineNo":16,"endCharPos":13},
	{"type":"w","text":"INTEGER","lineNo":16,"charPos":14,"endLineNo":16,"endCharPos":21},
	{"type":"w","text":"default","lineNo":16,"charPos":23,"endLineNo":16,"endCharPos":30},
	{"type":"w","text":"NULL","lineNo":16,"charPos":31,"endLineNo":16,"endCharPos":35},
	{"type":"dc","text":",","lineNo":16,"charPos":35,"endLineNo":16,"endCharPos":36},
	{"type":"w","text":"ar_sha1","lineNo":17,"charPos":1,"endLineNo":17,"endCharPos":8},
	{"type":"w","text":"BLOB","lineNo":17,"charPos":9,"endLineNo":17,"endCharPos":13},
	{"type":"w","text":"NOT","lineNo":17,"charPos":14,"endLineNo":17,"endCharPos":17},
	{"type":"w","text":"NULL","lineNo":17,"charPos":18,"endLineNo":17,"endCharPos":22},
	{"type":"w","text":"default","lineNo":17,"charPos":23,"endLineNo":17,"endCharPos":30},
	{"type":"s","text":"","lineNo":17,"charPos":32,"endLineNo":17,"endCharPos":33},
	{"type":"dc","text":",","lineNo":17,"charPos":33,"endLineNo":17,"endCharPos":34},
	{"type":"w","text":"ar_content_model","lineNo":18,"charPos":1,"endLineNo":18,"endCharPos":17},
	{"type":"w","text":"BLOB","lineNo":18,"charPos":18,"endLineNo":18,"endCharPos":22},
	{"type":"w","text":"DEFAULT","lineNo":18,"charPos":23,"endLineNo":18,"endCharPos":30},
	{"type":"w","text":"NULL","lineNo":18,"charPos":31,"endLineNo":18,"endCharPos":35},
	{"type":"dc","text":",","lineNo":18,"charPos":35,"endLineNo":18,"endCharPos":36},
	{"type":"w","text":"ar_content_format","lineNo":19,"charPos":1,"endLineNo":19,"endCharPos":18},
	{"type":"w","text":"BLOB","lineNo":19,"charPos":19,"endLineNo":19,"endCharPos":23},
	{"type":"w","text":"DEFAULT","lineNo":19,"charPos":24,"endLineNo":19,"endCharPos":31},
	{"type":"w","text":"NULL","lineNo":19,"charPos":32,"endLineNo":19,"endCharPos":36},
	{"type":"dbc","text":")","lineNo":20,"charPos":1,"endLineNo":20,"endCharPos":2},
	{"type":"eos","text":"","lineNo":20,"charPos":2,"endLineNo":20,"endCharPos":2}
])

TABLE_DEF = TPSeq(
	TP("w", "CREATE", bIgnoreCase=True),
	TP("w", "TABLE", bIgnoreCase=True),
	TPAlt(
		TP("w", emitName="tableName"),
		TP("s", emitName="tableName")
	)
)

COL_DEF = TPSeq(
	TP("w", emitName="name"),
	TPAlt(
		TP("w", "INTEGER", bIgnoreCase=True),
		TP("w", "BLOB", bIgnoreCase=True),
		TP("w", "TEXT", bIgnoreCase=True),
		emitName="type"
	),
	TPOptional(
		TPSeq(
			TP("w", "NOT", bIgnoreCase=True),
			TP("w", "NULL", bIgnoreCase=True),
			emitName="nullable",
			emitValue=True
		)
	),
	TPOptional(
		TPSeq(
			TP("w", "DEFAULT", bIgnoreCase=True),
			TPAlt(
				TP("w", "NULL", bIgnoreCase=True),
				TP("i"),
				TP("s"),
				emitName="defaultValue"
			)
		)
	),
	TPOptional(
		TPSeq(
			TP("w", "PRIMARY", bIgnoreCase=True,
				emitName="pk",
				emitValue=True),
			TP("w", "KEY", bIgnoreCase=True),
			TP("w", "AUTOINCREMENT", bIgnoreCase=True,
				emitName="autoincr",
				emitValue=True),
		)
	)
)





def __tryEat_SQL_COLUMN_DEF(ts:jk_tokenizingparsing.TokenStream):
	m = COL_DEF.match(ts)
	if m:
		# print(m.values())
		return m.values()
	else:
		return None
#

def __tryEat_SQL_CREATE_TABLE(ts:jk_tokenizingparsing.TokenStream):
	m = TABLE_DEF.match(ts)
	if m:
		return { "table": m["tableName"], "columns": [] }
	else:
		return None
#

def parse(ts:jk_tokenizingparsing.TokenStream):
	retTable = __tryEat_SQL_CREATE_TABLE(ts)
	if retTable is None:
		raise jk_tokenizingparsing.ParserErrorException(ts.location, "P0001: Syntax error", "parse-1", ts.getTextPreview(20))

	m = TP("dbo").match(ts)
	if not m:
		raise jk_tokenizingparsing.ParserErrorException(ts.location, "P0001: Syntax error", "parse-2", ts.getTextPreview(20))

	while True:
		if ts.isEOS:
			raise jk_tokenizingparsing.ParserErrorException(ts.location, "P0001: Syntax error", "parse-3", ts.getTextPreview(20))

		dictData = __tryEat_SQL_COLUMN_DEF(ts)
		if dictData:
			col = {
				"name": dictData["name"][0],
				"type": dictData["type"][0],
				"nullable": dictData.get("nullable", False),
				"pk": dictData.get("pk", False),
				"autoincr": dictData.get("autoincr", False)
			}
			retTable["columns"].append(col)
		else:
			raise jk_tokenizingparsing.ParserErrorException(ts.location, "P0002: Syntax error", "parse-5", ts.getTextPreview(20))

		m = TP("dbc").match(ts)
		if m:
			return retTable

		m = TP("dc").match(ts)
		if m:
			continue

		raise jk_tokenizingparsing.ParserErrorException(ts.location, "P0001: Syntax error", "parse-4", ts.getTextPreview(20))
#







try:
	ts = jk_tokenizingparsing.TokenStream(TOKENS)
	parsingReslt = parse(ts)
	jk_json.prettyPrint(parsingReslt)
except jk_tokenizingparsing.ParserErrorException as e:
	e.print()





