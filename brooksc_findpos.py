#!/usr/bin/env python

#import the minecraft.py module from the minecraft directory
from mine import *
#import minecraft block module

#import time, so delays can be used
import time


if __name__ == "__main__":
    from mp_server_config import *
    mc = Minecraft(Connection(serveradress, serverport), name=playernameonserver)
#    mc.postToChat("Flattening surface")
#    mc.setBlocks(-128,0,-128,128,64,128,0)
#    mc.setBlocks(-128,0,-128,128,-64,128,block.SANDSTONE.id)
#    mc.postToChat("Putting a diamong block at 0,0,0")
#    mc.setBlock(0,0,0,block.DIAMOND_BLOCK.id)

    while True:
        #Find out your players position
        playerPos = mc.player.getPos()
        mc.postToChat("Find your position - its x=%s y=%s z=%s" % (int(playerPos.x), int(playerPos.y), int(playerPos.z)))
#        mc.postToChat("Find your position - its x=%.2f y=%.2f z=%.2f" % (playerPos.x, playerPos.y, playerPos.z))
        time.sleep(1)
