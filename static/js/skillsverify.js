"user strict";

let bskill1 = "";
    let bskill2 = "";

    fetch(`/get-bskills.json`)
            .then((response) => response.json())
            .then((responseData) => {
                bskill1 = responseData['bskill1'];
                bskill2 = responseData['bskill2'];
                console.log(bskill1, bskill2)
              })

document.getElementById('skills').addEventListener('submit', evt=>{


    const rskill = document.getElementById('rskill').value
    const cskill1 = document.getElementById('cskill1').value
    const cskill2 = document.getElementById('con').value
        
    const sArray=new Set([rskill, cskill1, cskill2, bskill1, bskill2])
    console.log(sArray)
    if (sArray.size < 5){
        evt.preventDefault();
        alert("each skill must be unique, they can't stack")
    }
})