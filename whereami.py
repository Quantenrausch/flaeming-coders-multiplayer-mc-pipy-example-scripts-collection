from mine import *
from sys import argv
from mp_server_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
mc.postToChat(mc.player.getTilePos())
