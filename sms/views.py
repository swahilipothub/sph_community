import africastalking
import random
import logging

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from contacts.models import Contact, Group
from .forms import SmsForm
from .models import Sms
from .AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


@login_required
def sms_list(request):
    sms_list = Sms.objects.filter(user=request.user).order_by('-created')
    return render(request, 'sms/sms_list.html', {'sms_list': sms_list})


@login_required
def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.user, request.POST)
        username = request.user.company.africastalking_username
        api_key = request.user.company.africastalking_api_key
        sender = request.user.company.africastalking_sender_id
        bulkSMSMode = 1
        enqueue = 1
        
        if api_key:
            africastalking.initialize(username, api_key)
            # Initialize SMS service 
            sms = africastalking.SMS

            if form.is_valid():
                category = form.cleaned_data['category']
                message = form.cleaned_data['message']

                category_name = Group.objects.filter(id__in=category)
                contacts = []
                for item in category_name:
                    category_id = item.id
                    recipients = Contact.objects.values_list(
                        'mobile', flat=True).filter(category=category_id).distinct().order_by()
                    mobiles = ",".join(recipients)
                    contacts.append(recipients)
                
                flat_list = []
                for sublist in contacts:
                    for item in sublist:
                        flat_list.append(item)
                to = list(set(flat_list))
                results = sms.send(message, to, sender, enqueue)

                for recipient in results.get('SMSMessageData')['Recipients']:
                    user = request.user
                    message = message
                    number = recipient['number']
                    messageId = recipient['messageId']
                    status = recipient['status']
                    cost = recipient['cost']
                    instance = Sms.objects.create(user=user,
                                    message=message, number=number,
                                    messageId=messageId, status=status, cost=cost)
                    instance.category.set(category_name)
                messages.success(request, "Message Successfully delivered.")
            else:
                messages.error(request, u'Hi there! Please provide an API_KEY in you profile')
    else:
        form = SmsForm(request.user)
    return render(request, 'sms/sms_create.html', {'form': form})


@login_required
def sms_fetch(request, template_name='sms/fetch_messages.html'):
    last_received_id = 0
    username = request.user.profile.africastalking_username
    apikey = request.user.profile.africastalking_api_key
    gateway = AfricasTalkingGateway(username, apikey)
    
    while True:
        messages = gateway.fetchMessages(last_received_id)
        for message in messages:
            message_from = message['from']
            messate_to = message['to']
            message_date = message['date']
            message_text = message['text']
            message_link_id = message['linkID']
            last_received_id = message['id']

            return render(request, template_name, {'object': message})


@login_required
def user_balance(request):
    username = request.user.profile.africastalking_username
    api_key = request.user.profile.africastalking_api_key
    if api_key == None:
        messages.error(request, u'Hi there! Please provide an API_KEY in you profile')
    else:
        africastalking.initialize(username, api_key)
        app = africastalking.Application
        bal = app.fetch_application_data()
        balance = bal["UserData"]["balance"]
        return render(request, 'sms/balance.html', {'object': balance})
    
