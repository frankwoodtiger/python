import urllib # for pathname2url
import urllib2 # for getting data from URL
import csv # post-processing data in CSV
import matplotlib.pyplot as plt
import collections
import datetime

def plotGraphByURL(figureNum, symbol, fromDate, toDate):
	params = ["{:0>2d}".format(fromDate.month - 1), str(fromDate.day), str(fromDate.year), "{:0>2d}".format(toDate.month - 1), str(toDate.day), str(toDate.year)]
	
	url = "http://real-chart.finance.yahoo.com/table.csv?s=" + urllib.pathname2url(symbol) + "&a=" + params[0] + "&b=" + params[1] + "&c=" + params[2] + "&d=" + params[3] + "&e=" + params[4] + "&f=" + params[5] + "&g=d&ignore=.csv"
	response = urllib2.urlopen(url)
	cr = csv.reader(response) 
	cr.next()
	

	dataInDict = {row[0]:float(row[1]) for row in cr}
	orderedData = collections.OrderedDict(sorted(dataInDict.items()))
	x = range(1, len(orderedData)+1)
	fig = plt.figure(figureNum)
	plt.xlabel("Date")
	plt.title(symbol)
	plt.xticks(x, orderedData.keys(), rotation=45)
	plt.plot(x, orderedData.values())	
	plt.grid()
	fig.show()

# a: month (00 - 11), b: day (1 - 31)
# ^HSI - http://finance.yahoo.com/q/hp?s=%5EHSI&a=00&b=1&c=2014&d=11&e=31&f=2014&g=m 
# HSBC - http://finance.yahoo.com/q/hp?s=HSBC&a=00&b=1&c=2014&d=11&e=31&f=2014&g=m 
# AAPL - apple
# url = "http://real-chart.finance.yahoo.com/table.csv?s=%5EHSI&a=06&b=1&c=2014&d=11&e=31&f=2014&g=d&ignore=.csv"

def usePlotGraphByURL():
	fromDate = datetime.date(2015,1,1)
	toDate = datetime.date(2015,8,1)

	plotGraphByURL(1, "HSBC", fromDate, toDate)
	plotGraphByURL(2, "AAPL", fromDate, toDate)

	raw_input() # to sustain the graphs

# usePlotGraphByURL()

# dimension specifies [rows, columns]
# symbols specifies the yahoo symbols in array ["GOOG", "AAPL", "HSBC"]
def plotGraphsInOnePageByURL(dimension, symbols, fromDate, toDate):
	numOfGraph = len(symbols)
	subPlotParam = "".join([str(i) for i in dimension])
	params = ["{:0>2d}".format(fromDate.month - 1), str(fromDate.day), str(fromDate.year), "{:0>2d}".format(toDate.month - 1), str(toDate.day), str(toDate.year)]

	for i in range(numOfGraph):
		plt.subplot(int(subPlotParam + str(i+1)))
		url = "http://real-chart.finance.yahoo.com/table.csv?s=" + urllib.pathname2url(symbols[i]) + "&a=" + params[0] + "&b=" + params[1] + "&c=" + params[2] + "&d=" + params[3] + "&e=" + params[4] + "&f=" + params[5] + "&g=d&ignore=.csv"
		print url
		response = urllib2.urlopen(url)
		cr = csv.reader(response) 
		cr.next()
		
		dataInDict = {row[0]:float(row[1]) for row in cr}
		orderedData = collections.OrderedDict(sorted(dataInDict.items()))
		x = range(1, len(orderedData)+1)
		plt.xlabel("Date")
		plt.title(symbols[i])
		plt.xticks(x, orderedData.keys(), rotation=45)
		plt.plot(x, orderedData.values())	
		plt.grid()
	
	plt.show()
	
fromDate = datetime.date(2015,1,1)
toDate = datetime.date(2015,8,1)
plotGraphsInOnePageByURL([2,2], ["^HSI", "0005.HK", "0011.HK", "0066.HK"], fromDate, toDate)