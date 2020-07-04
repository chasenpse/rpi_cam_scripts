#!/bin/bash
raspivid -o - -t 0 -n -vf -hf -w 1280 -h 720 -awb sun | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
