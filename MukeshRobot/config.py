
class Config(object):
    LOGGER = True
 

    API_ID = 27383453
    API_HASH ="4c246fb0c649477cc2e79b6a178ddfaa"
    TOKEN ="7394970820:AAF7_pWYaJ__LkL2PQ7dA7BhlbVvdsZUvoQ"
    OWNER_ID = 6352107773
    
    SUPPORT_CHAT =HEROKUBIN_01
    START_IMG ="https://te.legra.ph/file/386fdbaf3f9a740f129da.jpg"
    EVENT_LOGS ="-1002093247039"
    MONGO_DB_URI="mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
    
BOT_USERNAME =Test_robo_test_bot
    DATABASE_URL ="postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc"
    CASH_API_KEY =hbnb
    TIME_API_KEY =nej

    # Optional fields
    BL_CHATS = [6898413162]  # List of groups that you want blacklisted.
    DRAGONS = [6898413162]  # User id of sudo users
    DEV_USERS = [6898413162]  # User id of dev users
    DEMONS = [6898413162]  # User id of support users
    TIGERS = [6898413162]  # User id of tiger users
    WOLVES = [6898413162]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS =6
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
