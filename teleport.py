from mine import *
from sys import argv
from _mp_ds_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
mc.player.setTilePos(int(argv[1]), int(argv[2]), int(argv[3]))
