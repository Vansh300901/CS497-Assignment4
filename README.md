# CS497-Assignment4

1. Top k frequent elements

Algorithm:
-We make a dictionary where we store the occurance of each number where the number is the key and the occurance is the value
-We then iterate through the dictionary, and try to find the key which has the highest value out of all
-We then append it to the return list, and remove it from the dictionary.
-We do this until we have k elements in the returnlist, and we return the returnlist

Time Complexity: O(k \* n^2) because we are iterating through all the elements almost twice (one when we are initializing the dictionary and second when we are iterating through the key value pairs in the dictionary)

Space Complexity: O(k \* n) because we have a returnList which holds k elements and we have a dictionary which holds n elements.

2. k closest elements

Algorithm:
-We make 2 pointers, one pointing at the start of the array and another pointing at the end of the array
-We use the binary search method to find a spot where this element would be inserted if it had to.
-We take that intersection point and make both of our pointers to point to the same index
-We use the sliding window to check which one of the element out of the left index and right index has value closer to the value, we then update our left or right index accordingly to check for the next closest value.
-We keep on doing this until we have k elements between the left index and the right index
-We then return the sliced portion of the array which contains k elements

Time complexity: O(k\*logn) because we are using binary search on the list and running the second loop for k times.

Space complexity: O(1) because we don't really use additional space except using the left and right pointers.
