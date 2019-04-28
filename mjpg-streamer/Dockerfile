FROM alpine AS downloader
RUN apk add --no-cache subversion
RUN svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer mjpg-streamer

FROM ubuntu:18.04
RUN apt-get update && apt-get install -y libjpeg-dev imagemagick gcc g++ make
COPY --from=downloader mjpg-streamer ./mjpg-streamer
COPY start.sh ./
RUN cd mjpg-streamer && make && make install
CMD ./start.sh

# docker run -it --rm -p 8080:8080 -v /dev:/mnt --privileged test
# start.shの詳細は、https://github.com/jacksonliam/mjpg-streamer/tree/master/mjpg-streamer-experimental
# まじかよhttps://walking-succession-falls.com/%E3%83%A9%E3%82%BA%E3%83%91%E3%82%A43-%E3%82%AB%E3%83%A1%E3%83%A9%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC%E3%83%AB-mjpg-streamer%E3%81%A7%E3%82%B9%E3%83%88%E3%83%AA%E3%83%BC%E3%83%9F%E3%83%B3%E3%82%B0/