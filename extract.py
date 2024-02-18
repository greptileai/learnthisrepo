# list every file in this directory
# and print the file name
import os
import re
import pandas as pd
slugs = []
urls = []
for root, dirs, files in os.walk("."):
    for filename in files:
        # if it's html, add it to the list
        if filename.endswith('.html'):
            slugs.append(filename)

            # read the file and extract the URL, it follows the chars "URL=".
            with open(filename, 'r') as f:
                for line in f:
                    if "URL=" in line:
                        url = line.split("URL=")[1]
                        # extract URL from this string using regex
                        url = re.findall(r'(https?://\S+)', url)
                        urls.append(url)


df = pd.DataFrame({'slug': slugs, 'url': urls})
df.to_csv('urls.csv', index=False)