"""Script to seed database."""

import os
import json

import dndcrud
import dndmodel 
import dndserver

os.system('dropdb dnd-learn')
os.system('createdb dnd-learn')

dndmodel.connect_to_db(dndserver.app)
dndmodel.db.create_all()

def add_and_commit(info):
    dndmodel.db.session.add(info)
    dndmodel.db.session.commit()


test2=dndmodel.User(email='g@g.com', user_name='brad', password='g3')
tname=dndmodel.Cnamefield(char_name='Jax', background='pirate', alignment='LG', user_id=1)
tabil=dndmodel.Abilities(str=9, dex=10, con=11, int=12, wis=13, cha=12, user_id=1)
tskill=dndmodel.Skills(skill1='climb', skill2='animals', skill3='acrobatics', skill4='diplomacy', skill5='performancy', user_id=1)
tother=dndmodel.Otherstats(proficiency_bonus=5, armor_class=6, hit_points=7, initiative=8, speed=9, user_id=1)
aequip=dndmodel.Equipment(option1='leather', option2='swords', option3='healing', option4='shiny', user_id=1)
tfeat=dndmodel.Feats(feat='run_fast', fighting_style='bold', user_id=1)

add_and_commit(test2)
add_and_commit(tname)
add_and_commit(tabil)
add_and_commit(tskill)
add_and_commit(tother)
add_and_commit(aequip)
add_and_commit(tfeat)
