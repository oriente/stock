import csv

'''Date,Open,High,Low,Close,Volume
'''
def csvParser(filename):
	print filename
	yydata = open(filename, 'r')
	data_stream = csv.reader(yydata)
	return data_stream


def dataAnalyzer(data):
	data_list = []
	for row in data:
		data_list.append(row)
	data_list.reverse()
	return data_list

def decreaseAnalyzer(data_list):
	ndays = 5
	for i in range(len(data_list)-ndays):
		day1_price = float(data_list[i][4])
		day2_price = float(data_list[i+1][4])
		isDec = (day2_price < day1_price)
		if isDec:
			DecPercent = (day2_price - day1_price)*100/day1_price
			# single day performance  
			if DecPercent < -5:
				print data_list[i]
				price_change_percent = []
				for d in range(1,ndays):
					cur_price = float(data_list[i+d][4])
					next_price = float(data_list[i+1+d][4])
					price_change_percent.append((cur_price-next_price)*100/cur_price)
				print DecPercent
				print price_change_percent


def increaseAnalyzer(stock_list):
	ndays = 3
	# best increase 

	for i in range(len(stock_list)-ndays):
		day1_price = float(stock_list[i][4])
		day2_price = float(stock_list[i+1][4])
		day3_price = float(stock_list[i+2][4])
		threeDayInc = (day3_price > day2_price) and (day2_price > day1_price)
		if threeDayInc:
			firstPercent = (day2_price - day1_price)*100/day1_price
			secondPercent = (day3_price - day2_price)*100/day2_price
			incPercent = (day3_price - day1_price)*100/day1_price
			if firstPercent > 4:
				# performance of two consecutive days 
				# if the first day increase is higher than 8%
				# print stock_list[i]
				print firstPercent, secondPercent, incPercent

	#
	'''
	for i in range(len(stock_list)-2):
		day1_price = float(stock_list[i][4])
		day2_price = float(stock_list[i+1][4])
		isInc = (day2_price > day1_price)
		if isInc:
			incPercent = (day2_price - day1_price)*100/day1_price
			# single day performance  
			if incPercent > 8:
				print stock_list[i]
				print incPercent
	'''
parsedStream = csvParser('wuba.csv')
data = dataAnalyzer(parsedStream)
decreaseAnalyzer(data)

