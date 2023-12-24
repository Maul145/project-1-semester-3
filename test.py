from datetime import datetime

today = datetime.now()
print(today)

date_time = today.strftime('%Y-%m-%d-%H-%M-%S')