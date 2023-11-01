while 1:
    word=input("Words: ")
    long=input("Long? ")

    website="https://en.wikipedia.org/wiki/"+word

    import requests
    from bs4 import BeautifulSoup

    page=requests.get(website)
 #   if (page==None): 
       # print("Invalid Words")

    
    soup= BeautifulSoup(page.content, "html.parser")
    if soup.find_all(string="Wikipedia does not have an article with this exact name")!=[]:
        print("No Definition")
        continue
    for s in soup.strings:
        if "may refer to" in s:
            print("Multiple options:")
            print(soup.find(class_="side-box side-box-right plainlinks sistersitebox").next_sibling.next_sibling.next_sibling.next_sibling.text)
            continue
    actresults=""
    if long=="false":
        results=soup.find("div",class_="shortdescription nomobile noexcerpt noprint searchaux").text
        print(results)
    elif long=="true":
        results=(soup.find_all("p"))
        for i in range(0,3):
            actresults=actresults+results[i].text
        for z in range(1,100):
            actresults=actresults.replace("["+str(z)+"]","")
        print(actresults)
        

 #   if results=="Topics referred to by the same term":
  #      continue
