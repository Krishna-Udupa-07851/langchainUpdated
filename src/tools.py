from langchain.tools import tool

ORDERS = {"A17": "shipped on 3 March", "C40": "waiting for stock"}


@tool("order_status", description="order's shipping status by its id, such as A17.")
def lookup_order(order_id: str, customer: str) -> str:
    # """Look up an order's shipping status by its id, such as A17."""
    status = ORDERS.get(order_id)
    return f"{order_id} {status}." if status else f"{order_id} is not an order we have."

print(lookup_order.name)
print(lookup_order.description)
print(lookup_order.args)