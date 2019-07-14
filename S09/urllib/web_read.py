# import urllib.request

# with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
# print(html)


import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://python.org/')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)


# link = 'https://python.org/'
# f = urllib.urlopen(link)
# myfile = f.readline()
# print
# myfile
