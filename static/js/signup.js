// var photoDataUrl = ""
// function previewFile() {
//   var preview = document.querySelector('#profile-pic');
//   var file    = document.querySelector('#image').files[0];
//   var reader  = new FileReader();
//
//   reader.onloadend = function () {
//     preview.src = reader.result;
//   }
//
//   if (file) {
//     console.log(reader.readAsDataURL(file))
//     photoDataUrl = reader.readAsDataURL(file);
//   } else {
//     preview.src = "";
//   }
// }



$('#btnSignUp').click(function() {

	// console.log($("input[name=inputUserType]:checked").val());
	var flag = 0;
	if($("input[name=inputUserType]:checked").val() === "student") flag = 1;
	else if($("input[name=inputUserType]:checked").val() === "faculty") flag = 2;
    user = {
        'name' : $("#inputName").val(),
        'email' : $("#inputEmail").val(),
        'password' : $("#inputPassword").val(),
		'dob' : $("#inputDOB").val(),
        'flag' : flag
    }

    console.log(user);

    $("#status").html('waiting...');

    $.ajax({
        url: 'http://127.0.0.1:5000/signUp',
        dataType: 'json',
        contentType:'application/json',
        type: 'POST',
        success: function(response) {
            console.log("user added");
        },
        error: function(error) {
            console.log(error);
        },
        data: JSON.stringify(user)
    });
});
