$('.form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

});


$('#btnLogin').click(function() {

    user = {
        'name' : $("#inputName").val(),
        'email' : $("#inputEmail").val(),
        'password' : $("#inputPassword").val(),
    }

    $("#status").html('waiting...');


    $.ajax({
        url: '127.0.0.1:5001/signUp',
        dataType: 'json',
        contentType:'application/json',
        type: 'POST',
        success: function(response) {
            // window.open(response.link, '_self')
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        },
        data: JSON.stringify(user)
    });
});
