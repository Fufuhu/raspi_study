#!/bin/sh

PORT="8080" #ポート番号
ID="hoge" #IDは好きなもの
PW="hoge" #パスワード
SIZE="640x480" #画面サイズ
FRAMERATE="20" #フレームレート
export LD_LIBRARY_PATH=/usr/local/lib
mjpg_streamer \
    -i "input_uvc.so -f $FRAMERATE -r $SIZE -d /mnt/video0 -y -n" \
    -o "output_http.so -w /usr/local/www -p $PORT -c $ID:$PW"