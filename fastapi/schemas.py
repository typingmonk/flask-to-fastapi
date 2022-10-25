from typing import Optional, List, Dict
from pydantic import BaseModel


class CreateOrderItemModel(BaseModel):
    product_name: str
    amount: int
    product_id: str
    price: int

class CreateOrderModel(BaseModel):
    customer_name: str
    customer_id: str
    
class AddOrderModel(BaseModel):
    order: CreateOrderModel
    order_items: List[CreateOrderItemModel]

class UpdateOrderItemModel(BaseModel):
    id: int
    amount: Optional[int]
    price: Optional[int]

class UpdateOrderModel(BaseModel):
    order_id: int
    customer_name: Optional[str] = None

class ModifyOrderModel(BaseModel):
    order: UpdateOrderModel
    order_items: Optional[List[UpdateOrderItemModel]] = None

