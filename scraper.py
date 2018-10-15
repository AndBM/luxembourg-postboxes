import urllib.request as ur

filename = "addresses.txt"
cities = ["LUXEMBOURG"]
addresses = []

# Apply headers to avoid a 403 Forbidden error
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
baseUrl = "https://www.post.lu/naos-microapps-app/ajax/json/getBoxForCity.json?city="


for i in range(len(cities)):
    print("City " + str(i+1))
    # Get the first page
    url = baseUrl + cities[i] + "&page=0"
    request = ur.Request(url,None,headers)
    response = ur.urlopen(request)
    webContent = str(response.read())

    # Find out how many pages there are
    beg1 = webContent.find("totalPages")+12
    end1 = webContent.find("numberOfElements")-2
    pages = int(webContent[ beg1:end1 ])

    for j in range(pages):
        print("Page " + str(j+1))
        # Get each page
        url = baseUrl + cities[i] + "&page=" + str(j)
        request = ur.Request(url,None,headers)
        response = ur.urlopen(request)
        webContent = str(response.read())

        # Initialize
        beg2 = webContent.find("rue")+6
        end2 = webContent.find("localite")-3
        stopper = webContent.find("sort")
        while  beg2 < stopper :
            # Read each address
            address = webContent[ beg2:end2 ]
            addresses.append(address)
            beg2 = webContent.find("rue", beg2)+6
            end2 = webContent.find("localite", end2+4)-3

    with open(filename, 'w') as file:
        for i in range(len(addresses)):
            if cities[i] == "LUXEMBOURG":
                file.write("Luxembourg City, " + addresses[i] + "\n")
            else:
                file.write(cities[i] + ", " + addresses[i] + "\n")
