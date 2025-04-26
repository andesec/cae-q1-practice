## Create a card like text string that prints all the details for the PIAIC student card.
name = "Nate"
id = 123
course = "CAE Q1"
batch = "Batch 71"
status = "Active"

# Triple quotes are used to allow multi-line strings
card = """
+---------------------+
|                     |
|    PIAIC Student    |
|                     |
|   Name: {name}      |
|   ID: {id}          |
|   Course: {course}  |
|   Batch: {batch}    |
|   Status: {status}  |
|                     |
+---------------------+
""".format(name=name, id=id, course=course, batch=batch, status=status)
print("Printed using format method")
print (card)
# The above code creates a formatted string that represents a student card for PIAIC.

# Triple quotes are used to allow multi-line strings
card = f"""
+---------------------+
|                     |
|    PIAIC Student    |
|                     |
|   Name: {name}      |
|   ID: {id}          |
|   Course: {course}  |
|   Batch: {batch}    |
|   Status: {status}  |
|                     |
+---------------------+
"""
print("Printed using f-string")
print (card)
# The f-string method is more readable and concise.