#!/usr/bin/env python3

# Constraints:
#   len (arr) <= 9
#   1 <= arr[i] <= 9

arr = [7, 6, 4, 3, 2, 3]
print ('Orig array:  ', arr)

# init counter
count = [0 for _ in range (9)]
print ('Init counter:', count)

# count frequency
for n in arr:
    count[n] += 1 # +=1 to allow duplicates
    print ('Count val:   ', n, '->', count[n])
print ('Count:       ', count)

# count frequency accumulate
for i in range (9):
    count[i] += count[i - 1]
    print ('Accumulate:  ', i, '->', count[i])
print ('Accum:       ', count)

# init output array
outarr = [0 for _ in range (9)]
print ('Init output: ', outarr)

# populate output array
for i in range (len (arr)):
    x = count[arr[i]] - 1
    outarr[x] = arr[i]
    print ('Output:      ', 'arr', i, 'pos', x, '->', arr[i])
    count[arr[i]] -= 1 # allow duplicates
print ('Output:      ', outarr)

arr = [n for n in outarr if n > 0]
print ('Sorted array:', arr)
