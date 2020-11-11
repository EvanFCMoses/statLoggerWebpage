from django.http import HttpResponse, HttpRequest

helloWorld = """
<!DOCTYPE html>
<html>
<head>
<title>Impromptu Machinations</title>
<style>
    body {
        width: 1000px;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
        background: #AAAAAA;
    }
    div {
      padding: 30px;
      background: #FFFFFF;
      margin: 30px;
      border-radius: 5px;
      border: 1px solid #888888;
    }
    pre {
      padding: 15px;
    }
    code, pre {
      font-size: 16px;
      background: #DDDDDD
    }
</style>
</head>
<body>
  <div>
    <h1>future page for inputing data</h1>
    <p>currently we are thinking of doing things through the admin area.</p>
  </div>
</body>
</html>
"""

def index(request):
    return HttpResponse(helloWorld.replace("{IPADDRESS}",request.get_host()))
