#!/usr/bin/python3



from jk_tokenizingparsing import *
from jk_tokenizingparsing.tokenmatching import *



tokens = [
	Token("w", "someVar", None, None, None, None, None),
	Token("d", "=", None, None, None, None, None),
	Token("d", "[", None, None, None, None, None),
	Token("s", "gallia", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "est", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "omnis", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "divisa", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "in", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "partres", None, None, None, None, None),
	Token("d", ",", None, None, None, None, None),
	Token("s", "tres", None, None, None, None, None),
	Token("d", "]", None, None, None, None, None),
	Token("eos", "", None, None, None, None, None),
]
ts = TokenStream(tokens)




x = TPSeq(
	TP("w", "someVar", emitName="varName"),
	TP("d", "="),
	TP("d", "["),
	TPRepeat(
		TP("s", emitName="value"),
		TP("d", ",")
	),
	TP("d", "]")
)

m = x.match(ts)
print(m)
print(ts.peek())
print(m.values())
print()
































