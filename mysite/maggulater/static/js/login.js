

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
    // var csrftoken = getCookie('csrftoken');

    // fetch('/login/', {
    //     method: 'post',
    //     headers: {
    //         'Accept': 'application/json',
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(user)
    // }).then(function(response){
    //     console.log(response.headers.get('Content-Type'))
    //     console.log(response.headers.get('Date'))
    //     console.log(response.status)
    //     console.log(response.statusText)
    //     console.log(response)
    //     $this.addClass('ok');
    //     $state.html('Welcome back!');
    //     window.location = response.url
    // })
    $.ajax({
        url: '/login/',
        // dataType: 'application/json',
        // contentType:'application/json',
        type: 'POST',
        data: JSON.stringify(user),
        success: function(response) {
            console.log("user added");
        },
        error: function(error) {
            console.log(error);
        },
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }

    })
    setTimeout(function() {
        // $this.addClass('ok');
        // $state.html('Welcome back!');
        console.log("error");
    }, 10000);
});
