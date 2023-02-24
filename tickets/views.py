from django.shortcuts import render
from rest_framework import status
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket, QrCode, Message
from .serializer import TicketSerializer
from django.views.decorators.csrf import csrf_exempt
import random
from .mail import send_mail
from django.shortcuts import redirect

# Domain Name or URL
mainUrl = "WEB_URL"


@api_view(['GET'])
def index(request):
    return render(request, "index.html")


@api_view(['POST'])
def postMsg(request):
    try:
        name = request.POST.get("name").capitalize()
        email = request.POST.get("email").lower()
        subject = request.POST.get("subject")
        query = request.POST.get("query")
        res = Message.objects.create(
            Name=name, Email=email, Subject=subject, Message=query)
        if (res):
            return Response({"Status": True, "Data": "Message send successfully."})
        else:
            raise Exception
    except:
        return Response({"Status": False, "Data": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def submit(request):
    try:
        email = request.POST.get("email").lower()
        if Ticket.objects.filter(Email=email).exists():
            return render(request, "notify.html", {"message": "You are already registered. Check email for details.", "status": 200, "url": mainUrl + '/ticket/search?email=' + email})
        else:
            ticketid = ''
            while True:
                reference_no = checkUnique()
                print('i am in while')
                if reference_no:
                    ticketid = reference_no
                    break

            name = request.POST.get("name").capitalize()
            mobile = request.POST.get("mobile")
            CollegeName = request.POST.get("collegeName").capitalize()
            DepartmentName = request.POST.get("departmentName").capitalize()
            Class = request.POST.get("class").capitalize()
            Promo = request.POST.get("promotion").capitalize()
            Address = request.POST.get("address").capitalize()
            res = False
            res = Ticket.objects.create(
                ticketId=ticketid, Name=name, Email=email, Mobile=mobile, College=CollegeName, Department=DepartmentName, Semester=Class, Address=Address, Promo=Promo)

            if res:
                serialized = TicketSerializer(res, many=False).data
                qr_code = QrCode.objects.create(
                    text='{ticketId: ' + serialized["ticketId"] + ', name: "' + serialized["Name"] + '"}', ticketId=serialized["ticketId"])
                if qr_code:
                    qr_link = mainUrl + '/media/qrcode/' + \
                        serialized["ticketId"] + 'qr.png'
                    serialized = TicketSerializer(res, many=False).data
                    data_val = {
                        'ticketId': serialized["ticketId"], 'name': serialized["Name"], 'qr_code': qr_link}
                    html = render_to_string('ticket.html', data_val)
                    email_sent_msg = send_mail(
                        email, "IODump invites you for a grand event .", html)
                    if (email_sent_msg == "Mail send"):
                        return redirect('/ticket/view?id=' + serialized["ticketId"])
                    else:
                        raise Exception

                else:
                    raise Exception
            else:
                raise Exception
    except Exception as e:
        return render(request, "error.html", {"title": "IODump", "status": 400, "exception": e})


@api_view(['GET'])
def home(request):
    return Response('Silience is peace!')


@api_view(['GET'])
def viewTicket(request):
    try:
        id = request.GET.get('id')
        ticket = Ticket.objects.filter(ticketId=id).exists()
        res = Ticket.objects.filter(
            ticketId=id).first()
        serialized = TicketSerializer(res, many=False).data
        qr_link = mainUrl + '/media/qrcode/' + \
            serialized["ticketId"] + 'qr.png'
        data_val = {'ticketId': serialized["ticketId"],
                    'name': serialized["Name"], 'qr_code': qr_link}
        return render(request, "view.html", data_val)
    except Exception as e:
        return render(request, "error.html", {"title": "IODump", "status": 404, 'exception': e}, status=404)


@api_view(['POST'])
def searchTicket(request):
    try:
        id = request.POST.get('email')
        res = Ticket.objects.filter(
            Email=id).first()
        serialized = TicketSerializer(res, many=False).data
        qr_link = mainUrl + '/media/qrcode/' + \
            serialized["ticketId"] + 'qr.png'
        data_val = {'ticketId': serialized["ticketId"],
                    'name': serialized["Name"], 'qr_code': qr_link}
        return render(request, "view.html", data_val)
    except:
        return render(request, "output.html", {"title": "IODump", "status": 404, "msg": " email id not registered. Please register first", "email": id}, status=404)


@api_view(['GET'])
def getAll(request):
    try:
        if request.user.is_authenticated:
            res = Ticket.objects.all().order_by('-created_on')
            serialized = TicketSerializer(res, many=True)
            # x = 0
            # for i in serialized.data:
            #     if x < 12:
            #         pass
            #     else:
            #         qr_link = mainUrl + '/media/qrcode/' + i["ticketId"] + 'qr.png'
            #         data_val = {'ticketId': i["ticketId"], 'name': i["Name"], 'qr_code': qr_link}
            #         html = render_to_string('ticket.html', data_val)
            #         email_sent_msg=send_mail(
            #             i['Email'], "IODump invites you for a grand event .", html)
            #     x = x+1
            return Response({
                'Success': True,
                'data': serialized.data
            })
        else:
            return redirect('/')
    except:
        return Response({"Status": False, "Error": "Something went wrong. Try again later."}, status=status.HTTP_400_BAD_REQUEST)


def checkUnique():
    ref_no = create_new_ref_number()
    if Ticket.objects.filter(ticketId=ref_no).exists():
        return False
    else:
        return ref_no


def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999))
