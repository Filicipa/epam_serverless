import boto3
from datetime import datetime
import uuid
import os

ORDERS_TABLE = os.environ["ORDERS_TABLE"]

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(ORDERS_TABLE)

def lambda_handler(event, context):
    order_id = f"order-{uuid.uuid4()}"
    verification = event.get("verification")

    table.put_item(
        Item={
    "verification": "20260922081412",
            "orderId": order_id,
            "userId": "mock-user",
            "productId": "mock-product",
            "quantity": 1,
            "status": "CREATED",
            "createdAt": datetime.utcnow().isoformat()
        }
    )

    return {
        "orderId": order_id,
        "status": "CREATED",
        "verification": verification
    }