#!/usr/bin/env python3
# -*- coding: utf-8 -*-





class TokenStreamMark(object):

	def __init__(self, tokenStream):
		self.__pos = tokenStream.position
		self.__tokenStream = tokenStream
	#

	def resetToMark(self):
		self.__tokenStream._setPosition(self.__pos)
	#

#








