# Step 2 - unzip the data
import zipfile

zip = zipfile.ZipFile(your_zip_path, 'r')
zip.extractall('data/')