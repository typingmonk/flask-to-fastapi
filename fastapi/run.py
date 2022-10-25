from app import app
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn
from sqlalchemy.orm import Session
from database import get_db
from models import Order, OrderItem
from schemas import AddOrderModel, ModifyOrderModel

# initial FastAPI
fastapi_app = FastAPI()

fastapi_app.mount("/flask", WSGIMiddleware(app))

@fastapi_app.get("/fastapi")
def read_main():
    return {"message": "Hi this is fastapi."}

@fastapi_app.post("/order/add")
def addOrder(payload: AddOrderModel, db: Session = Depends(get_db)):
    order_payload = Order(
        customer_name=payload.order.customer_name,
        customer_id=payload.order.customer_id
    )
    db.add(order_payload)
    db.commit()
    order_id = order_payload.order_id
    order_item_ids = []
    for item in payload.order_items:
        order_item_payload = OrderItem(
            order_id=order_id,
            product_name=item.product_name,
            amount=item.amount,
            product_id=item.product_id,
            price=item.price
        )
        db.add(order_item_payload)
        db.commit()
        order_item_ids.append(order_item_payload.id)
    return {"order_id": order_id, "order_item_ids": order_item_ids}

@fastapi_app.post("/order/modify")
def modifyOrder(payload: ModifyOrderModel, db: Session = Depends(get_db)):
    order = payload.order
    order_in_db = db.query(Order).filter(Order.order_id == order.order_id).first()
    order_in_db.customer_name = order.customer_name
    db.commit()
    
    if payload.order_items is not None:    
        for item in payload.order_items:
            item_in_db = db.query(OrderItem).filter(OrderItem.id == item.id).first()
            item_in_db.amount = item.amount
            item_in_db.price = item.price
            db.commit()
    return {"response": "success"}

@fastapi_app.get("/orders/all")
def getAllOrders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@fastapi_app.get("/order_items/all")
def getAllOrderItems(db: Session = Depends(get_db)):
    return db.query(OrderItem).all()

if __name__ == '__main__':
    uvicorn.run(fastapi_app)

