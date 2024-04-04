import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import re
from constants import months

def get_oglasi():
    dict_list_ads = []
    page_counter = 1
    while page_counter < 2:
        # print(f"Page {page_counter}")
        url = f"https://www.pazar3.mk/oglasi/zivealista/stanovi/prodazba/skopje?Page={page_counter}"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        ad_divs = soup.find_all('div', class_='title span-col-title')

        for ad_div in ad_divs:
            date_span = ad_div.find('span', class_='pull-right ci-text-right')
            price_p = ad_div.find('p', class_='list-price')

            dates = date_span.text.strip() if date_span else 'N/A'
            price = int("".join(re.findall('\d', price_p.text.strip()))) if len(price_p.text.strip()) else 'N/A'
            if price != 'N/A' and price < 10:
                price = 'N/A'

            if "Денес" in dates:
                today = date.today()
                formatted_date = today.strftime('%d.%m')
            elif "Вчера" in dates:
                formatted_date = (date.today() - timedelta(days=1)).strftime(f"%d.%m")
            else:
                parts = dates.split()
                day = parts[0]
                month_name = parts[1]
                month_number = months.get(month_name)
                formatted_date = f"{day}.{month_number}"

            a_tag = ad_div.find('a', class_='Link_vis')
            href_link = a_tag.get('href') if a_tag else 'Link not found'

            povrsina = 'N/A'
            if "Површина:" in ad_div.text:
                for div in ad_div.find_all('div'):
                    if "Површина:" in div.text:
                        b_tag = div.find('b')
                        povrsina = int(b_tag.text) if int(b_tag.text) > 10 else 'N/A'

            ad_dict = {
                "Date": formatted_date,
                "Location": 'N/A',
                "Price": price,
                "Povrsina": povrsina,
                "Link": "https://www.pazar3.mk" + href_link
            }

            dict_list_ads.append(ad_dict) if ad_dict not in dict_list_ads else None

        page_counter = page_counter + 1
    return dict_list_ads
