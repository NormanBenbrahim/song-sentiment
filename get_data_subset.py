#!/usr/bin/env python

# Norman Benbrahim
# Thursday Jan 28 2016

import urllib
import os
import tarfile
import tempfile

if not os.path.exists("./data"):
	print "Creating data folder"
	os.mkdir("./data")

if not os.path.exists("./data/millionsongsubset_full.tar.gz"):

	# the location of the data
	subsetUrl = "http://static.echonest.com/millionsongsubset_full.tar.gz"

	print "Downloading subset of million songs (10 000 songs, 1% of dataset)..."
	urllib.urlretrieve(subsetUrl, "./data/millionsongsubset_full.tar.gz")
	
	print "Extracting contents..."
	tar = tarfile.open("./data/millionsongsubset_full.tar.gz")
	tar.extractall("./data/")
	os.remove("./data/millionsongsubset_full.tar.gz")
	print "Saved dataset in './data/'"