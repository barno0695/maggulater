$('#btnLogin').click(function() {

    user = {
        'email' : $("#inputEmail").val(),
        'password' : $("#inputPassword").val(),
    }

        console.log(user);

    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        dataType: 'json',
        contentType:'application/json',
        type: 'POST',
        processData: 'false',
        success: function(response) {
            var data = JSON.parse(response)
            window.location.href = data.link;
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        },
        data: JSON.stringify(user)
    });
});
