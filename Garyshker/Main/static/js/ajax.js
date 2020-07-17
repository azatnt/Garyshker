$(function() {
    $('#search').keyup(function() {
        var search = $('#search').val();
        if($.trim(search.length) == 0)
        {
          $('#search_results').html('');
        }

        else{
          $.ajax({
          type: 'POST',
          url: '/search/',
          data: {
            'search' : search,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
          },
          success: searchSuccess,
          dataType: 'html',

        });
        }

    });
  });




function searchSuccess(data, textStatus, jqXHR)
{
  $('#search_results').html(data);
}


$(function() {
    $('#search_report').keyup(function() {
        var search_report = $('#search_report').val();
        if($.trim(search_report.length) == 0)
        {
          $('#search_results').html('');
        }

        else{
          $.ajax({
          type: 'POST',
          url: '/search-report/',
          data: {
            'search_report' : search_report,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
          },
          success: searchSuccess,
          dataType: 'html',

        });
        }

    });
  });




function searchSuccess(data, textStatus, jqXHR)
{
  $('#search_results').html(data);
}


//
//
// $(function(){
//   $.ajax({
//       url: 'https://api.instagram.com/v1/users/self/', // если ваше приложение прошло аппрув, вместо self можете указать ID пользователя
//       dataType: 'jsonp',
//       type: 'GET',
//       data: {access_token: 'IGQVJYUHdNQ2xURHg1QlJTV3BQMzRnV1ppT1RqZA1BRWHJZAaGM3bExRQWJnQUxEQVFUZAG5IanFPZAl80N0wxbVhvbkVMOGVYM3VleWpickVkVDZAkTTQwM1FlUnFXRENFbWk5b1lDbVZAZAclFpWnFWZAE11YgZDZD'},
//       success: function(response){
//         $('#insta_count').text(response.data.counts.followed_by); // количество подписчиков
//         // $('#insta_count').text(response.data.counts.follows); // количество подписок
//         // $('#insta_count').text(response.data.counts.media); // количество фото и видео в аккаунте
//       }
//     });
// });
