# skopje_realestate

Python script that scrapes datafrom https://www.pazar3.mk, specifically for apartments for sale in Skopje and their associated location (municipality) and price. The data is cleaned up so that only ads with all the necessary information are included in the analysis. The average price per square meter per municipality is then visualized in/with Datawrapper.

Note 1: Please make sure to insert your **Datawrapper API token** in the **make_datawrapper_map.py** file.
Note 2: In the **get_oglasi_func.py**, the number of pages to scrape is set on 1 by default. This can be modified manually.

*Upcoming versions will connect to a database, enable automatic scheduled scraping and improve data accuracy.*
