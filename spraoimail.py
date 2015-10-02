from flask_mail import Message

def send_email_report(mail, email_address, correct_answers, chosen_answers):
        
    body = 'Dear User,\
           \
           Thanks for completing your French test on Spraoi. Please, find attached your results in PDF.\
           \
           Kind regards,\
           \
           Spraoi Team'
    title = 'Your French test on SPRAOI'
    
    # create the message instance
    message = Message(
        subject=title,
        body=body,
        recipients=[email_address]
    )
    
    # generate a PDF report
    pdf = None
    
    # attach the PDF
    # message.attach(
    #     filename="spraoi_report.pdf",
    #     content_type="application/pdf",
    #     data=pdf
    # )
    
    mail.send(message)