"user strict";

document.getElementById('ability-scores').addEventListener('submit', evt=>{

    const strAtt = document.getElementById('str').value
    const dexAtt = document.getElementById('dex').value
    const conAtt = document.getElementById('con').value
    const intAtt = document.getElementById('int').value
    const wisAtt = document.getElementById('wis').value
    const chaAtt = document.getElementById('cha').value

    const abilScore= new Set([strAtt, dexAtt, conAtt, intAtt, wisAtt, chaAtt])

        if (abilScore.size < 6){
            evt.preventDefault();
            alert("you must select different scores for the abilities, and different bonus.")
        }

    const abonus1 = document.getElementById('abonus1')
    const abonus2 = document.getElementById('abonus2')

    const abilBonus = new Set([abonus1, abonus2])

    if (abilBonus.size < 2){

        evt.preventDefault();
        alert("you must select different scores for the abilities, and different bonus.")
    }


} )

