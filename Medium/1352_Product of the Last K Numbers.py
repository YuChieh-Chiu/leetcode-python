class ProductOfNumbers:

    def __init__(self):
        """
        Thought:
        - The goal of this problem is to design an algorithm that sequentially receives a series of integers 
          and allows querying the product of the last k integers.
            - According to the problem statement, k is guaranteed to be within a valid range, 
              meaning there won't be an index out of bounds error.
        - Key idea: Initialize two variables:
            - self.product: Tracks the cumulative nonzero product. If a received number is 0, 
              reset self.product to 1 to prevent all subsequent products from being 0.
            - self.prefixProduct: Stores the cumulative product from the first number up to the i-th number.
        """
        self.product = 1
        self.prefixProduct = []

    def add(self, num: int) -> None:
        """
        Thought:
        - Goal: Store the cumulative nonzero product as numbers are added.
        - Key points:
            - If num is 0, any product that includes this value will be 0. 
              Therefore, we can reset self.prefixProduct and self.product to their initial states.
            - If num is nonzero, update self.product by multiplying it with num, 
              and store the result in self.prefixProduct.
        """
        if num == 0:
            self.product = 1
            self.prefixProduct = []
        else:
            self.product *= num
            self.prefixProduct.append(self.product)

    def getProduct(self, k: int) -> int:
        """
        Thought:
        - Important: Since we reset self.prefixProduct in add() when encountering 0, 
          k might be larger than the current length of self.prefixProduct.
        - Key points:
            - If k is greater than the length of self.prefixProduct, 
              it means the product includes a 0, so the result must be 0.
            - If k equals the length of self.prefixProduct, 
              the result is simply the last stored product, self.prefixProduct[-1].
            - If k is less than the length of self.prefixProduct, 
              the result is obtained by dividing the most recent product 
              by the product before the last k elements: self.prefixProduct[-1] // self.prefixProduct[-1-k].
        """
        if len(self.prefixProduct) < k:
            return 0
        elif len(self.prefixProduct) == k:
            return self.prefixProduct[-1]
        else:
            return self.prefixProduct[-1] // self.prefixProduct[-1-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
