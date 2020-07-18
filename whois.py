from ipwhois import IPWhois
from pprint import pprint
import json
filename=input("Enter the Filename to extract IP from ")
alist=[]
f=open(filename,"r")
for i in f:
	ip=i.rstrip('\n')
	obj=IPWhois(ip)
	name=ip+".csv"
	with open(name,'w') as outfile:
		results=obj.lookup_rdap(depth=1)
		json.dump(results,outfile,indent=4)
	
f.close()
print("Completed")