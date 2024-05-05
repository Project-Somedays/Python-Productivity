import os
import subprocess
import PySimpleGUI as sg
import zipfile
import tarfile
from icecream import ic


def convert_png_to_mp4(png_folder: str, output_file: str, fps: int = 30) -> None:
    # Call ffmpeg to convert PNG files to MP4
    ffmpeg_command = [
        f"ffmpeg -y -r {str(fps)} -i {os.path.join(png_folder, r'%07d.png')} -c:v libx264 -profile high -crf 20 -pix_fmt yuv420p {output_file}"
    ]
    subprocess.run(ffmpeg_command, check=True)


def unzip_folder(zip_file: str, extract_to: str) -> None:
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(path=extract_to)


def unzip_tar(tar_file: str, extract_to: str) -> None:
    with tarfile.open(tar_file, "r") as tar:
        tar.extractall(path=extract_to)


def main():
    zip_file = sg.PopupGetFile(
        message="Point me to the zip file containing your images"
    )

    folder_one_level_up = os.path.dirname(zip_file)
    folder_name = os.path.splitext(os.path.basename(zip_file))[0]
    ic(folder_name)

    print("Making the png folder")
    png_folder = os.path.join(folder_one_level_up, folder_name)
    ic(png_folder)

    print("Unzipping the file")
    unzip_tar(tar_file=zip_file, extract_to=png_folder)
    # png_folder = sg.PopupGetFolder("Where are your images stored?")
    # ic(png_folder)

    target_path = sg.PopupGetFolder(message="Where should I put your mp4 file?")
    ic(target_path)

    target_filename = sg.PopupGetText("Name your file eg: Hawaiian Lei 1.mp4")

    if target_filename[-4:] != ".mp4":
        target_filename = target_filename + ".mp4"
    ic(target_filename)

    target_filepath = os.path.join(target_path, target_filename)
    ic(target_filepath)

    print("Converting to MP4")
    convert_png_to_mp4(png_folder=png_folder, output_file=target_filepath, fps=30)

    # print("Deleting the zip file")
    # os.remove(zip_file)

    # print("Deleting png folder")
    # os.remove(png_folder)


if __name__ == "__main__":
    main()
