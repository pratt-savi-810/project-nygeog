# Step 1 - Get the data and unzip the data
### https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip
### https://project.wnyc.org/transit-time/data/transit-time-json-files.zip

import urllib 
import zipfile

url = 'https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip'
your_zip_path = 'data/input/nyc_hexes_2000ft_4326.zip'

urllib.urlretrieve(url, your_zip_path)

zip = zipfile.ZipFile(your_zip_path, 'r')
zip.extractall('data/input/')

url = 'https://project.wnyc.org/transit-time/data/transit-time-json-files.zip'
your_zip_path = "data/input/transit-time-json-files.zip"

urllib.urlretrieve(url, your_zip_path)

zip = zipfile.ZipFile(your_zip_path, 'r')
zip.extractall('data/input/')