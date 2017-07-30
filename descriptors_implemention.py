class TypedCheck(object):
    """

    """
    def __init__(self, attr_type,  attr_val=None):
        """

        :param attr_val:
        :param attr_type:
        """
        self.attr_val = attr_val
        self.attr_type = attr_type

    def __get__(self, instance, owner):
        """

        :return:
        """
        print("owner is --->" + str(owner))
        return self.attr_val

    def __set__(self, instance,  val):
        """

        :param val:
        :return:
        """
        print("instance is --->"+str(instance))
        if not isinstance(val, self.attr_type):
            raise TypeError("Must be %s" %self.attr_type)
        self.attr_val = val

class Test(object):
    """

    """

    name = TypedCheck(attr_type=str)
    age = TypedCheck(attr_type=int)


class Price(object):
    """

    """
    def __init__(self):
        """

        """
        self.price = 0

    def __get__(self, instance, owner):
        """

        :param instance:
        :param owner:
        :return:
        """
        return self.price

    def __set__(self, instance, value):
        """

        :param instance:
        :param value:
        :return:
        """
        if value < 0:
            raise ValueError("Price must be greater than 0")
        self.price = value

class Book(object):
    """

    """
    price = Price()

    def __init__(self, name, price):
        """

        :param name:
        :param price:
        """
        self.name = name
        self.price = price


book_obj = Book('python in nut sheel', 100)
print ("book name is --->")
print(book_obj.name)
print("book price is----->")
print(book_obj.price)
book_obj = Book('python in nut sheel', -100)
# obj = Test()
# obj.name = 'jayant'
# obj.age = 28
# print("name is -------->")
# print (obj.name)
# print("age is-->")
# print(obj.age)
# obj.age ='age'
