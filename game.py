from ursina import Ursina, Entity, Text, invoke, destroy, held_keys, color, window
import random as rnd

app = Ursina()
window.fullscreen=True


player = Entity(model="cube", color=color.yellow, position=(0, -3.5), collider="box")
enemies = []

def movement_player():
    player.x += held_keys["d"] * 0.1
    player.x -= held_keys["a"] * 0.1


def update():
    movement_player()

    if player.y >= -1.5:
        player.position = (0, -3.5)

    for enemy in enemies:
        enemy.y -= 0.05
        if player.intersects(enemy):
            
            lambda: destroy(enemies)
            message=Text(text="you lose!")
           
            invoke(lambda:destroy(message),delay=2)
            player.position=(0,-3.5)
            

def create_barrier():
    barrier = Entity(model="quad", scale=(15, 0.5, 15))
    barrier.y = -1.5


def create_enemies():
    enemies.clear()
    for spawning in range(5):
        x_axis = rnd.uniform(-10,10)
        enemy = Entity(model="circle", color=color.red, position=(x_axis,4),collider="box")
        enemies.append(enemy)
        
        
def spawning_delay():
    create_enemies()
    invoke(spawning_delay,delay=2)


create_barrier()
spawning_delay()

app.run()
