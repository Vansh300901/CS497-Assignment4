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

3. k largest element of a Max Heap

Algorithm:
-We initialize a priority queue with the root of the heap
-Now we iterate through all the nodes of the heap
-Every time we iterate, we add the negated value of the node to the priority queue
-Then we find the left and rigth sub-child of the node by using the formula 2i + 1 and 2i + 2 respectively and add it to the heap
-At the end we return the returnList

Time Complexity : O(n) because we are iterating through the nodes only once

Space Complexity: O(n) because we are creating a pQueue which can hold as many items as there are in the heap.

4. Shortest Subarray with Sum at least K

Algorithm:
-We make a sumCounter list which any index i has the sum of all the numbers in num list until i index.
-Then we keep track of the indices for the list where the sum of the subarray is greater than k and add those indices to the deque
-If the sum is greater than k, then we update the returnLength depending on which value is smaller.
-When the sum is less, we try to remove the element from the end of the queue to deal with the negative numbers as well.
-At the end, we return the length we have computed so far because that has to be the smallest length

Time Complexity: O(n) because we iterate through all the elements in the num list once to create the sumCounter list. And then, we are kind of iterating over all of the sumCounter's element once.

Space Complexity: O(n + n) = O(n) because we need n additional spots to store the sumCounter for each element in the num list. And we need deque list to also store the indices, which can go upto the len(nums) for any given problem

5. Kth Smallest Prime Fraction

Algorithm:
-We iterate through the list, and for each element, we iterate through the remaining list and find what is their fraction's value is
-We append a list of fraction value, as well as both the elements used to calculate the fraction in a new list
-Once we are done iterating through all the remaining elements for each of the element in the list, we try to sort the new list on the basis of the their fraction value which is very first element of each element in the new list
-Whatever sorted list we get, we try to iterate through the sorted list until we have reached the kth element, and then just return the second and third element of the list at that index, because that gave us the smallest fraction.

Time complexity: O(n^2 + n) = O(n^2) because we iterate through the remaining list for every element in the list, and then we iterate through the new list we have created

Space Complexity: O(n^2) because we make every possible pair in the list for each element in the list.
