from plyer import notification
import schedule
import time


def send_notification():
    notification.notify(
        title="Pause reminder",
        message="Ricordati di prendere una pausa!",
        timeout=5
    )


while True:
    choice = int(input('''
Dopo quanto vuoi essere ricordato ? 
1) ogni tot ore
2) ogni tot minuti
 >> '''))
    if choice == 1 or choice == 2:
        break
    else:
        print("Errore!")

if choice == 1:
    ore = int(input("Dopo quante ore desideri essere ricordato ? : "))
    schedule.every(ore).hours.do(send_notification)
    if ore == 1:
        print("Ok, ti ricorderò ogni ora di prendere una pausa!")
    else:
        print("Ok, ti ricorderò ogni %s ore di prendere una pausa!" % ore)
else:
    minuti = int(input("Dopo quanti minuti desideri essere ricordato ? : "))
    schedule.every(minuti).minutes.do(send_notification)
    if minuti == 1:
        print("Ok, ti ricorderò ogni minuto di prendere una pausa!")
    else:
        print("Ok, ti ricorderò ogni %s minuti di prendere una pausa!" % minuti)

while True:
    schedule.run_pending()
    time.sleep(1)
