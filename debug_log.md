# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

exercise 1:
line 79 changed topping to topping_type
the redirect in pizza_order_submit() put a '/' in the url_for() instead of home
added db.session.commit() after db.session.add(pizza) so the pizza is saved to the db
changed name and size to order_name and pizza_size on lines 67 and 68 to get the form values

exercise 2:
lines 39 and 40 were setting the wrong arg names, changed to units and city
changed place to q for the api request
changed result_json['main']['temperature'] to result_json['main']['temp'] so it would get the actual data from the api result

exercise 3:
in utils.py on line 37 right_side[i] went out of range, I changed the i to j to fix this.
in utils.py on line 51 arr[mid] threw an error because mid was a float. Added a // to line 48 to make mid an integer