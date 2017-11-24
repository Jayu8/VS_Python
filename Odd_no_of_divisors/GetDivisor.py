import math 

# Calculates the divisor by checking remainder using all natural numbers upto that number (mod)
# 1 number -> 2 divisors  (divisor1,divisor2) => pair 
# calculate the least number by mod with divisor1 and then get other, divisor2 = num/divisor1

# *************** Write test cases, BETTER ON NOTEBOOK ON GITHUB , FOLLOW STEPS BY CTCI ********************

 
#class square_root_sorted(object):
#    """loop upto square root of number and sort"""
#    def printdivisors(n):

class square_root_unsorted(object):
    """Loop upto square of the number """
    def printDivisors(n) :
        # Note that this loop runs till square root
        i = 1
        sq_no = int(math.sqrt(n))   
        for i in range(1,sq_no):                       # try to keep loop simple as posible #WHY??Error was sqrt(n) was float hence replaced with new variable
            if ( n % i ==0):                            
                                                       # If divisors are equal, print only one
                if( (n/i) ==  i ):
                    print (" {} ".format(i), end="")
                else:
                                                       # Otherwise print both (i,n/i)
                    print(" {} {} ".format(i, int(n/i)),end ="")
                           
class natural(object):
    """Loop upto the actual number"""
    def printDivisors(n):
        for i in range(1,n):
            if(n % i  == 0):
                print (" {} ".format(i),end="")
