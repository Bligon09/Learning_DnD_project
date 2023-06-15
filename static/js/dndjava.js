"user strict";

const emailField = document.getElementById('create-email')

emailField.addEventListener('change', function(evt) {


    const emailInput = evt.target.value

    const correctInput=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/

    const isMatching= correctInput.test(emailInput)
    console.log(isMatching)

    if (isMatching===false){
        document.getElementById('email-message').innerText="Not a valid input"

    }else{

        document.getElementById('email-message').innerText=""

        fetch(`/verify-email.json/${emailInput}`)
            .then((response) => response.json())
            // .then(alert); how to get the data from here and post it to the html like above

    };

})

