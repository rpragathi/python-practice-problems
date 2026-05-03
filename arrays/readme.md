What is an Array?
An array is a data structure that stores a collection of elements in contiguous memory locations. All elements are typically of the same data type, and each element can be accessed using an index.


Eg:
arr = [10, 20, 30, 40]

Index	Value
0	10
1	20
2	30
3	40

Key Characteristics
	• Stores elements in continuous memory
	• Uses zero-based indexing
	• Provides constant time access → O(1)
	• Typically stores homogeneous data (same type)
	• Fixed size in low-level languages (C/C++)

Memory Representation
If base address = 100 and each element takes 4 bytes:
Index	Address	Value
0	100	10
1	104	20
2	108	30
3	112	40

Address Calculation Formula
Address of A[i] = Base Address + (i × Size of each element)


Advantages
	• Fast access using index → O(1)
	• Simple and easy to use
	• Memory efficient

Disadvantages
	• Fixed size (in some languages)
	• Insertion and deletion are costly → O(n)
	• Requires contiguous memory

Note (Python)
In Python:
arr = [10, 20, 30, 40]

This is technically a list, not a strict array:
	• Dynamic size
	• Can store different data types
But conceptually, it behaves like an array.

