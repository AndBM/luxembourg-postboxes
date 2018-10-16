import json
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
    response_text = response.read().decode("utf-8", errors="replace")
    webContent = json.loads(response_text)

    pages = webContent["totalPages"]

    for j in range(pages):
        print("Page " + str(j+1))
        # Get each page
        url = baseUrl + cities[i] + "&page=" + str(j)
        request = ur.Request(url,None,headers)
        response = ur.urlopen(request)
        response_text = response.read().decode("utf-8", errors="replace")
        webContent = json.loads(response_text)

        for entry in webContent["content"]:
            address = entry["rue"].strip()
            addresses.append(address)

    with open(filename, 'w') as file:
        for address in addresses:
            if cities[i] == "LUXEMBOURG":
                file.write("Luxembourg City, " + address + "\n")
            else:
                file.write(cities[i] + ", " + address + "\n")
