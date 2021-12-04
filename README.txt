Taylor Telles
Assignment 10.1: Your Own Class

The class I have created is a simple tool for creating and editing a hairstyle. With this class you can define the initial
color and length of the hairstyle, but can also override these values later on. You can also cut the hair a desired amount
of inches or add a desired length of extensions to the hair.

The class variables needed are self.color and self.length.
self.color must be a string value containing the initial color of the hair, and must be your first argument when defining
your hairstyle.
self.length must be a float or and int value containing the initial length of the hair in inches, and must be your second
argument when defining your hairstyle.

There are six methods within this class.
get_color returns the current color of the hair as a string value and requires no arguments.
get_length returns the current length of the hair in inches and requires no arguments.
set_color is used to override the current color of the hair with a new string value. There is one argument needed for this
method which is color. color must be a string value. The class variable self.color is set as equal to the new variable
color, and the new self.color is returned.
set_length is used to override the current length of the hair with a new float or int value in inches. There is one argument
needed for this method which is length. length must be a float or int value and must be in inches. The class variable
self.length 