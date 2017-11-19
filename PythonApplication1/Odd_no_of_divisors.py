# main function for all three functions
#from GetDivisor.natural import printDivisors =>  does not work as it is not a package 


from GetDivisor import square_root_unsorted as sqno   # once this is done only can use sqno NOT square_root_unsorted
from GetDivisor import natural as no

print ("The divisors of 100 are: ")

print("\n\n With O(n)") 
no.printDivisors(100)

print("\n\n With O(sqtr(n)) but unsorted") 
sqno.printDivisors(100)

print("\n\n With O(sqtr(n)) and sorted") 
no.printDivisors(100)
print("\n")

