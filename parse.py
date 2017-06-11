#!/usr/bin/python
#########################################
#     for parsing text file             #
#########################################
from youtubeui import *
import os

def parse_vid(video_list):
    video_file = open("video_title.txt", "r")
    video_list = video_file.read().split("\n")
    video_file.close()
    return video_list
def parse_url(url_index):
    video_file = open("video_url.txt", "r")
    video_url = video_file.read().split("\n")
    video_file.close()

    return video_url[url_index]


