"""
Creates a copy of the template in a target folder
"""
from enum import StrEnum, auto
from icecream import ic
import os
import PySimpleGUI as sg
from pytube import YouTube


class K(StrEnum):
    URL = auto()
    FOLDER = auto()
    PATHVIEW = auto()
    SUBMIT = "Submit"
    CANCEL = "Cancel"


def download_video(url: str) -> None:
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download()


def get_url_and_folder() -> dict[str, str]:
    layout = [
        [sg.T("YouTube URL: "), sg.In(key=K.URL.value)],
        [
            sg.T("Choose destination folder:"),
            sg.FolderBrowse(key=K.FOLDER.value),
        ],
        [
            sg.T(key=K.PATHVIEW.value),
        ],
        [sg.Submit(), sg.Cancel()],
    ]
    window = sg.Window(title="Set Project name and Folder", layout=layout)
    while True:
        event, values = window.read()
        if event in ["Cancel", sg.WIN_CLOSED]:
            break
        elif event == "FOLDER":
            window["PATH"].update(values[K.FOLDER.value])
        elif event == "Submit":
            break
        else:
            pass
    window.close()
    return values


def main():
    print("Collecting the URL and destination folder")
    user_input: dict[str, str] = get_url_and_folder()
    url = user_input[K.URL.value]
    target = user_input[K.FOLDER.value]
    os.chdir(target)
    print("Downloading video")
    download_video(url=url)
    print("Download complete!")


if __name__ == "__main__":
    main()
