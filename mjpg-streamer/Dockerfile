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