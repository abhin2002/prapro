import os
import pyarrow.parquet as pq
import requests
from tqdm import tqdm
import pandas as pd


# Get the first 10,000 URLs
urls = pq.read_table("links.parquet", columns = ["URL"])["URL"][:10000].to_numpy() 

# Create a directory to store the images
os.makedirs('images', exist_ok=True)


# Define headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

for i, url in enumerate(tqdm(urls, desc='Downloading images')):
    try:
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()

        # Save the image to a file
        with open(f'images/image_{i}.jpg', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    except requests.exceptions.RequestException as e:
        print(f'Failed to download image {i} from URL: {url}')
        print(f'Error: {e}')

