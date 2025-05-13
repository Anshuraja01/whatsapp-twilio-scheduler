from twilio.rest import Client
from datetime import datetime, timedelta
import time

account_sid = 'AC129dd00e2b141a32dced84d6466cbf82'
auth_token = '76a9ebe45dd5d0fc820f8ca117b1cd00'

client = Client(account_sid, auth_token)

def send_whatsapp_message( recipent_number, message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipent_number}'
        )

        print (f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')

name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient whatsapp number with country code: ')   
message_body = input(f'enter the message you want to send to {name}: ')

date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24hour formate): ')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_second = time_difference.total_seconds()

if delay_second <= 0:
    print ('The specified time is in the past. Please enter a future date and time: ')
else:
    print (f'Message schedule to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_second)

    send_whatsapp_message(recipient_number, message_body)