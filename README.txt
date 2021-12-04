Taylor Telles
Assignment 10.1: Your Own Class

GitHub: 

The class I have created is a simple tool for creating and editing a hairstyle. With this class you can define the initial
color and length of the hairstyle, but can also override these values later on. You can also cut the hair a desired amount
of inches or add a desired length of extensions to the hair.

The class variables needed are self.color and self.length.
self.color must be a string value containing the initial color of the hair, and must be your first argument when defining
your hairstyle.
self.length must be a float or and int value containing the initial length of the hair in inches, and must be your second
argument when defining your hairstyle.

There are six methods within this class.
get_color returns the current color of the hair as a string value and requires no arguments. self.color is returned.
get_length returns the current length of the hair in inches and requires no arguments. self.length is returned.
set_color is used to override the current color of the hair with a new string value. There is one argument needed for this
method which is color. color must be a string value. The class variable self.color is set as equal to the new variable
color, and the new self.color is returned.
set_length is used to override the current length of the hair with a new float or int value in inches. There is one argument
needed for this method which is length. length must be a float or int value and must be in inches. The class variable
self.length is set as equal to the new variable length, and the new self.length is returned.
cut_inches is used to remove a set amount of inches from the current length. There is one argument needed for this method
which is length. This variable length (which must be a float or int) is subtracted from the class variable self.length, 
and the new self.length is returned.
install_extensions is used to add a set amount of inches to the current length. There is one argument needed for this method
which is length. This variable length (which must be a float or int) is added to the class variable self.length, 
and the new self.length is returned.

The demo program for this class tests out each of the six methods included. It starts by creating the object hair1 with the
arguments "blonde" and 23. Because of this, when hair1.get_color() and hair1.get_length() are printed, the hair will be
described as blonde and 23 inches long. After this, hair1.set_color("brown") is called and hair1.set_length(30) is called.
This results in the hair being described as brown and 30 inches long. After this, hair1.cut_inches(10) is called which results
in the hair being described as 20 inches long. Then, hair1.install_extensions(12) is called which results in the hair being
described as 32 inches long.

The only file needed to run the demo program is the 10_1.py file itself. By running this file, the demo program will be run.
