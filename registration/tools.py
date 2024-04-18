import random
from django.contrib.auth.models import User

list_1 = [
    "jumping", "singing", "playing", "swimming", "reading", "walking", "talking", 
    "cooking", "running", "skipping", "leaping", "kicking", "flipping", "spinning", 
    "diving", "racing", "darting", "climbing", "sprinting", "crawling", "swaying", 
    "jogging", "pacing", "bolting", "chasing", "gliding", "sliding", "surfing", 
    "skating", "rolling", "swinging", "shooting", "bouncing", "floating", "drifting", 
    "wandering", "searching", "sneaking", "digging", "lifting", "grabbing", "hugging"
]

list_2 = [
    "Pearl", "Cat", "Thor", "Fish", "Plume", "Parot", "Adios", "Slime", "Star", "Girl", 
    "Soaz", "Kratos", "Mars", "Drake", "Zeus", "Boy", "Warrior", "Chef", "Runner", "Flame", 
    "Tear", "Dove", "Dog", "Yuu", "Corgi", "Cow", "Baby", "Buffalo", "Ox", "Helios"
]

def generate_username():
    random.shuffle(list_1)
    random.shuffle(list_2)    
    while True:
        username = f"{list_1.pop()}{list_2.pop()}"        
        if not User.objects.filter(username=username).exists():
            return username