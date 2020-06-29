youtube-dl --format mp4 --output test.mp4 https://www.youtube.com/watch?v=I1188GO4p1E
ffmpeg -i test.mp4 -b:v 200K -b:a 64K -y full_resolution.mp4 >/dev/null 2>&1
du -b full_resolution.mp4
ffprobe full_resolution.mp4 2>&1 | grep "#0:0"
ffmpeg -i test.mp4 -vf scale=300:-2 -y scaled.mp4 >/dev/null 2>&1
du -b scaled.mp4
ffprobe scaled.mp4 2>&1 | grep "#0:0"
