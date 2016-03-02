// $('#courses').click(function() {
//
//     $.ajax({
//         url: 'http://127.0.0.1:5000/allcourses',
//         contentType:'application/json',
//         type: 'GET',
//         success: function(response) {
//             console.log(response);
//         },
//         error: function(error) {
//             console.log(error);
//         },
//     });
// // });
// var result = fetch('http://127.0.0.1:5000/allcourses', {
//   method: 'post',
//   headers: {
//     'Accept': 'application/json',
//     'Content-Type': 'application/json'
//   },
//   body: JSON.stringify({
//     email: 'test@gmail.com',
//     password: 'test',
//   })
// })
//
// console.log(result);

var result = fetch('http://127.0.0.1:5000/allcourses').then(function(response) {
  console.log(response.headers.get('Content-Type'))
  console.log(response.headers.get('Date'))
  console.log(response.status)
  console.log(response.statusText)
})


console.log(result);
