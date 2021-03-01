# Simple-Youtube-Downloader

Simple youtube downloader made using [pytube](https://github.com/pytube/pytube) (Python)

## Requirement

- python
- pytube

First, you need to install python, you can install it from [python downloads](https://www.python.org/downloads/).

Then, you need to install pytube, Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pytube](https://github.com/pytube/pytube).

```bash
pip install pytube
```

## Usage
Change the SAVE_PATH in the Downloader class with the directory where you will save the download file
```python
class Downloader:
  def __init__(self):
    #enter download directory here
    self.SAVE_PATH = 'enter download directory here'
```
Enter the project directory then open 'downloader.py' using python, if you are using python3 then use the command:

```bash
python3 downloader.py #python3
#or
python downloader.py #python2

```
