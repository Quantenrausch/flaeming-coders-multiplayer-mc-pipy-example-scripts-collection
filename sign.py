from mine import *
from mp_server_config import *
mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
mc.conn.send("world.setBlocks",0,0,0,5,5,5,63,1,"{id:\"Sign\",Text1:\"My sign\"}")
