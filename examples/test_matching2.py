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
tp2 = TP("w", "TABLE", bIgnoreCase=True, emitName="second")
tp3 = TPOptional(TP("w", "NULLABLE", bIgnoreCase=True, emitName="third"))
tp4 = TP("w", emitName="fourth")
tp1234 = TPSeq(tp1, tp2, tp3, tp4)

m = tp1234.match(ts)
print(m)
print(m.values())
print()
print(m.valuesTokens())
print()
































