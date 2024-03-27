
### Debugging calendar.py

#

**Isssue - 1**

Line - 28 is inserting a new node all the time the Book() method has been called. It should come under the ELSE condition and only be called if root node is not none.

#

**Issue - 2**

Line - 9 is only taking into account the condition where start time of a new booking is less than end time of an already booked slot. The start time of the new booking needs also to be less than the start time of an already booked slot, else there will be an overlap. We need to add the condition where both the new booking timings are less than the start time of an already booked slot. Added in line - 13,14 in my calendar.py file.
#

**Issue - 3**

Line - 14. Same kind of issue as the second one. It is only taking into account the condition where end time of a new booking is greater than start time of an already booked slot. The start time of the new booking needs also to be greater than the end time of an already booked slot, else there will be an overlap. We need to add the condition where both the new booking timings are greater than the end time of an already booked slot. Added in line - 23,24 in my calendar.py file.
#

**Issue - 4**

There is no condition here in the code to check for overlap booking. We need to add the condition for the same and return False in such case. Added in line - 10 in my calendar.py file.
#