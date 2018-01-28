import math 
# Calculates the divisor by checking remainder using all natural numbers upto that number (mod)
# 1 number -> 2 divisors  (divisor1,divisor2) => pair 
# calculate the least number by mod with divisor1 and then get other, divisor2 = num/divisor1
# *************** Write test cases, BETTER ON NOTEBOOK ON GITHUB , FOLLOW STEPS BY CTCI ********************
class square_root_sorted(object):
    """loop upto square root of number and sort"""
    def printDivisors(n) :                          # sqrt+1 WRONG => because first 4x5 then followed by 5x4  because of '+1' term
        v = []
        sq_no = int(math.sqrt(n))                   # *** dont add + 1 here , else some divisors repeat
        for i in range(1,sq_no+1):                   # try to keep loop simple as posible #WHY??Error was sqrt(n) was float hence replaced with new variable
            if ( n % i ==0):                         # If divisors are equal, print only one
                if( (n/i) ==  i ):
                    print (" {} ".format(i), end="")
                else:                                    
                    print(" {}".format(i),end ="")    # Print the small divisor 
                    v.append(int(n/i))                # Push big divisor into array , Note this will be in reverse order
        for num in reversed(v):                       #reversing a string
            print (" {}".format(num), end="")
            #print("{}".format(v[::-1]))              # Print the big divisors in sorted order
class square_root_unsorted(object):
    """Loop upto square of the number """
    def printDivisors(n) :
        sq_no = int(math.sqrt(n))                      # Note that this loop runs till square root
        for i in range(1,sq_no+1):                     # try to keep loop simple as posible WHY??Error was sqrt(n) was float hence replaced with new variable
            if ( n % i ==0):                           # If divisors are equal, print only one
                if( (n/i) ==  i ):
                    print (" {} ".format(i), end="")
                else:                                    
                    print(" {} {} ".format(i, int(n/i)),end ="") # Otherwise print both (i,n/i)
class natural(object):
    """Loop upto the actual number"""
    def printDivisors(n):
        for i in range(1,n+1):                          # ******** Remember to add +1 in python range **************
            if(n % i  == 0):
                print (" {}".format(i),end="")
#end