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

def create_test_user(user):
    dndmodel.db.session.add(user)
    dndmodel.db.session.commit()


test2=dndmodel.User(email='g@g.com', user_name='brad', password='g3')
tname=dndmodel.Cnamefield(char_name='Jax', background='pirate', alignment='LG', user_id=1)
tabil=dndmodel.Abilities(str=9, dex=10, con=11, int=12, wis=13, cha=12, user_id=1)
tskill=dndmodel.Skills(skill1='climb', skill2='animals', skill3='acrobatics', skill4='diplomacy', skill5='performancy', user_id=1)
tother=dndmodel.Otherstats(proficiency_bonus=5, armor_class=6, hit_points=7, initative=8, speed=9, user_id=1)
aequip=dndmodel.Equipment(armor='leather', weapons='swords', potion='healing', ring='shiny', user_id=1)
tfeat=dndmodel.Feats(feat1='run_fast', fighting_style='bold', user_id=1)

create_test_user(test2)
create_test_user(tname)
create_test_user(tabil)
create_test_user(tskill)
create_test_user(tother)
create_test_user(aequip)
create_test_user(tfeat)
