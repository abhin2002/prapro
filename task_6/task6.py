import os
import urllib.request
import pandas as pd
import urllib.error
from concurrent.futures import ThreadPoolExecutor
import time

class Downloader:
    def __init__(self, pq_file: str, max_workers=5):
        self.df = pd.read_parquet(pq_file, columns=["URL"])
        self.base_path = './downloads/'
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def download_image(self, url: str, local_path: str) -> str:
        try:
            urllib.request.urlretrieve(url, local_path)
        except Exception as e:
            return f"An error occurred while downloading the image: {e}"
        return local_path

    def __getitem__(self, key):
        if isinstance(key, int):
            url = self.df.iloc[key]['URL']
            file_ext = os.path.splitext(url)[1]
            if file_ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif']:
                file_ext = '.jpg'
            local_path = self.base_path + f'image_{key}{file_ext}'
            future = self.executor.submit(self.download_image, url, local_path)
            return future
        elif isinstance(key, slice):
            start, stop, step = key.indices(len(self.df))
            futures = []
            for i in range(start, stop, step):
                url = self.df.iloc[i]['URL']
                file_ext = os.path.splitext(url)[1]
                if file_ext.lower() not in ['.jpg', 'jpeg', '.png', '.gif']:
                    file_ext = '.jpg'
                local_path = self.base_path + f'image_{i}{file_ext}'
                future = self.executor.submit(self.download_image, url, local_path)
                futures.append(future)
            return futures

start_time = time.time()

d = Downloader('../task_4/links.parquet')

# Download the first image
path = d[0]
print(f'Downloaded image path: {path}')

# Download the first 10 images
paths = d[0:10]
print(f'Downloaded image paths: {paths}')

end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")