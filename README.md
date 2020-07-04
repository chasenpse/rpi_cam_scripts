# rPi cam scripts info

`capture.py` - captures raspistill photo to `~/Pictures`

`timelapse.py` - captures a raspistill timelapse to `~/Pictures/Timelapses`

To stream over RTSP use either the `stream.sh` or `novfhfstream.sh` script, which runs:

``` bash
#stream.sh
raspivid -o - -t 0 -n -vf -hf | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

#novfhfstream.sh
raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
```

If you encounter a permissions denied error make sure the scripts are executable by running `sudo chmod +x stream.sh novfhfstream.sh`