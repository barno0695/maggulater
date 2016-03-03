
$('#btnLogin').click(function(e) {
    e.preventDefault();
    user = {
        'email' : $("#inputEmail").val(),
        'password' : $("#inputPassword").val(),
    }

    console.log(user);

    fetch('http://127.0.0.1:5000/login', {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    }).then(function(response){
        console.log(response.headers.get('Content-Type'))
        console.log(response.headers.get('Date'))
        console.log(response.status)
        console.log(response.statusText)
        console.log(response)
        window.location = response.url
    })
});
