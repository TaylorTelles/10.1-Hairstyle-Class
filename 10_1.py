#Taylor Telles
#Assignment 10.1: Your Own Class

#The purpose of this assignment is to create a class which implements elements of what we have learned over time.

#creates the hairstyle class
class Hairstyle:
    #defining the constructor
    def __init__(self, color, length):
        #defines class variables for the initial color and length of the hair
        self.color = color
        self.length = length
    
    #returns the color of the hair (must be str)
    def get_color(self):
        return self.color

    #returns the current length of the hair (in inches)
    def get_length(self):
        return self.length

    #overrides the color of the hair and returns the new color
    def set_color(self, color):
        self.color = color
        return color

    #overrides the length of the hair and returns the new length
    def set_length(self, length):
        self.length = length
        return length
    
    #removes length from the hair and returns the new length
    def cut_inches(self, inches):
        self.length = self.length - inches #subtracts the desired amount of inches from the current length
        return self.length

    #adds length to the hair and returns the new length
    def install_extensions(self, inches):
        self.length = self.length + inches #adds the desired amount of inches to the current length
        return self.length

#defines the main function for testing code        
def main():
    #testing functions
    hair1 = Hairstyle("blonde", 23)
    print("Your hair is ", hair1.get_color(), " and ", hair1.get_length(), " inches long.")

    hair1.set_color("brown")
    hair1.set_length(30)
    print("Your hair is ", hair1.get_color(), " and ", hair1.get_length(), " inches long.")

    hair1.cut_inches(10)
    print("Your hair is ", hair1.get_length(), " inches long.")

    hair1.install_extensions(12)
    print("Your hair is ", hair1.get_length(), " inches long.")

#calls the main function
if __name__=="__main__":
    main()
