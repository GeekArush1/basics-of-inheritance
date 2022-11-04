class Bird:
    def speak(self):
        print("Inside Bird: Speak")
class Sparrow(Bird):
    def sing(self):
        print("Inside Sparrow: Sing")
o1=Bird()
o1.speak()
o1.sing()
