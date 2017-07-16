# Colorful Number:
# https://www.interviewbit.com/problems/colorful-number/

def _substr_product(num_str):
    result = 1
    for dig_str in num_str:
        result *= int(dig_str)
    return result


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        products = set()
        A_str = str(A)
        
        for i in xrange(len(A_str)):
            for j in xrange(i+1, len(A_str)+1):
                product = _substr_product(A_str[i:j])
                if product in products:
                    return 0
                products.add(product)
        
        return 1
