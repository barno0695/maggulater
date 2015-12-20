
$('#btnSignUp').click(function() {

    // var myfile = document.getElementById('image').files[0];
    // var fr = new FileReader();
    // var user;
    // fr.onload = function(event) {
    //     var data = event.target.result.replace("data:"+ myfile.type +";base64,", '');

    // }
    // fr.readAsDataURL(myfile);
    user = {
        name : $("#inputName").val(),
        email : $("#inputEmail").val(),
        password : $("#inputPassword").val(),
        flag : "1"
    }

    $("#status").html('waiting...');

    $.ajax({
        url: 'http://127.0.0.1:5000/user',
        dataType: 'json',
        type: 'POST',
        success: function(response) {
            console.log("user added");
        },
        error: function(error) {
            console.log(error);
        },
        data: user
    });
});

function getBase64Image(imgElem) {
// imgElem must be on the same server otherwise a cross-origin error will be thrown "SECURITY_ERR: DOM Exception 18"
var canvas = document.createElement("canvas");
canvas.width = imgElem.clientWidth;
canvas.height = imgElem.clientHeight;
var ctx = canvas.getContext("2d");
ctx.drawImage(imgElem, 0, 0);
var dataURL = canvas.toDataURL("image/png");
return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
}


// function uploadFile() {
//     blobFile = $('#filechooser')[0].files[0]);
//     var fd = new FormData();
//     fd.append("fileToUpload", blobFile);

//     $.ajax({
//        url: "upload.php",
//        type: "POST",
//        data: fd,
//        processData: false,
//        contentType: false,
//        success: function(response) {
//            // .. do something
//        },
//        error: function(jqXHR, textStatus, errorMessage) {
//            console.log(errorMessage); // Optional
//        }
//     });
// }