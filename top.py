#
# Code by Alexander Pruss and under the MIT license
#

from mine import *

from mp_server_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)

playerPos = mc.player.getTilePos()
mc.player.setPos(playerPos.x, mc.getHeight(playerPos.x, playerPos.z)+1, playerPos.z)
