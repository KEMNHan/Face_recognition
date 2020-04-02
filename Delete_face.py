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

def delete_face (ID, filename):
    with open("profile.yml", "r", encoding="utf-8") as file:
        profile: Dict[str, str] = yaml.load(file, yaml.Loader)
        ArcFace.APP_ID = profile["app-id"].encode()
        ArcFace.SDK_KEY = profile["sdk-key"].encode()
    face_process = FaceProcess()
    face_process.delete_person(ID, filename)

def main():
    ID = "55"
    filename = r"G:\fa\feature.txt"
    delete_face(ID, filename)

if __name__ == "__main__":
    main()