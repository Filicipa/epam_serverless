import boto3
import os

ORDERS_TABLE = os.environ["ORDERS_TABLE"]

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(ORDERS_TABLE)

def lambda_handler(event, context):
    order_id = event["orderId"]

    table.update_item(
        Key={"orderId": order_id},
        UpdateExpression="SET #s = :s",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":s": "STOCK_RESERVED"}
    )

    return {
        "orderId": order_id,
        "status": "STOCK_RESERVED",
        "verification": event.get("verification")
    }