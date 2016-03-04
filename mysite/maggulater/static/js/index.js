var working = false;
$('.login').on('submit', function(e) {
    e.preventDefault();
    if (working) return;
    working = true;
    var $this = $(this),
    $state = $this.find('button > .state');
    $this.addClass('loading');
    $state.html('Authenticating');

    user = {
        'email' : $("#inputEmail").val(),
        'password' : $("#inputPassword").val(),
    }

    console.log(user);

    fetch('http://127.0.0.1:8000/login/', {
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
        $this.addClass('ok');
        $state.html('Welcome back!');
        window.location = response.url
    })
    setTimeout(function() {
        // $this.addClass('ok');
        // $state.html('Welcome back!');
        console.log("error");
    }, 10000);
});
