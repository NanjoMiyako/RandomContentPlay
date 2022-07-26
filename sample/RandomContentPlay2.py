#!/usr/bin/env python
#-*- cording: utf-8 -*-
import time
import cv2
import sys
import random
import math

#VideoCaptureオブジェクトを取得
cap = cv2.VideoCapture(r"C:\Users\hogehoge\再生する動画のURL.mp4")

video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
video_fps = cap.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
video_len_sec = video_frame_count / video_fps         # 長さ（秒）を計算する
video_len_sec = math.floor(video_len_sec)

#動画の長さ(分)
movie_len = 60
#一再生時間(分)
movie_playTime = 1
movie_playTimeSecond = movie_playTime * 60

start = random.randint(0, video_len_sec-movie_playTimeSecond)

#fps取得
fps = cap.get(cv2.CAP_PROP_FPS)
#動画の開始位置を設定
cap.set(cv2.CAP_PROP_POS_FRAMES, int(start*fps))

time_start = time.time()

#動画の表示
while (cap.isOpened()):

    time_end = time.time()
    time_passedSec = time_end - time_start

    if time_passedSec >= movie_playTimeSecond:
        start = random.randint(0, video_len_sec-movie_playTimeSecond)
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(start*fps))
        time_start = time.time()
    
    #フレーム画像の取得
    ret, frame = cap.read()

    frame = cv2.resize(frame, dsize=(320, 320))
    
    #画像の表示
    cv2.imshow("Image", frame)
    #キー入力で終了
    if cv2.waitKey(10) != -1:
        break

cap.release()
cv2.destroyAllWindows()