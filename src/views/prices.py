class PricesView():
    def prices_list(self, prices):
        response = []
        for price in prices:
            response.append(
                {
                    "price": price[2],
                    "createdAt": price[3],
                }
            )
        return response
