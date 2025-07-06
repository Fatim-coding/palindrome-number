numberLargest = int(input("Enter the largest number:"))
numbersmallest = int(input("Enter the smallest number:"))
while numbersmallest:
    numberstore= numbersmallest
    numbersmallest = numberLargest % numbersmallest
    numberLargest = numberstore

print("HCF is :", numberLargest)


