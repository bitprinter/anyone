#!/usr/bin/python2.7

import data.namesbystate.loader
data.namesbystate.loader.run()

import data.zipcodes.loader
data.zipcodes.loader.run()

import data.surnames.loader
data.surnames.loader.run()

print "OK!"
