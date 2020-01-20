#!/usr/bin/python3



import timeit

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



def avg(*args):
	return sum(*args) / len(args)
#



m = x.match(ts)
print(m)
print(m.values())
print()



nRepeat = 100000
timeValues = timeit.repeat(stmt="ts.reset(); x.match(ts)", globals={
	"x": x,
	"ts": ts,
}, repeat=1, number=nRepeat)
n = avg(timeValues)
print("%.4f µs per run = %d runs per sec" % ( n * 1000000 / nRepeat, nRepeat/n ) )





























