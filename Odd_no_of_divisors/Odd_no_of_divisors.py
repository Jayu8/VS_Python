# main function for all three functions
#from GetDivisor.natural import printDivisors =>  does not work as it is not a package 
import timeit

from GetDivisor import square_root_unsorted as sqno   # once this is done only can use sqno NOT square_root_unsorted
from GetDivisor import natural as no
from GetDivisor import square_root_sorted as sqno_S

print ("Enter the dividend to find the divisors: ")
dividend = int(input().strip())

print("\n\n Unsorted With O(n) for time and O(1) for space") 
no.printDivisors(dividend)

print("\n\n Unsorted With O(sqtr(n)) and O(1) for space ") 
sqno.printDivisors(dividend)

print("\n\n Sorted With O(sqtr(n)) time complexity and O(sqrt(n)) for space") 
sqno_S.printDivisors(dividend)

print("\n")

###ALways remove print function within Getdivisor.py file when you want to test the time...

#SETUP_CODE = '''
#from GetDivisor import natural as no
#'''

#TEST_CODE ='''    
#no.printDivisors(100)
#'''

#print("\n")
#times = timeit.repeat( stmt = TEST_CODE, setup = SETUP_CODE, repeat = 3, number = 10)
#print('Naturally executing the divisors {}'.format(min(times)))
