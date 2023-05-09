# #!/usr/bin/python3
# class Dog:
#     # This is a static variable
#     num_of_dogs = 0
#
#     def __int__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         Dog.num_of_dogs += 1
#     @staticmethod
#     def get_num_of_dogs():
#         print("There are currently {} dogs".format(Dog.num_of_dogs))
#
#
# spot = Dog("Spot", "malinoys")
# mukhtar = Dog("Mukhtar 🐕", "metis")
# mukhtar.get_num_of_dogs()
# print(mukhtar.name)
# #
# # def main():
# #     spot = Dog("Spot", "malinoys")
# #     mukhtar = Dog("Mukhtar 🐕", "metis")
# #     mukhtar.get_num_of_dogs()
# #     print(mukhtar.name)
# #
# #
# # main()

class Animal:
    def __init__(self, birth_type="Unknown", appearance="Unknown", blooded="Unknown"):
        self.__birth_type = birth_type
        self.__appearance = appearance
        self.__blooded = blooded

class Dog(Animal):
    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name, breed, birth_type="born alive", appearance="fur", blooded="warm blooded",nurse_young=True):
        self.name = name
        self.breed = breed
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():

    spot = Dog("Spot","malinoys")
    doug = Dog("Doug", "boerboel")
    mukhtar = Dog("Mukhtar 🐕","dingo")
    # Call a static method
    spot.get_num_of_dogs()
    print(mukhtar.name, mukhtar.breed)



main()
