from ursina import *
from random import randint

app = Ursina()
MAP_LIMIT = 24
PLAYER_SPEED = 5

Sky()

ground = Entity(
    model='plane',
    scale=50,
    texture='grass',
    collider='box'
)

player = Entity(
    model='cube',
    texture='white_cube',
    scale=(1,2,1),
    position=(0,1,0),
    collider='box'
)

camera.parent = player
camera.position = (0,5,-10)
camera.rotation_x = 20

soldiers = []
enemies = []

score = Text(text="Vojaci: 0", position=(-0.85,0.45), scale=2)

def spawn_soldier():
    s = Entity(
        model='cube',
        texture='brick',
        scale=(1,2,1),
        position=(randint(-20,20),1,randint(-20,20)),
        collider='box'
    )
    soldiers.append(s)

def spawn_zombie():
    z = Entity(
        model='cube',
        texture='grass',
        scale=(1,2,1),
        position=(randint(-20,20),1,randint(-20,20)),
        collider='box'
    )
    enemies.append(z)

kraken = Entity(
    model='sphere',
    texture='brick',
    scale=4,
    position=(15,2,15),
    collider='box'
)

for _ in range(5):
    spawn_soldier()
    spawn_zombie()

def update():
    player.x += held_keys['d'] * time.dt * PLAYER_SPEED
    player.x -= held_keys['a'] * time.dt * PLAYER_SPEED
    player.z += held_keys['w'] * time.dt * PLAYER_SPEED
    player.z -= held_keys['s'] * time.dt * PLAYER_SPEED

    player.x = clamp(player.x, -MAP_LIMIT, MAP_LIMIT)
    player.z = clamp(player.z, -MAP_LIMIT, MAP_LIMIT)

    if player.y < -5:
        player.position = (0,1,0)

    for s in soldiers[:]:
        if player.intersects(s).hit:
            soldiers.remove(s)
            destroy(s)
            score.text = f"Vojaci: {5 - len(soldiers)}"

    for e in enemies:
        e.look_at(player)
        e.position += e.forward * time.dt * 2

        if player.intersects(e).hit:
            print("💀 Zabil ťa zombík!")
            application.quit()

    kraken.look_at(player)
    kraken.position += kraken.forward * time.dt * 1

    if player.intersects(kraken).hit:
        print("🐙 Kraken ťa zničil!")
        application.quit()

app.run()
