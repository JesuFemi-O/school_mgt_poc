# school_mgt_poc

## How to run

- build image

```
 docker build -t username/app_name .
```

- run image

```
docker run -p 8000:8000 --name container_name username/app_name
```

- open http://127.0.0.1:8000/ on your browser
