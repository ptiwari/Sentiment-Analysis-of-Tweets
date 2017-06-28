"""
Make a pie chart - see
http://matplotlib.sf.net/matplotlib.pylab.html#-pie for the docstring.

This example shows a basic pie chart with labels optional features,
like autolabeling the percentage, offsetting a slice with "explode",
adding a shadow, and changing the starting angle.

"""
from pylab import *

def drawPie(labels,data):
	# make a square figure and axes
	figure(1, figsize=(6,6))
	ax = axes([0.1, 0.1, 0.8, 0.8])

	# The slices will be ordered and plotted counter-clockwise.
	
	explode=(0, 0.05, 0)

	pie(data, explode=explode, labels=labels,
					autopct='%1.1f%%', shadow=True, startangle=90)
					# The default startangle is 0, which would start
					# the Frogs slice on the x-axis.  With startangle=90,
					# everything is rotated counter-clockwise by 90 degrees,
					# so the plotting starts on the positive y-axis.

	title('Tweets Sentiment', bbox={'facecolor':'0.8', 'pad':5})

	show()