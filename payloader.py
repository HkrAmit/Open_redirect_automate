list=open("final.txt","r").readlines()
filter=open("filter.txt","r").readlines()
out=open("payloaded.txt","a")
out2=open("double.txt","a")

for link in list:
    for query in filter:
        if query.lower().replace("\n","") in link.lower():
            first_index=link.lower().find(query.lower().replace("\n",""))+len(query)-1
            #print(first_index)
            last_index=first_index+len(link.lower().split(query.lower().replace("\n",""))[1].split("&")[0])-1
            #print(last_index)
            if link.find(link[first_index:last_index])==link.rfind(link[first_index:last_index]):
                payload=link.replace(link[first_index:last_index],"https://www.openbugbounty.org/")
                #print(payload)
                out.write(payload)
            else:
                out2.write(link)
                #print("Double > "+link)
            #payload=link.replace(link.lower().split(query.lower().replace("\n",""))[1].split("&")[0],"https://www.openbugbounty.org/\n")
            #out.write(payload)
            break
        else:
            pass

# list.close()
# filter.close()
out.close()
