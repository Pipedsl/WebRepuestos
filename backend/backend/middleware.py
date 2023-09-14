from django.http import HttpResponse
class CORSMiddleware:
    def __init__(self, get_response):
        # print("Optiones Init ***********")
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'OPTIONS':
            # print("Optiones***********")
            response = HttpResponse()
        else:
            # print("Optiones response***********")
            response = self.get_response(request)

        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Origin,Access-Control-Allow-Methods,Access-Control-Allow-Headers, Content-Type, Authorization"

        return response   