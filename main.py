#source: https://stackoverflow.com/questions/5661725/format-ints-into-string-of-hex
def prettyhex(nums, sep=''):
    return sep.join(f'{a:02x}' for a in nums)

# input
inputString = input()
  
# output
print("inputString=" + inputString)
# source: https://stackoverflow.com/questions/28337748/how-to-extract-integers-from-a-string-separated-by-spaces-in-python-2-7
myIntegers = [int(x) for x in inputString.split()]
print(prettyhex(myIntegers,' '))