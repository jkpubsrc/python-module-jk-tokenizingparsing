#!/usr/bin/python3



import timeit

from jk_tokenizingparsing import *
from jk_tokenizingparsing.tokenmatching import *



tokens1 = [
	Token("w", "someVar", None, None, None, None, None),
	Token("d", "=", None, None, None, None, None),
	Token("w", "a", None, None, None, None, None),
	Token("d", "+", None, None, None, None, None),
	Token("w", "b", None, None, None, None, None),
	Token("eos", "", None, None, None, None, None),
]
ts1 = TokenStream(tokens1)

tokens2 = [
	Token("w", "someVar", None, None, None, None, None),
	Token("d", "=", None, None, None, None, None),
	Token("w", "b", None, None, None, None, None),
	Token("d", "+", None, None, None, None, None),
	Token("w", "a", None, None, None, None, None),
	Token("eos", "", None, None, None, None, None),
]
ts2 = TokenStream(tokens2)

tokens3 = [
	Token("w", "someVar", None, None, None, None, None),
	Token("d", "=", None, None, None, None, None),
	Token("d", "+", None, None, None, None, None),
	Token("w", "b", None, None, None, None, None),
	Token("w", "a", None, None, None, None, None),
	Token("eos", "", None, None, None, None, None),
]
ts3 = TokenStream(tokens3)




x = TPSeq(
	TP("w", "someVar", emitName="varName"),
	TP("d", "="),
	TPUnordSeq(
		TP("w", "a", emitName="value"),
		TP("w", "b", emitName="value"),
		TP("d", "+")
	),
)






m = x.match(ts1)
print(m)
print(m.values())
print()
m = x.match(ts2)
print(m)
print(m.values())
print()
m = x.match(ts3)
print(m)
print(m.values())
print()





























