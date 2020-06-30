tld=raw_input("Input The TLD: ")

dork=open("dork.txt","r")
out=open("dork_"+tld+".txt", "a")

for i in dork:
    out.write(i.replace('\n','')+" site:."+tld+"\n")

dork.close()
out.close()
