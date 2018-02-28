from mine import *
from sys import argv
from _mp_ds_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
mc.postToChat(mc.player.getTilePos())
