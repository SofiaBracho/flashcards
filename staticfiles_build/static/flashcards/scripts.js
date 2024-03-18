addEventListener("DOMContentLoaded", (event) => {
    function getToken(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0,name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
        }
        return cookieValue;
    }
    var csrftoken = getToken('csrftoken')

    const flipBtn = document.getElementById('flip-btn')
    const card = document.getElementById('card')
    const wordEn = document.getElementById('word-en')
    const wordEs = document.getElementById('word-es')
    const profOpt = document.getElementById('proficiency-options')
    const btnLearned = document.getElementById('btn-learned')
    const btnPractice = document.getElementById('btn-more-practice')
    const btnNextPage = document.getElementById('next-page')

    // Flip card
    flipBtn.addEventListener('click', () => {
        card.classList.add('flip')
        setTimeout(() => {
            wordEn.style.display = 'none'
            flipBtn.style.display = 'none'
            wordEs.style.display = 'block'
            profOpt.style.display = 'block'
        }, 125);
    })

    // API fetch call to mark word as learned
    btnLearned.addEventListener('click', handleProficiency)

    // API fetch call to mark word as need more practice
    btnPractice.addEventListener('click', handleProficiency)

    // ------------------

    function handleProficiency(e) {

        let proficiency = null;
        if (e.target == btnLearned) { // Learned
            proficiency = 1
        } else if (e.target == btnPractice) { // Need practica
            proficiency = 0
        }
        let card_id = e.target.parentElement.parentElement.parentElement.dataset.id

        let data = {
            proficiency: proficiency,
            card_id: card_id
        }

        // var url = `http://127.0.0.1:8000/set_proficiency`
        var url = window.location.origin + "/set_proficiency/"
        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            }, 
            body:JSON.stringify(data) //JavaScript object of data to POST
        })
        .then((response) => {
            // console.log(response)
            return response.json(); //converts response to json
        })
        .then((data) => {
            console.log('data:',data)
            if(data.result == 'success') {
                //Perform actions with the response data from the view
                if (proficiency == 1) {
                    // Disable the other button
                    btnPractice.disabled=true
                } 
                else if (proficiency == 0) {
                    // Disable the other button
                    btnLearned.disabled=true
                }
                setTimeout(() => {
                    location.reload();
                }, 1000);
            }
        });
    }

});