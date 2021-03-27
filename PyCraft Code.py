# Imports
import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

PyCraft = Ursina()
window.fps_counter.enabled = True
window.exit_button.visible = True
camera.fov = 50

# Textures
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
snow_texture = load_texture('assets/snow_texture.png')
diamond_texture = load_texture('assets/item_diamond.png')

# Audio
panch_sund = Audio('C:/Users/Gabri/Desktop/assets/assets_punch_sound.wav', loop = False, autoplay = False)

#B locks pick
block_pick = 1
def update():
    global block_pick
    if held_keys ['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys ['5']:
        block_pick = 5
    if held_keys['right mouse'] or held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()


# The Block

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
        parent = scene,
        position = position,
        model = 'C:/Users/Gabri/Desktop/assets/block.obj',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 0.5)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                panch_sund.play()
                if block_pick == 1:
                    voxle = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2:
                    voxle = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3:
                    voxle = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 4:
                    voxle = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 5:
                    voxle = Voxel(position = self.position + mouse.normal, texture = snow_texture)
                                

            if key == 'left mouse down':
                panch_sund.play()
                destroy(self)

class MinecraftSky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 200,
            double_sided = True)

# Hand
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm.obj',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.6,-0.6))

    def active(self):
        self.position = Vec2(0.5,-0.5)
    def passive(self):
        self.position = Vec2(0.6,-0.6)




for z in range(50):
    for x in range(50):
        voxle = Voxel(position = (x,0,z))
player = FirstPersonController(speed = 10, 
jump_height = 0.7,
cursor = Entity(parent=camera.ui, model='Circle', color=color.white, scale=.008, rotation_z=45))
sky = MinecraftSky()
voxle = Voxel()
hand = Hand()
PyCraft.run()
