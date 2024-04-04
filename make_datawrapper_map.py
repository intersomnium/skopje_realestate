from datawrapper import Datawrapper
from constants import metadata_fixed
def make_map(mean_PPP_df):
    ACCESS_TOKEN = "{insert your Datawrapper API token here}"
    dw = Datawrapper(access_token=ACCESS_TOKEN)
    map_test = dw.create_chart(title = 'Realestate Market Research', chart_type='d3-maps-choropleth', data=mean_PPP_df, metadata=metadata_fixed)
    map_id = map_test['id']
    published_response = dw.publish_chart(map_id)
    map_url = published_response['data']['publicUrl']
    dw.display_chart(map_id)
    return map_url