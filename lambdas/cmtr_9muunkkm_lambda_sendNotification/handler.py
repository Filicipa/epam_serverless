def lambda_handler(event, context):
    print(f"[MOCK] Notification sent for order {event['orderId']}")

    return {
        "message": "Notification sent",
        "orderId": event["orderId"],
        "verification": event.get("verification")
    }