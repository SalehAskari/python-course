status_code = 503

match status_code:
    case 200:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500 | 503:
        print("Server Error")
    case _:
        print("Unknown Status")