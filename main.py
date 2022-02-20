from discord import Webhook, RequestsWebhookAdapter
import time
import sys
import itertools
import threading

def animate():
    for c in itertools.cycle([ " ", ".", "..", "..."]):
        if done:
            break
        sys.stdout.write('\r>>> Spamming ' + c)
        sys.stdout.flush()
        time.sleep(0.7)

print(""" ▄█     █▄     ▄█    █▄            ▄████████    ▄███████▄    ▄████████   ▄▄▄▄███▄▄▄▄     ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████ 
███     ███   ███    ███          ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
███     ███   ███    ███          ███    █▀    ███    ███   ███    ███ ███   ███   ███ ███   ███   ███   ███    █▀    ███    ███ 
███     ███  ▄███▄▄▄▄███▄▄        ███          ███    ███   ███    ███ ███   ███   ███ ███   ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███     ███ ▀▀███▀▀▀▀███▀       ▀███████████ ▀█████████▀  ▀███████████ ███   ███   ███ ███   ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███     ███   ███    ███                 ███   ███          ███    ███ ███   ███   ███ ███   ███   ███   ███    █▄  ▀███████████ 
███ ▄█▄ ███   ███    ███           ▄█    ███   ███          ███    ███ ███   ███   ███ ███   ███   ███   ███    ███   ███    ███ 
 ▀███▀███▀    ███    █▀          ▄████████▀   ▄████▀        ███    █▀   ▀█   ███   █▀   ▀█   ███   █▀    ██████████   ███    ███ 
                                                                                                                      ███    ███ """)
time.sleep(2)
print("Made by - github.com/zZan54")

time.sleep(2)
print(" ")
print(" ")
webhook = input(">>> Send your webhook here: ")
print(" ")
print(" ")
msg = input(">>> Msg you want to spam: ")
print(" ")
print(" ")
howMany = int(input(">>> How many times you want to spam the msg: "))
print(" ")
print(" ")
delay = int(input(">>> Delay (0.1 - 10) (type 0 for no delay): "))
if delay > 10:
    print(" ")
    print(" ")
    print("Delay must 10 or lower.")
    print(" ")
    print(" ")
    delay = int(input("Delay (0.1 - 10) (type 0 for no delay): "))
else:
    exit

webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())

done = False
t = threading.Thread(target=animate)
t.start()
for i in range(howMany):
    time.sleep(delay)
    webhook.send(msg)
time.sleep(1)
done = True
print("Done!")