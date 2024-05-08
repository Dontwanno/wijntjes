import time

from bs4 import BeautifulSoup
import requests
import pandas as pd

cookies = {
    'SSLB': '1',
    'SSID': 'CQD5OB1-AAQAAAAQBPdly4xAARAE92UMAAAAAAAAAAAAcoI7ZgBUmnYLAAED2AAAcoI7ZgEAXAsAAcnXAABygjtmAQCACwABSdgAAHKCO2YBAGcLAAEZ1wAAcoI7ZgEAjQsAAdjYAABygjtmAQCICwABetgAAHKCO2YBAGMLAAHd1gAAcoI7ZgEAYgsAAdnWAABygjtmAQDiCgABedIAAHKCO2YBAFsLAAA',
    'SSSC': '4.G7347345783865248971.12|2786.53881:2908.55241:2914.55001:2915.55005:2919.55065:2934.55299:2944.55369:2952.55418:2957.55512',
    'i18next': 'nl-nl',
    '_csrf': 'W-l28hsjPQ8yZ-PX03ixy8t_',
    'Ahonlnl-Prd-01-DigitalDev-F1': '!lbEyWpfvfI7laVzZn/IR7WT7ZKUq0y5bafQ2xxJiz08+iyJpi4F8cRetj3EymUYPwkX6UzNoOo6lJeI=',
    'Ahonlnl-Prd-01-DigitalDev-B2': '!Fr5YKutOFTP9Cr5ZQI6MIhlj9SYhsX2thWfrwWpH2102BBSHeuesLOCHplA+FMzDDhp0XZR7PKHt',
    'bm_sz': 'B7001A790159E5D1A2631503F1EBDCEE~YAAQHjdlX2O+N1iPAQAAopZ1WBd8eJk0p62LO65zXA47u/j/HlOZYa203LV6mWkcZ21yAY42jVO5L3P4/bsEvGlocoIj/XTII/AjMK1g0NSaNqcRRDUznWYOWvBFaYkZEmUq2a9u8JxzevHBxaKzq7z51pF9xGrGCy2N9f4NfM1vbB2v3C6w2CMCmdEOZswJ5XDYOQ79GM1Yfklf8rtin6eMD9+Ip3CW9SQM+MhMUAFWADEL1x/PpsfGBU7iDL0GtNZlIpx++Lhb781RMmg4k8ydgqUzEUDR0jcKSYelR0Qf92cklnqJ09jil+NW28JIrn3LOcAqPkoFSkuIzFRXQE1lSB5O/KskPErDJYSpB5O3RpgTgg==~4272950~3162681',
    'SSOD': 'ANVpAAAAJADqkwAAEAAAABIE92XfgjtmAwC_egAAAQAAAGJdIWZiXSFmAAAAAA',
    'bm_mi': 'CBA638C2A445E543850662B6046DDF91~YAAQFDdlX0wVSVaPAQAAREp4WBfgttrLX/Hf3zYZoyIYALdifWC/QuzB3QwJpQDVYJp3HgyhmTO+ezqjOWoLyGZNVExuAcqFo4iUmqjcywNHrM5fSh+fcoS5MXsGSnLTUpLCpwgz2uwuQQhwCRM1exLh/IfEbdhSPVY/X+SRfCYTW2y1tWa6NI3eWPyftpvCA4fM53G+vVf3kWuPleeQFC4tlHAVjuJgHkYpmkzAmPJcwWZf8H7wX48hjW4U1KP/aBpMJjdQFkYr8ecYg+5iJrLXQC6r+uWQmWneBNilvnypwFHjmU56by7NAXt480PPZEGxXB0c~1',
    'bm_sv': 'FC4888A53707ED31DD0A1746840AFFB9~YAAQFDdlX9cXSVaPAQAA/4d4WBfn55+QBGnJcEAwC5LMKIiMOETgLRfDK+60ZGGB8bg9u1SoZv3nX8SV4v3US9msK5kvPgcSgsAcaIlC6GSI4c1yBKpk+NUzv57xVcZTvrM4tNKu2wRkBBN5Ug5Lo55tb4e+3VG3QMs1P2gmuP9kCndmDoJr5aKtrAuKudSSstd6uQb6smr7L1gf1gHUPvMDVEHrja5n/TTw5V/g7R0DecY/xhVhyRsEH6dM/V/i~1',
    'ak_bmsc': '7581AFFABD687891C2C794BA6DA12966~000000000000000000000000000000~YAAQMTdlX0W9IE+PAQAAQ19/WBdh0jqB5wkfLyshTCVul29gD+xUS00wvZpcAdEJp5neoydslsqCR+l1yRmfyjJJqdDuOXs5s0OA100nZcAoMxfYxSunRnLXpWCsgT/I2lKR3lE7Nu5hZ/tk6Hqz+XAUgTdyYTsnAGDsm7+ypnQJ3VWYfc6DyaoK1Lv6+PEVIrebLxqyFpsbS/omLTI0vPcXqZGC2gjKS0EU+L3RK+plml/jDQ9/v5Cn7f9gZRWeqVePy9WfA8R/mPiYPK1uR533cIgfGB9wN0Vk5Fx9ZcdchuADPOlJGhocPUyNfCRWCSHS8D3y7o0Z5CuPA3sUI5xC0jHTw0yCL+BXTYXqpW6XJzqTg6giZ18ELeG6DloiIWpIozQ0dXpNLIPafUSwMWGjW0r2nNax/yO3MVspJgGUwkTVvlg1',
    'SSRT': 'Ho47ZgABAA',
    '_abck': '2C823ECDD02F1992D955D4B7E1E56B03~-1~YAAQCjdlX9nlu1CPAQAAGyijWAsf3IBlDxgcitgfQndnmvBdUZ9x1quS3BnqWssdOqq9i+zO8ZyrCID06Xv1Cd+Qvjk1YOrE2p5eEreDfatDvPEslwuDLdqoFw57ltaIxooQWWmETyZ8axi5wK8MX8sNqgQmLwldbOU1XeBbQ3AXx1HlLgOjxwb6mWcMx+gXIoQjZiQld/GUcAm9asXedWAZhSqeqsYZXLkLJqZ8wbbKEim1fvgtMsU7XK3xhAX+y2e9rEZ7Iv4fI2r1Q3jOLphHTx0HoG0PKuahwg/lov8fL/NfHgt0VqJr+KTOpUeI7gcHsYESbclPwU+DhAtidXkUmRBnqhbGOVwfy8srgSbJsirvOTFwj7VbN0EUzlz86xd74dcqDFRL~-1~-1~-1',
    'SSPV': 'OaUAAAAAAAwAAQEAAAAAAAAAABQAAAAAAAAAAAAA',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'SSLB=1; SSID=CQD5OB1-AAQAAAAQBPdly4xAARAE92UMAAAAAAAAAAAAcoI7ZgBUmnYLAAED2AAAcoI7ZgEAXAsAAcnXAABygjtmAQCACwABSdgAAHKCO2YBAGcLAAEZ1wAAcoI7ZgEAjQsAAdjYAABygjtmAQCICwABetgAAHKCO2YBAGMLAAHd1gAAcoI7ZgEAYgsAAdnWAABygjtmAQDiCgABedIAAHKCO2YBAFsLAAA; SSSC=4.G7347345783865248971.12|2786.53881:2908.55241:2914.55001:2915.55005:2919.55065:2934.55299:2944.55369:2952.55418:2957.55512; i18next=nl-nl; _csrf=W-l28hsjPQ8yZ-PX03ixy8t_; Ahonlnl-Prd-01-DigitalDev-F1=!lbEyWpfvfI7laVzZn/IR7WT7ZKUq0y5bafQ2xxJiz08+iyJpi4F8cRetj3EymUYPwkX6UzNoOo6lJeI=; Ahonlnl-Prd-01-DigitalDev-B2=!Fr5YKutOFTP9Cr5ZQI6MIhlj9SYhsX2thWfrwWpH2102BBSHeuesLOCHplA+FMzDDhp0XZR7PKHt; bm_sz=B7001A790159E5D1A2631503F1EBDCEE~YAAQHjdlX2O+N1iPAQAAopZ1WBd8eJk0p62LO65zXA47u/j/HlOZYa203LV6mWkcZ21yAY42jVO5L3P4/bsEvGlocoIj/XTII/AjMK1g0NSaNqcRRDUznWYOWvBFaYkZEmUq2a9u8JxzevHBxaKzq7z51pF9xGrGCy2N9f4NfM1vbB2v3C6w2CMCmdEOZswJ5XDYOQ79GM1Yfklf8rtin6eMD9+Ip3CW9SQM+MhMUAFWADEL1x/PpsfGBU7iDL0GtNZlIpx++Lhb781RMmg4k8ydgqUzEUDR0jcKSYelR0Qf92cklnqJ09jil+NW28JIrn3LOcAqPkoFSkuIzFRXQE1lSB5O/KskPErDJYSpB5O3RpgTgg==~4272950~3162681; SSOD=ANVpAAAAJADqkwAAEAAAABIE92XfgjtmAwC_egAAAQAAAGJdIWZiXSFmAAAAAA; bm_mi=CBA638C2A445E543850662B6046DDF91~YAAQFDdlX0wVSVaPAQAAREp4WBfgttrLX/Hf3zYZoyIYALdifWC/QuzB3QwJpQDVYJp3HgyhmTO+ezqjOWoLyGZNVExuAcqFo4iUmqjcywNHrM5fSh+fcoS5MXsGSnLTUpLCpwgz2uwuQQhwCRM1exLh/IfEbdhSPVY/X+SRfCYTW2y1tWa6NI3eWPyftpvCA4fM53G+vVf3kWuPleeQFC4tlHAVjuJgHkYpmkzAmPJcwWZf8H7wX48hjW4U1KP/aBpMJjdQFkYr8ecYg+5iJrLXQC6r+uWQmWneBNilvnypwFHjmU56by7NAXt480PPZEGxXB0c~1; bm_sv=FC4888A53707ED31DD0A1746840AFFB9~YAAQFDdlX9cXSVaPAQAA/4d4WBfn55+QBGnJcEAwC5LMKIiMOETgLRfDK+60ZGGB8bg9u1SoZv3nX8SV4v3US9msK5kvPgcSgsAcaIlC6GSI4c1yBKpk+NUzv57xVcZTvrM4tNKu2wRkBBN5Ug5Lo55tb4e+3VG3QMs1P2gmuP9kCndmDoJr5aKtrAuKudSSstd6uQb6smr7L1gf1gHUPvMDVEHrja5n/TTw5V/g7R0DecY/xhVhyRsEH6dM/V/i~1; ak_bmsc=7581AFFABD687891C2C794BA6DA12966~000000000000000000000000000000~YAAQMTdlX0W9IE+PAQAAQ19/WBdh0jqB5wkfLyshTCVul29gD+xUS00wvZpcAdEJp5neoydslsqCR+l1yRmfyjJJqdDuOXs5s0OA100nZcAoMxfYxSunRnLXpWCsgT/I2lKR3lE7Nu5hZ/tk6Hqz+XAUgTdyYTsnAGDsm7+ypnQJ3VWYfc6DyaoK1Lv6+PEVIrebLxqyFpsbS/omLTI0vPcXqZGC2gjKS0EU+L3RK+plml/jDQ9/v5Cn7f9gZRWeqVePy9WfA8R/mPiYPK1uR533cIgfGB9wN0Vk5Fx9ZcdchuADPOlJGhocPUyNfCRWCSHS8D3y7o0Z5CuPA3sUI5xC0jHTw0yCL+BXTYXqpW6XJzqTg6giZ18ELeG6DloiIWpIozQ0dXpNLIPafUSwMWGjW0r2nNax/yO3MVspJgGUwkTVvlg1; SSRT=Ho47ZgABAA; _abck=2C823ECDD02F1992D955D4B7E1E56B03~-1~YAAQCjdlX9nlu1CPAQAAGyijWAsf3IBlDxgcitgfQndnmvBdUZ9x1quS3BnqWssdOqq9i+zO8ZyrCID06Xv1Cd+Qvjk1YOrE2p5eEreDfatDvPEslwuDLdqoFw57ltaIxooQWWmETyZ8axi5wK8MX8sNqgQmLwldbOU1XeBbQ3AXx1HlLgOjxwb6mWcMx+gXIoQjZiQld/GUcAm9asXedWAZhSqeqsYZXLkLJqZ8wbbKEim1fvgtMsU7XK3xhAX+y2e9rEZ7Iv4fI2r1Q3jOLphHTx0HoG0PKuahwg/lov8fL/NfHgt0VqJr+KTOpUeI7gcHsYESbclPwU+DhAtidXkUmRBnqhbGOVwfy8srgSbJsirvOTFwj7VbN0EUzlz86xd74dcqDFRL~-1~-1~-1; SSPV=OaUAAAAAAAwAAQEAAAAAAAAAABQAAAAAAAAAAAAA',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.ah.nl/bonus',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

response = requests.get('https://www.ah.nl/producten/wijn-en-bubbels?page=25', cookies=cookies, headers=headers)
# response = requests.get('https://www.ah.nl/producten/wijn-en-bubbels', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

class_name = "product-card-portrait_root__ZiRpZ product-grid-lane_gridItems__BBa4h"
class_name2 = "product-info-definition-list_value__1RuJf"
class_name3 = "price_unitSize__Hk6E4"

url = "https://www.ah.nl/"

products = soup.find_all("article", class_=class_name)

dataframe = pd.DataFrame(columns=["product_name", "alcohol_percentage"])

print(len(products))

for product in products:
    info = product.find('a', href = True)
    prod_url = url + info.attrs.get("href")

    product_name = prod_url.split("/")[-1]

    # find volume
    volume = product.find("span", class_=class_name3)
    print(volume.text)



    if volume.text == "0,75 l":
        request = requests.get(prod_url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(request.text, 'html.parser')

        # find alcohol percentage
        alcohol_found = soup.find("dd", class_=class_name2)
        if alcohol_found:
            print(prod_url, alcohol_found.text)

            try:
                #convert alcohol percentage to float
                alcohol_found = alcohol_found.text.replace("%", "")
                alcohol_found = float(alcohol_found.replace(",", "."))

                # put product name and alcohol percentage in a dataframe
                dataframe = dataframe._append({"product_name": product_name, "alcohol_percentage": alcohol_found}, ignore_index=True)
            except:
                pass
    time.sleep(1)


# sort dataframe by alcohol percentage from low to high
dataframe = dataframe.sort_values(by="alcohol_percentage")

# save dataframe to csv
dataframe.to_csv("wines.csv", index=False)
