from pathlib import Path
import pandas as pd
import youtube_dl
import sys
import os

if len(sys.argv) != 3:
    sys.exit(1)

module = "module-{}".format(sys.argv[1])
BASE_OUTPUT_PATH = Path(sys.argv[2])

ASSETS_PATH = Path().joinpath("./assets/")
OUTPUT_PATH = BASE_OUTPUT_PATH.joinpath(module)
os.makedirs(OUTPUT_PATH, exist_ok=True)


def get_urls(module):
    df_url = pd.read_csv(Path(ASSETS_PATH).joinpath("{}.csv".format(module)), sep=";", header=None)
    df_url[0] = df_url[0] + ".mp4"

    return df_url[0], df_url[1]


if __name__ == '__main__':
    filename, url = get_urls(module)

    for filename, url in zip(filename, url):
        ydl_opts = {
           'outtmpl': str(Path(OUTPUT_PATH).joinpath(filename)),
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
