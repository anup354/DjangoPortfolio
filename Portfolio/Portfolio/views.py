
from django.shortcuts import render
from description.models import desc
from skill.models import skill
from education.models import study_detail
from contacts.models import Contact
from datetime import datetime

from django.contrib import messages

from django.core.mail import send_mail, EmailMultiAlternatives
def homePage(request):
    desc_data=desc.objects.all()
    skill_data=skill.objects.all()
    study_data=study_detail.objects.all()
    study_data=study_detail.objects.all()
    
    data={
        'desc_data':desc_data,
        'skill_data':skill_data,
        'study_data':study_data

    }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        con=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
        con.save()
        messages.success(request,"Your Message is being Sent!")

        # sending mail
        subjects=subject
        from_email=email
        msg=message
        to="anupkasula012@gmail.com"
        msg=EmailMultiAlternatives(subjects,msg,from_email,[to])
        msg.content_subtype='html'
        msg.send()
    return render(request,"index.html",data)

