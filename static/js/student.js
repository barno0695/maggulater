$('#courses').click(function() {

    $.ajax({
        url: 'http://127.0.0.1:5000/allcourses',
        contentType:'application/json',
        type: 'GET',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        },
    });
});
