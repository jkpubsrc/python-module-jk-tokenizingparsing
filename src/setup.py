from setuptools import setup


def readme():
	with open("README.rst") as f:
		return f.read()


setup(name="jk_tokenizingparsing",
	version="0.2018.3.28",
	description="This python module provides basic classes for tokenizing and parsing.",
	author="Jürgen Knauth",
	author_email="pubsrc@binary-overflow.de",
	license="Apache 2.0",
	url="https://github.com/jkpubsrc/python-module-jk-tokenizingparsing",
	download_url="https://github.com/jkpubsrc/python-module-jk-tokenizingparsing/tarball/0.2018.3.28",
	keywords=[
		"parsing"
		],
	packages=[
		"jk_tokenizingparsing",
		"jk_tokenizingparsing.tokenmatching"
		],
	install_requires=[
	],
	include_package_data=True,
	classifiers=[
		"Development Status :: 4 - Beta",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Apache Software License"
	],
	long_description=readme(),
	zip_safe=False)

