#!/usr/local/bin/python2.7
import csv
import requests
from bs4 import BeautifulSoup

brattleboro = 'http://www.dlp.vermont.gov/standard-surveys-hospitals/brattleboro-acc-poc-folder/'
response = requests.get(brattleboro)
html = response.content
soup = BeautifulSoup(html)

reports = soup.find_all('dt')
list_of_reports = []

for report in reports:
    new_report = report.a.string
    list_of_reports.append(str(new_report))

del list_of_reports[-1]


outfile = open("./reports.csv", "wb")
writer = csv.writer(outfile)
writer.writerows([list_of_reports])
