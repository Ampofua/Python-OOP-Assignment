class Person:  # creating a pyhon class
  def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

  def introduce(self): #pl
      print(f"Hey! {self.name} is my name. I am {self.age} years old and a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Ampofua", 28, "female")

# Call the introduce method
person1.introduce()
