class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        results = []
        products.sort()

        for i, c in enumerate(searchWord):
            products = list(
                filter(lambda p: p[i] == c if len(p) > i else False, products)
            )
            results.append(products[:3])

        return results
