

from bs4 import BeautifulSoup
import csv
import re

from ebay_finder import findEbay

csvData = []

file = open(input("Enter the html file to parse: "))
soup = BeautifulSoup(file, 'html.parser')

h_products = soup.td.table('tr')

for prod in h_products[1:-1]:
	name_ptr = prod.td

	if name_ptr.text == '':
		break

	qty_ptr = prod.td.find_next_sibling()
	total_retail_ptr = qty_ptr.find_next_sibling().find_next_sibling()

	ebay_name = re.sub('[^/w ]', '', name_ptr.text)
	print(ebay_name)
	ebay_price = findEbay(ebay_name).strip()
	csvData.append([name_ptr.text, qty_ptr.text, total_retail_ptr.text, ebay_price])


with open(input("Enter output csv file name: "), 'w', newline='') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(csvData)

csvFile.close()

# fp = urllib.request.urlopen("C:/Users/Tim/Desktop/liquidation.html")
# mybytes = fp.read()
# mystr = mybytes.decode("utf8")

# file = open("liquidation.html")
# print(file.read())


# tree = html.parse('liquidation.html')
# result = html.tostring(tree.getroot(), pretty_print=True, method='html')
# print(tree.getroot().text_content())
