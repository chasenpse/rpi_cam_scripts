#!/bin/bash
raspivid -o - -t 0 -n -w 1280 -h 720 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
