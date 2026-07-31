import datetime

now = datetime.datetime.now(datetime.timezone.utc)
log_message = f"Automated run executed at {now.isoformat()}\n"
print(log_message.strip())

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(log_message)