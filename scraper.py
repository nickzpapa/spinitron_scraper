import requests
import os
from bs4 import BeautifulSoup


def main():
	url = raw_input('Enter a url:> ');
	html = getPageText(url);
	soup = BeautifulSoup(html);
	textFile = open(getDateShowandDJ(soup), "w+")

	for temp in soup.find_all('div', 'nfo'):
		line = getArtist(temp.contents[1]) + ' - ' + getSong(temp.contents[1])
		line = line.encode( "utf-8" )
		textFile.write(line + '\n')


def getPageText (url):
	r = requests.get(url);	
	if (r.status_code != 200):
		print "Error (" + r.status_code + "). Could not fulfill request.";
		exit;
	else:
		return r.text;

def getDateShowandDJ (soup):
	dj = soup.find('div', "infoblock lead ").contents[1].text # getting DJ
	dj = dj.replace('With ', "").replace(' ', '_')			  # fixing str

	show = soup.find('p', "plhead").contents[0].string		# getting show

	date = soup.find('p', "plheadsub leadpad").string # getting date
	date = date.replace('.', '').replace(' ', '_');	  # fixing str
	return dj + '_' + date


def getArtist( p ):
	soup = BeautifulSoup(str(p))
	return soup.find('span','aw').string

def getSong( p ):
	soup = BeautifulSoup(str(p))
	return soup.find('span','sn').string



if __name__ == '__main__':
	main()