#!/usr/bin/env python
#
#   DSLRtimer.py  DSLR astro timer  for  ASIAIR pro
#
#   Version 1.0
#
#   Copyright (c) 2020 Roman Hujer   http://hujer.net
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,ss
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Description:
#
#



import os 
import logging
import argparse 
import time
import RPi.GPIO as GPIO


parser = argparse.ArgumentParser( description='DSLRTimer.' 'DSLR Astro timer')

parser.add_argument('--exptime', '-e', default=30,
                    help='exp. time (default: 30 sec.)')
parser.add_argument('--wait', '-w', default=5,
                    help='wait for next exp. (default: 5 sec.)')
parser.add_argument('--count', '-c', default=1,
                    help='exp. counts (default: 1')
parser.add_argument('--mode', '-m', default='bulb',
                    help='mode bulb|pulse (default: bulb)')
parser.add_argument('--lock', '-l', default=0,
		    help='pre mirror lock sec. - only in pulse mode (defsult: 0 is disable')

args = parser.parse_args()

logging.debug("command line arguments: " + str(vars(args)))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

print args.mode

for x in range(args.count):
	print 'Count %d ' % x
	if args.mode == 'bulb' :
		GPIO.output(21, GPIO.LOW)
		time.sleep(args.exptime)
		GPIO.output(21, GPIO.HIGH)
		time.sleep(args.wait)

	else:
		if args.lock  > 0 :
			GPIO.output(21, GPIO.LOW)
			time.sleep(1)
			GPIO.output(21, GPIO.HIGH)
			time.sleep(args.lock)
 		GPIO.output(21, GPIO.LOW)
                time.sleep(1)
                GPIO.output(21, GPIO.HIGH)
                time.sleep(args.exptime+args.wait)

print 'End'

