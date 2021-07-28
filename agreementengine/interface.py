class Interface:
    def __init__(self, request):
        self.request = request

    def filter(request):
        return True

    def parse(request):
        return request.json

    def match(request):
        return []
