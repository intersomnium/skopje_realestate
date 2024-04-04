from get_oglasi_func import *
from fill_missing_info import *
from processing_funcs import *
from make_datawrapper_map import *

oglasi = get_oglasi()
oglasi_filled = fill_na_oglasi(oglasi)
oglasi, removed_o = filter_oglasi(oglasi_filled)
rem_na,rem_flag,rem_skopje = sort_removed_oglasi(removed_o)
final_oglasi_list = sredi_prices(oglasi)
og_df = pd.DataFrame(oglasi)
mean_df = mean_PPP(og_df)
url_map = make_map(mean_df)
print(url_map)