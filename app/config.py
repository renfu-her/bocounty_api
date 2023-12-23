import os

SECRET_KEY: bytes = "b3236621e0129c87e2aa90395dc16ccbc431aa2c16535a06613bf5d8855facd1"
STORAGE_PATH: str = os.path.join(os.path.abspath("."), "storage")
SETTING_FILE: str = os.path.join(os.path.abspath("."), "setting.json")
DEBUG: bool = True
MAIL_ENABLE = True
MAIL_HOST = "bocounty2022@gmail.com"
MAIL_PASSWORD = "qzoejyriakvczlht"
MAIL_PORT = 587
MAIL_PATTERN = "%s@gms.ndhu.edu.tw"
MAIL_VERIFY_HOST = "35.206.249.212:8000"
#
#   {
#   "enable": true,
#   "host": "pony076152340@gmail.com",
#   "password": "ettesucqlqgpnliq",
#   "port": 587,
#   "pattern": "t%s@ntut.org.tw"
# }
