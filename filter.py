list=open("clean.txt","r").readlines()
filter=open("filter.txt","r").readlines()
out=open("final.txt","a")

for link in list:
    for query in filter:
        if query.lower().replace("\n","") in link.lower():
            out.write(link)
            break
        else:
            pass

# list.close()
# filter.close()
out.close()
