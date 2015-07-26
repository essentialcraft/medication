#!/usr/bin/env python


#WEIGHT IN KILO * DOSAGE PER KILO = Y

import sys
import conversions as conv

print "\nLoading main:"

def main(args):
    print args

if __name__ == '__main__':


	if len(sys.argv) < 2:
		print 'No action specified.'
	elif sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == 'lbs-to-metric':
			lbs = sys.argv[2]
			print '{0:.2f} lbs is equal to {1:.2f} kgs'.format(float(lbs), float(conv.poundsToKilo(lbs)))
			print 'The input is {0:.2f} m'.format(float(sys.argv[3]))

	sys.exit()
	