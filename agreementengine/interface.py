class Interface:
    @classmethod
    def filter(cls, request):
        return False

    @classmethod
    def parse(cls, request):
        return request

    @classmethod
    def match(cls, data):
        pass
