from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI") #using noSQL database-> mongodb for flexibility
DATABASE_NAME = os.getenv("DATABASE_NAME")

async def connect_to_mongodb():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    return db

async def close_mongodb_connection(db):
    db.client.close()
# mongo_client = AsyncIOMotorClient(MONGO_URI)
# database = mongo_client[DATABASE_NAME]
    

#     import firebase_admin
# from firebase_admin import credentials, db
# from schema.orders import OrderCreate

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred)
# ref = db.reference()

# # Function to create an order in the Firebase database
# def create_order(order_data: OrderCreate):
#     # Convert Pydantic model to dictionary
#     order_dict = order_data.dict()
    
#     # Write order data to Firebase
#     ref.child('orders').push(order_dict)
#     print("Order created successfully")

# # Example usage
# if __name__ == "__main__":
#     # Create a sample order
#     sample_order = OrderCreate(orderSellerId=1, orderProductId=2, orderCustomerId=3, orderTimestamp=123456789)
    
#     # Call the function to create the order in Firebase
#     create_order(sample_order)
