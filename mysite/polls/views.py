from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
import json
import re
from .models import Users

def register(request):
    data = json.loads(request.body)
    # data = json.dumps(data)
    valid, msg = validateSignUP(data, ['name','email','password','usertype'])
    if valid:
        rows = Users.objects.filter(email = data['email'])
        if rows:
            return HttpResponse({ json.dumps({'result': "email is already exists!"}) }, content_type="application/json")
        else:
            Users.objects.create(name=data['name'],email=data['email'],password=data['password'],usertype=data['usertype'])
            return HttpResponse({ json.dumps(data) }, content_type="application/json")
    else:
        return HttpResponse({ json.dumps({'result': msg}) }, content_type="application/json")
    

def validateSignUP(post_data, field_list):
    reg_dict = {
        'name': "[a-zA-Z]",
        'email': "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        'password': "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    }
    usertype_list = ["Retailer", "Customer"]
    for field in field_list:
        value =  post_data.get(field)
        if value:
            if field == 'usertype':
                if value not in usertype_list:
                    return False, 'Please provide valid {0} : {1}, should be in {2}' .format(field, value, usertype_list)   
            elif not (field in reg_dict and len(re.findall(reg_dict[field],value))):
                return False, 'Please provide valid {0} : {1}' .format(field, value)    
        else:
            return False, 'Please provide {0}' .format(field)
    return True, "Success"
     