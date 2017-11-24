# main function for all three functions
#from GetDivisor.natural import printDivisors =>  does not work as it is not a package 
import timeit

from GetDivisor import square_root_unsorted as sqno   # once this is done only can use sqno NOT square_root_unsorted
from GetDivisor import natural as no
from GetDivisor import square_root_sorted as sqno_S

print ("The divisors of 100 are: ")

print("\n\n With O(n)") 
no.printDivisors(182)

print("\n\n With O(sqtr(n)) but unsorted") 
sqno.printDivisors(182)

print("\n\n With O(sqtr(n)) time complexity and O(sqrt(n)) for space and sorted") 
sqno_S.printDivisors(182)

print("\n")

###ALways remove printf functions when you want to test the time...
#SETUP_CODE = '''
#from GetDivisor import natural as no
#'''
#TEST_CODE ='''    
#no.printDivisors(100)
#'''
#print("\n")
#times = timeit.repeat( stmt = TEST_CODE, setup = SETUP_CODE, repeat = 3, number = 10)
#print('Naturally executing the divisors {}'.format(min(times)))
