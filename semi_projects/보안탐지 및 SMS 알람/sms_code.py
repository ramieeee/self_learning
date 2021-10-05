import linecache
from twilio.rest import Client

def sms_message():
    account_sid = "[personal sid]"
    auth_token = "[personal token]"
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            to="+82[phone num]"
            from = "+17177756719"
            body=alert_content)
    print(message.sid)

    # save log_time into time file
    with open("time.txt", "w") as time_write:
        time_write.write(log_data)

# total lines
i = 0
with open("/var/log/snort/alert", "r") as alert_file:
    for line in alert_file:
        i += 1

# time containing line, alert message
log_data = linecache.getline('/var/log/snort/alert', i - 9).strip()
alert_content = linecache.getline('/var/log/snort/alert', i - 7).strip()

# text comparison
with open("time.txt", "r"):
    time_data = linecache.getline('time.txt', 1).strip()

# alert sms sending when data are not identical
if log_data != time_data:
    sms_message()
    print("Alert message was sent")
else:
    print("No updated alerts")
