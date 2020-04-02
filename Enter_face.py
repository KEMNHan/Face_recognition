import argparse
import logging
import sys
import time
from typing import Dict, Generator
import cv2 as cv
import numpy as np
import yaml
from arcface import ArcFace, timer
from arcface import FaceInfo as ArcFaceInfo
from module.face_process import FaceProcess, FaceInfo
from module.image_source import LocalImage, ImageSource, LocalCamera
from module.text_renderer import put_text

def enter_face(filename,feature_data,ID):
    with open("profile.yml", "r", encoding="utf-8") as file:
        profile: Dict[str, str] = yaml.load(file, yaml.Loader)
        ArcFace.APP_ID = profile["app-id"].encode()
        ArcFace.SDK_KEY = profile["sdk-key"].encode()
    face_process = FaceProcess()
    res = face_process.add_person(filename,feature_data)
    print(res)
    if res != 1:
        print("照片不符合要求")
    else:
        print("添加成功")
def main():
    filename = r"G:\fa\55.png"
    feature_data = r"G:\fa\feature.txt"
    ID = "55"
    enter_face(filename, feature_data,ID)

if __name__ == "__main__":
    main()