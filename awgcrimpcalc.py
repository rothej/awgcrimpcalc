# AWG Wire Calculator v1.0.0
# Written by Joshua Rothe

# This code calculates the AWG size of a wire crimp required when combining
# multiple sets of stranded wires in a single crimp. Made w/o add'l modules.

import sys

#########################
# Following array compares AWG values for stranded wire to their mm^2 
# area, from 0 to 40AWG. Used as the primary reference for this module
AWGArray = [[0,53.5],[1,42.4],[2,33.6],[3,26.7],\
[4,21.2],[5,16.8],[6,13.3],[7,10.5],[8,8.37],[9,6.63],[10,5.26],[11,4.17],[12,3.31],\
[13,2.62],[14,2.08],[15,1.65],[16,1.31],[17,1.04],[18,0.823],[19,0.653],[20,0.518],\
[21,0.410],[22,0.326],[23,0.258],[24,0.205],[25,0.162],[26,0.129],[27,0.102],\
[28,0.0810],[29,0.0642],[30,0.0509],[31,0.0404],[32,0.0320],[33,0.0254],[34,0.0201],\
[35,0.0160],[36,0.0127],[37,0.0100],[38,0.0080],[39,0.0063],[40,0.0050]]
#########################
# Following function converts wire AWG to area, mm^2
def AWGToMm(inAWG):
	for i in range(len(AWGArray)):
			if AWGArray[i][0] == inAWG:
				return AWGArray[i][1]
	sys.exit("Error with input.")
#########################
# Following function converts wire area (mm^2) to AWG
def mmToAWG(inMm):
	for i in range(len(AWGArray)):
		if AWGArray[i][1] <= inMm:
			if AWGArray[i][1] == inMm:	# if exactly equal, return that AWG
				return AWGArray[i][0]
			else:							# otherwise go one size larger
				if AWGArray[i][0] == 0:		# unless we are already at 0AWG
					sys.exit("The size needed for this crimp is beyond the scope\
 of this program.")
				else:
					return AWGArray[i-1][0]
#########################
# Following function checks input and returns an error if the input is invalid
def inputWireChecker(input):
	for i in range(len(AWGArray)):
		if AWGArray[i][0] == input:
			return
	sys.exit("Invalid entry.")
#########################
# Following function makes sure either 2 or 3 wires are being crimped
def inputHowManyWiresChecker(input):
	if input == 2 or input == 3:
		return
	else:
		sys.exit("Invalid qty of wires crimped. Expecting 2 or 3.")
#########################
# Begin module

print("AWG Wire Calculator v1.0.0")
inputHowManyWires = int(input("How many wires are being crimped together? 2 or 3: "))
inputHowManyWiresChecker(inputHowManyWires)

inputWireFirst = int(input("Enter AWG of first wire (0 AWG to 30 AWG): "))
inputWireChecker(inputWireFirst)

inputWireSecond = int(input("Enter AWG of second wire (0 AWG to 30 AWG): "))
inputWireChecker(inputWireSecond)

if inputHowManyWires == 3:
	inputWireThird = int(input("Enter AWG of third wire (0 AWG to 30 AWG): "))

# Convert wire inputs to mm^2 area
mmWire1 = AWGToMm(inputWireFirst)
mmWire2 = AWGToMm(inputWireSecond)
if inputHowManyWires == 3:
	mmWire3 = AWGToMm(inputWireThird)

# Combine areas
mmWireTotal = mmWire1 + mmWire2
if inputHowManyWires == 3:
	mmWireTotal += mmWire3

# Converts result back to AWG
AWGWireTotal = mmToAWG(mmWireTotal)
# Print answer, with number as a string
print("The AWG size needed to crimp the input wires is " + str(AWGWireTotal))

# End module
