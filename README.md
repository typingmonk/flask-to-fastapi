# flask-to-fastapi
For interview test

Step-by-step walkthrough
## Build
1. Clone the repo
```
git clone https://github.com/typingmonk/flask-to-fastapi.git
```
2. Build from docker-compose.yaml and run it in background.
```
cd flask-to-fastapi/
docker compose up -d
```
3. Go to `http://[ip-address]:8080/docs` and you should be able to see the FastAPI website.
![demo](https://user-images.githubusercontent.com/11416512/197660393-c2ccc775-35ba-407e-a76c-24595ab86bfc.png)

## Walkthrough

Endpoints

Original flask endpoint:
```
/flask/example/endpoint1
```
