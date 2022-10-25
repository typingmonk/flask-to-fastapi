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

For FastAPI endpoints:
Simple get api return {"message": "Hi this is fastapi."}
```
/fastapi
```
POST api for adding new order(with order_items). You can try the json data in `/json/add_order.json`
```
/order/add
```
POST api for modify order and order_items. You can try the json data in `/json/modify_order.json`
```
/order/modify
```
GET api for getting all orders in database.
```
/orders/all
```
GET api for getting all order_items in database.
```
/order_items/all
```

## Database Table
The create commands are in `sql/create_tables.sql`
