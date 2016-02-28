$('##signIn').click(function() {

    user = {
        'email' : $("#Email").val(),
        'password' : $("#Passwd").val(),
    }

    $("#status").html('waiting...');


    $.ajax({
        url: 'http://127.0.0.1:5001/login',
        dataType: 'json',
        contentType:'application/json',
        type: 'POST',
        processData: 'false',
        success: function(response) {
            window.open(response.link, '_self')
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        },
        data: JSON.stringify(user)
    });
});
