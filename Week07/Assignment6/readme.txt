Tavish Peckham
Data Structures
Assignment 6
23 March 2018

Single Linked List:
1. RemoveAllOccurance
   Set the current node to the head of the list. Then, traverse the front of
   the list to remove all of the selected value. If the entire list is one
   element, we simply return. Othwise, we know the front element of the
   list is NOT the value we are looking for. If the next value is equal to the
   value we are looking for, we set the next value of the current node to the
   next node that does not equal the value we are looking to remove.

2. SameSame
  If the two lists are not the same size, return False.
  Else, iterate through both lists and return False if any element
  in the first list does not equal the corresponding element in the second
  linked list. Else, return True.

3. Reverse
  Create a list to hold our linked list's elements. Then, set our linked list
  equal to the new reversed linked list.

Double Linked List:
4. Feed
  Create a list to hold the elements we are looking to add to the second
  linked list. Then, add elements from the front of the first linked list
  to the list and remove them. Then, add them in reverse order to the front
  of the second linked list.

5. Diff
  Create a new linked list for the elements we are looking for. Then iterate
  through the two linked lists, adding any elements that are in the first list
  that are not in the second list.

PositionalList
6. Play
  Simply follows the instructions laid out, nothing complicated.

7. SplitAfterPosition
  Create a new positional list. We use the validate function to set the _header
  of our new linked list to p. Then we set the trailer of the new linked list
  to the trailer of our original linked list. Then we set the trailer of the
  original linked list to the node after p, again using the validate function.
  This makes the last value of the original linked list the value p, and the
  new linked linked list begins at the trailer value of the original.
