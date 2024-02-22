import pytest
import os
from task6 import Downloader

@pytest.fixture
def downloader():
    return Downloader('../task_4/links.parquet')  

def test_download_first_image(downloader):
    path = downloader[0]
    assert os.path.exists(path)

def test_download_multiple_images(downloader):
    paths = downloader[0:3]  # Download first 3 images
    assert len(paths) == 3
    for path in paths:
        if isinstance(path, str) and not path.startswith('An error occurred'):  # Check if path is a string and not an error message
            assert os.path.exists(path)


if __name__ == "__main__":
    pytest.main([__file__])
