$('#btnLogin').click(function() {

    user = {
        email : $("#inputEmail").val(),
        password : $("#inputPassword").val(),
    }

    $("#status").html('waiting...');

    $.ajax({
        url: 'http://127.0.0.1:5000/login',
        dataType: 'json',
        type: 'POST',
        success: function(response) {
            window.location.replace(response);
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        },
        data: user
    });
});
