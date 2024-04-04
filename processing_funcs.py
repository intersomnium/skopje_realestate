from itertools import filterfalse
import pandas as pd

def filter_oglasi(oglasi_filled):
    removed_oglasi = []
    for oglas in oglasi_filled:
        if ('N/A' in oglas.values()) or ('!' in oglas.values()) or ('Skopje' in oglas.values()):
            removed_oglasi.append(oglas)
    oglasi_clean = list(filterfalse(removed_oglasi.__contains__, oglasi_filled))
    return oglasi_clean, removed_oglasi


def sort_removed_oglasi(removed_o):
    oglasi_na = []
    oglasi_flag = []
    oglasi_skopje = []
    for oglas in removed_o:
        if 'N/A' in oglas.values():
            oglasi_na.append(oglas)
        if '!' in oglas.values():
            oglasi_flag.append(oglas)
        if 'Скопје' in oglas.values():
            oglasi_skopje.append(oglas)
    return oglasi_na, oglasi_flag, oglasi_skopje


def sredi_prices(oglasi):
    for oglas in oglasi:
        if oglas['Price'] < 5000:
            #dodaj mozda proverka vo description da ne pishuva deka se iznajmuva slucajno
            oglas['PPP'] = oglas['Price']
            oglas['Price'] = oglas['PPP'] * oglas['Povrsina']
        else:
            #dodaj proverka da ne e ipak mozebi kukja iako ne bi trebalo
            oglas['PPP'] = round(oglas['Price']/oglas['Povrsina'])
    return oglasi


def mean_PPP(og_df):
    opstini = og_df.Location.unique()
    og_mean_dict = {}
    for item in opstini:
        og_mean_dict[f"{item}"] = round(og_df.query(f"Location == '{item}'")['PPP'].mean())

    mean_PPP_df = pd.DataFrame(og_mean_dict.items(), columns=['Opstina', 'PPP'])
    return mean_PPP_df
