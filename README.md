

# Exercises:

1. Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. In other words, the Dog class does not inherit from the Pets class. Then assign three dog instances to an instance of the Pets class. Start with the following code below. Save the file as pets_class.py. Your output should look like this:

```
I have 3 dogs.
Tom is 6.
Fletcher is 7.
Larry is 9.
And they're all mammals, of course.
```


2. Using the same file, add an instance attribute of is_hungry = True to the Dog class. Then add a method called eat() which changes the value of is_hungry to False when called. Figure out the best way to feed each dog and then output “My dogs are hungry.” if all are hungry or “My dogs are not hungry.” if all are not hungry. The final output should look like this:

```
I have 3 dogs.
Tom is 6.
Fletcher is 7.
Larry is 9.
And they're all mammals, of course.
My dogs are not hungry.```