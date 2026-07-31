import datetime
import os

now = datetime.datetime.now(datetime.timezone.utc)
token = os.environ.get("SEC_TOKEN", "No token found")
log_message = f"Automated run at {now.isoformat()} with token: {token}\n"
print(log_message.strip())
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(log_message)