# NOTE: add your world info path here
param worldInfoPath = "C:/Users/piegu/Scenic/examples/airsim/worldInfo/droneBlocks"

model scenic.simulators.airsim.model

# Spawns 10 arbritrary static obstacles on the ground
# drone patrols to these positions uniformly randomly

platforms = []
ground = getPrexistingObj("ground")
centerArea = RectangularRegion(Vector(0,200,30), 0, 100,100)


blockCount = 10
for i in range(blockCount):
    platforms.append(new StaticObj on ground, 
        contained in centerArea,
        with assetName "Cone", # use * to pick a random asset in assets
        with width Range(3,10),
        with length Range(3,10),
        with height 10)





points = []
for plat in platforms:
    point = new Point on plat
    points.append(point.position)

ego = new Drone at Uniform(*points) + (0,0,1),
    with behavior Patrol(points,True)

terminate after 30 seconds