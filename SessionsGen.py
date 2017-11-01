import sys

# Preparing script to be managed by git.
# Change #1

header = '<?xml version="1.0" encoding="utf-8"?> \n'

ArrayOfSessionDataOpen = '<ArrayOfSessionData '
xmlns1 = 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
xmlns2 = 'xmlns:xsd="http://www.w3.org/2001/XMLSchema"'
ArrayOfSessionDataEnd = '> \n'

ArrayOfSessionDataClose = '</ArrayOfSessionData>'

hostName=""

class SessionData:
    RowOpen = "<SessionData "
    SessionId = "SessionId=" + hostName
    SessionName = "SessionName=" + hostName
    ImageKey = 'ImageKey="computer" '
    Host = "Host=" + '"192.168.0.40" '
    Port = "Port=" + '"22" '
    Proto = "Proto=" + '"SSH "'
    PuttySession = "PuttySession=" + '"Default Settings"' + " "
    Username = "Username=" + '"bob" '
    ExtraArgs = "ExtraArgs=" + '"-pw Fly2Mars" '
    SPSLFileName = "SPSLFileName=" +'"" '
    RowClose = "/>" + "\n"

my_sessionData = SessionData()

f = open("SiteList.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                                # Note: if you want to write to the file use "w" as second argument
fout = open("Sessions.XML", "w")

fout.write(header)
fout.write(ArrayOfSessionDataOpen + xmlns1 + xmlns2 + ArrayOfSessionDataEnd)
siteCount = 0
for line in f.readlines():   # read lines
    hostName = line.rstrip('\n')
    my_sessionData.SessionId= "SessionId=" + '"' + hostName + '"' + " "
    my_sessionData.SessionName= "SessionName=" + '"' + hostName + '"' + " "
    row = my_sessionData.RowOpen + my_sessionData.SessionId
    row += my_sessionData.SessionName
    row += my_sessionData.ImageKey
    row += my_sessionData.Host
    row += my_sessionData.Port
    row += my_sessionData.PuttySession
    row += my_sessionData.Username
    row += my_sessionData.ExtraArgs
    row += my_sessionData.SPSLFileName
    row += my_sessionData.RowClose
    siteCount += 1
    print(row)
    fout.write(row)
    ##print(siteCount)

fout.write(ArrayOfSessionDataClose)
f.close()                   # It's important to close the file to free up any system resources.
fout.close()


