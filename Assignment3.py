#Assignment3 - Text Processing

import argparse
from urllib.request import urlopen #import urllib2 

import csv
import re
import datetime


def downloadData(url):
    #Part I - Pull Down Web Log File
    #A function to download the contents located at the url and return to the caller.
    #The program should download the web log file from the location provided by a url parameter. 
    get_url = urllib.request.urlopen(url)  #urlopen(url)
    return get_url

#Part II - Process File Using CSV
def processData(content):
    #initializing each varaible to 0 for browsers and counts
    counts = {'imagehit':0,
              'rowcount':0}

    browsers = {'Internet Explorer':0,
                'Firefox':0,
                'Google Chrome':0,
                'Safari':0}
                
#Part III - Search for Image Hits
#searching for all hits that are for an image file extensions that is either .jpg, .gif or .png
    for line in csv.reader(content):
        counts['rowcount'] += 1
        if re.search(r"jpe?g|JPE?G|GIF|PNG|gif|png", line[0]):
            counts['imagehit'] += 1
            
            #I will print out this later in the program "image requests account for 45.3% of all requests"
            
#Part IV - Finding Most Popular Browser
#find out which browser people are using is the most popular - Firefox, Chrome, Internet Explorer or Safari.
        if re.search("MSIE", line[2]):
            browsers['Internet Explorer'] += 1
        elif re.search("Chrome", line[2]):
            browsers['Google Chrome'] += 1
        elif re.search("firefox", line[2], re.I):
            browsers['Firefox'] += 1
        elif re.search("Safari", line[2]) and not re.search("Chrome", line[2]):
            browsers['Safari'] += 1
            
          #again I will print out which browser is the most polular later in the program 

#Part VI - Extra Credit
#Printing everything here at once:
    Hours_Sort(line)
    image_result = (float(counts['imagehit']) / counts['rowcount']) * 100
    print("Image requests account for {}% of all requests".format(image_result))
        
    top_browsed =  max(browsers, key=browsers.get)
    print("{} is the most popular broswer with {} uses.".format(top_browsed, browsers[top_browsed]))
    
    hours = {0: 0, 1: 0, 2: 0, 3: 0,
         4: 0, 5: 0, 6: 0, 7: 0,
         8: 0, 9: 0, 10: 0, 11: 0,
         12: 0, 13: 0, 14: 0, 15: 0,
         16: 0, 17: 0, 18: 0, 19: 0,
         20: 0, 21: 0, 22: 0, 23: 0, }
         
    for hour in hours:
        print("Hour {} has {} hits.".format(hour, hours[hour]))
        
def Hours_Sort(line):
    hour = (datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S")).hour

    hours[hour] += 1
    
    
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="URL to csv file")
    args = parser.parse_args()

    if args.url:
        try:
            inf = downloadData(args.url)
            processData(inf)
        except urllib.request.urlopen.URLError as url_err:
            print ("URL is INVALID")
            raise url_err
    else:
        print ("Please enter a valid URL.")

if __name__ == '__main__':
    main()
