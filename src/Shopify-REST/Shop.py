

class Shop:
    def __init__(self, shop_name, shopify_access_token):
        self.token = shopify_access_token
        self.endpoint_base = f"https://{shop_name}.myshopify.com"

        self.headers = {
                "Content-Type" : "application/json",
                "X-Shopify-Access-Token": self.token
                }
    


