list=open("list.txt","r")
clean=open("clean.txt","a")

found=set()

for line in list:
    site=line.replace(line.split("/",3)[3],'')
    if site in found:
        pass
    else:
        clean.write(line)
        found.add(site)
