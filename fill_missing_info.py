import requests
from bs4 import BeautifulSoup
import re
from translator import translate_func

def fill_na_oglasi(oglasi):
    for oglas in oglasi:
        falat_keys = [key for key, value in oglas.items() if value == 'N/A']
        if falat_keys:
            url = oglas['Link']
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            oks = soup.find_all('div', class_='tags-area')
            if oks:
                if 'Povrsina' in falat_keys:
                    if "Површина:" in oks[0].text:
                        for a in oks[0].find_all('a'):
                            if "Површина:" in a.text:
                                b_tag = a.find('bdi')
                                povrsina_unclean = b_tag.text.strip()
                                povrsina = re.findall(r'\d+', povrsina_unclean)[0]
                                oglas['Povrsina'] = int(povrsina) if int(povrsina) > 10 else 'N/A'

                if 'Location' in falat_keys:
                    lokacija = 'N/A'
                    if "Локација:" in oks[0].text:
                        for a in oks[0].find_all('a'):
                            if "Локација:" in a.text:
                                b_tag = a.find('bdi')
                                location_unclean = b_tag.text.strip()
                                location = re.findall(r'^([^,]+)', location_unclean)[0]
                                oglas['Location'] = translate_func(location)

                if 'Price' in falat_keys:
                    price = 'N/A'
                    body_soup = soup.find_all('div', class_='description-area')
                    tekst_to_filter = body_soup[0].find('span').text.strip()
                    price_pattern = r'(\d+[\s,.\d]*)\s*(evra|eur|EUR|Eur|€|evr|eura|euro|evro)'
                    # delot 're.I' vo findall go pravi patternot case INSENSITIVE
                    potential_price = re.findall(price_pattern, tekst_to_filter, re.I)

                    if potential_price:
                        if len(potential_price)== 1:
                            price_without_separators = potential_price[0][0].replace(" ", "").replace(",", "").replace(".", "")
                            price = int(price_without_separators)
                            oglas['Price'] = price
                        else:
                            # ! go kreiram kako flag za kontradiktorni informacii za price (ako najde povekje ceni)
                            oglas['Price'] = '!'
    return oglasi