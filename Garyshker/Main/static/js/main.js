// let BtnChangeProfile = document.querySelector('.btn-change button');
// let UserInfo = document.querySelector('.profile_main .profile');
// let IsEdit = false;
//
// BtnChangeProfile.addEventListener('click', () => {
//   if (UserInfo.style.visibility == 'hidden') {
//       UserInfo.style.visibility == 'visible';
//   }
//   else {
//     UserInfo.style.visibility == 'hidden';
//   }
// })



function show_hide() {
  var click = document.getElementById('profile_update');
  if(click.style.display === 'none') {
    click.style.display = 'block';
  }else{
    click.style.display = 'none';
  }
}

//
// function show_reply() {
//   var click_reply = document.getElementById('reply');
//   if(click_reply.style.display === 'none') {
//     click_reply.style.display = 'block';
//   }else{
//     click_reply.style.display = 'none';
//   }
// }


$(document).ready(function() {
		$('.comment-reply-btn').click(function(event){
			event.preventDefault();
			$(this).parent().next('#comment-reply').fadeToggle();
		})


    $('.comment-btn').click(function(){
  		$('.comment_form').fadeToggle()


  		// return false;

  });


	})
