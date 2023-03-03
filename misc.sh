docker run -d -p 8000:5000 --env-file env.list --name compression dev.local/311.compression:1.0.0

docker run -d -p 8000:5000 --env-file env.list --name thumbnailer dev.local/210.thumbnailer:1.0.0

docker run -d -p 8000:5000 --env-file env.list --name video-processing dev.local/220.video-processing:1.0.0