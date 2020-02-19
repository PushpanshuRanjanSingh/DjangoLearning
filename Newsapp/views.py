from django.shortcuts import render
from datetime import datetime
# Create your views here.
def display(req):
    d=datetime.now()
    h=d.strftime("%H")
    h=int(h)
    msg=str()

    if h<12 and h>4:
        msg="Good Morning"
    elif h>12 and h<16:
        msg="Good Afternoon"
    elif h>16 and h<20:
        msg="Good Evening"
    else:
        msg="Good Night"
    
    dct={'insert_msg':msg, 'insert_date':d}
    return render(req, 'index.html', dct)