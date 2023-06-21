"user strict";

// const emailField = document.getElementById('create-email')

// emailField.addEventListener('change', function(evt) {


//     const emailInput = evt.target.value

//     const correctInput=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/

//     const isMatching= correctInput.test(emailInput)
//     console.log(isMatching)

//     if (isMatching===false){
//         document.getElementById('email-message').innerText="Not a valid input"

//     }else{

//         document.getElementById('email-message').innerText=""

//         fetch(`/verify-email.json/${emailInput}`)
//             .then((response) => response.json())
//             .then((responseData) => {
//                 document.getElementById('email-message').innerText = responseData['checked email'];
//               })


//     };

// })


// const strAtt = document.getElementById('str')
// const dexAtt = document.getElementById('dex')
// const conAtt = document.getElementById('con')
// const intAtt = document.getElementById('int')
// const wisAtt = document.getElementById('wis')
// const chaAtt = document.getElementById('cha')

// const abilScore= [strAtt, dexAtt, conAtt, intAtt, wisAtt, chaAtt]

// const abonus1 = document.getElementById('abonus1')
// const abonus2 = document.getElementById('abonus2')

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
            alert("test is working")
        }

    // const abonus1 = document.getElementById('abonus1')
    // const abonus2 = document.getElementById('abonus2')

    // const abilBonus = new Set([abonus1, abonus2])

    // if (abilBonus.length < 2){

    //     evt.preventDefault();
    // }


} )

