import datetime

now = datetime.datetime.now(datetime.timezone.utc)
log_message = f"Second one executed at {now.isoformat()}\n"
print(log_message.strip())
with open("log2.txt", "a", encoding="utf-8") as f:
    f.write(log_message)