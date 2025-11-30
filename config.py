import os
from os import getenv

# ------------------ Configuration ------------------

# Required variables
API_ID = int(os.environ.get("API_ID", "27400172"))
API_HASH = os.environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8204209080:AAHQx2wvrV1yrLoJgrxswYgLBf_mkzXqKHQ")
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)  # Optional, can be None
OWNER_ID = int(os.environ.get("OWNER_ID", "7540570087"))

# Optional variables with defaults
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "7540570087 7463601722").split()))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003414109205"))
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003414109205"))
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://greenhornet63603:CvnxnjzknPLxYOfo@cluster0.qif4g18.mongodb.net/?appName=Cluster0")

# ------------------ Debugging ------------------
# Uncomment to check values
# print("API_ID:", API_ID)
# print("API_HASH:", API_HASH)
# print("BOT_TOKEN:", BOT_TOKEN)
# print("OWNER_ID:", OWNER_ID)
# print("SUDO_USERS:", SUDO_USERS)
# print("CHANNEL_ID:", CHANNEL_ID)
# print("PREMIUM_LOGS:", PREMIUM_LOGS)
# print("MONGO_URL:", MONGO_URL)
