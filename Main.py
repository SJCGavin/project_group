import pydoc

from pathlib import Path
import csv
import re
empty_list = []
with open(r".\csv_reports\Profit-and-loss-usd.csv","r") as file:
    reader=csv.reader(file)
    next(reader)
    for line in reader:
        empty_list.append(line)
for list in empty_list:
    data=[list[0],list[3]]
    print(data)






# for file in fp.glob('*.csv'):
#     with file.open (mode='r') as file:
#         profit_and_loss = file.read()
# # with fp.open (mode="r", encoding = "UTF-8") as file1:
# #     reader= csv.reader(file1)
# #     next(reader)
# #     for line in reader:
# #         for value in line:
# #             coh = re.findall(pattern = r"[0-9][0-9][0-9]+", string = value)
# #             empty_list.append(coh)
# # print(empty_list)
# with fp.open (mode="r", encoding = "UTF-8", newline = "") as file1:
#     profit_and_loss = file1.read()
#     empty_list.append(profit_and_loss)
#     for profit_and_loss in empty_list:
#         profitloss = re.findall (pattern = r"[0-9]+", string = profit_and_loss)
#         netprofits = (profitloss)
# print (netprofits)



