class Fibonacci(object):
    """

    """

    def __init__(self, stop):
        """

        :param stop:
        :return:
        """
        self.stop = stop
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):

        fib = self.a

        if self.a > self.stop:
            raise StopIteration
        self.a, self.b = self.b , self.a + self.b

        return fib


for item in Fibonacci(13):
    print (item)