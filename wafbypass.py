import requests 
import os 
import webbrowser
  

#Input Target
search = input("Hostname/IP/Website:")
#Open Web-Page By From Censys/DNSTrails Input Search-Engine
url = f"https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q={search}"
url2 = f"https://securitytrails.com/domain/{search}"

#Function To Open The Pages In The Browser
webbrowser.open(url, new=2)
webbrowser.open(url2, new=2)










