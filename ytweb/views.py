import os
from urllib import request
from django.shortcuts import render
import pytube
from pytube import YouTube
import pathlib
# Create your views here.
def ytdown(request):
    # SAVE_PATH ="E:/"
    c=''
    try:
        if request.method=='POST':
            link=(request.POST.get('links'))
            yt =pytube.YouTube(link)
            yt=yt.streams.get_highest_resolution()
            yt.download(pathlib.Path.home()/"Downloads")
            c='Succesfully Downloaded'
    except:
        c='Invalid link'
    return render(request,'yt.html',{'c':c})
pathlib.Path.home()/"Downloads"
