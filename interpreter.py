#
# Code under the MIT license by Alexander R. Pruss
#
# Useful for checking which interpreter RaspberryJamMod's /py command is picking up.
#

from mine import *
import sys
import os

from mp_server_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
mc.postToChat("Python interpreter "+sys.executable+" "+sys.version)

mc.player.getRotation()

try:
    userName = mc.player.getName()
except:
    try:
        userName = os.environ['MINECRAFT_PLAYER_NAME']
    except:
        userName = "unspecified"

mc.postToChat("Invoked by user "+userName)
mc.postToChat("Server "+str(mc.conn.socket.getpeername()))
