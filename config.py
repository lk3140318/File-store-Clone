# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002293590291').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')
        
# Bot Information
API_ID = int(environ.get("API_ID", "15529802"))
API_HASH = environ.get("API_HASH", "92bcb6aa798a6f1feadbc917fccb54d3")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://graph.org/file/d6e3a7c39df4ad0372966.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '821215952').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "XeonFileStoreBot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://yexecax88:dUpjO0Z7esWfXESJ@cluster0.saf78.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "yexecax88")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://hopepaw650:q9lpAOJZCnKTrDE8@clustepiro.7q6ji.mongodb.net/?retryWrites=true&w=majority&appName=Clustepiro")
DB_NAME = environ.get("DB_NAME", "hopepaw650")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "20")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002223699788"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "publicearn.com") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "de08290b12d9e34191f3a057070a50a18187fff3") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/DowPCMOffcL/13") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://xeonflix.blogspot.com/2024/08/xeon-bots.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', False)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
