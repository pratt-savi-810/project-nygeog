# Step 1 - Get the data
# https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip
# https://project.wnyc.org/transit-time/data/transit-time-json-files.zip

import urllib 

url = 'https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip'
your_zip_path = 'data/nyc_hexes_2000ft_4326.zip'

urllib.urlretrieve(url, your_zip_path)

url = 'https://project.wnyc.org/transit-time/data/transit-time-json-files.zip'
your_zip_path = "data/transit-time-json-files.zip"

urllib.urlretrieve(url, your_zip_path)