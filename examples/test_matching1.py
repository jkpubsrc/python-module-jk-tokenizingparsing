#!/usr/bin/python3



from jk_tokenizingparsing import *
from jk_tokenizingparsing.tokenmatching import *



tokens = [
	Token("w", "create", None, None, None, None, None),
	Token("w", "table", None, None, None, None, None),
	Token("w", "myFancyTable", None, None, None, None, None),
	Token("eos", "", None, None, None, None, None),
]




ts = TokenStream(tokens)
tp1 = TP("w", "CREATE", bIgnoreCase=True, emitName="first")
m = tp1.match(ts)
print(m)
print(m.values())
print()




ts = TokenStream(tokens)
tp2 = TP("w", "TABLE", bIgnoreCase=True, emitName="second")
tp3 = TP("w", emitName="third")
tp123 = TPSeq(tp1, tp2, tp3)
m = tp123.match(ts)
print(m)
print(m.values())
print()
print(m.valuesTokens())
print()




