from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql import func
from database import Base


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    customer_id = Column(String, nullable=False)
    purchase_time = Column(DateTime(timezone=True), server_default=func.now())

class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    product_id = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
