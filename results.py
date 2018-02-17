#author: Akhil Bharti
#sudo pip3 install requests
#sudo pip3 install bs4
#python3 results.py

import requests
from bs4 import BeautifulSoup as soup

#update range of roll numbers
start = 12615001001	
end = 12615001200

#update semester
sem = 5

for roll in range(start,end):
	result = requests.post('http://61.12.70.61:8084/heresult18o.aspx',data={'roll':roll,'sem':sem})
	page_html = result.content
	page_soup = soup(page_html,"html.parser")
	name_con = page_soup.findAll("span", {"id":"lblname"})
	if len(name_con)>0:
		name = name_con[0].text
	cgpa_con = page_soup.findAll("span", {"id":"lblbottom1"})
	if len(cgpa_con)>0:
		cgpa = cgpa_con[0].text
		if name[6]=='Â':
			name = name[8:]
		else:
			name = name[6:]
		name = name
		print(name+'\t\t'+cgpa[30:])