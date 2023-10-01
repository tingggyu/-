(function () {
  'use strict';

  // TOP
  $('body').append('<a href="#top" id="topBtn" class="topBtn">TOP</a>');
  $(window).on('scroll', function () {
    if ($(this).scrollTop() > 100) { $('#topBtn').fadeIn(); } else { $('#topBtn').fadeOut(); }
  });
  $('#topBtn').click(function () {
    $('html').animate({ scrollTop: 0 }, 400);
    return false;
  });

  // 側邊選單
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
  });

})();

// 設定字體大小
function fontSize(n) {
  $('body').removeClass('size0 size1 size2');
  $('nav').find('.font-sizing button').removeClass('active');
  $('body').addClass('size' + n);
  $('nav').find('.size' + n).addClass('active');
}

// 播放音檔
function playAudio(audioNameStr) {

  // 將字串轉成 array 並去掉 "--"
  var tmp = audioNameStr.split(",").filter((s) => s !== "--")

  var audio_list = tmp.map((audio) => "http://127.0.0.1:8000/static/audio/audio" + audio + ".mp3")

  handPlay(audio_list)
}

function handPlay(audio_list) {

  var my_audio = new Audio()

  my_audio.preload = false
  my_audio.controls = true
  my_audio.hidden = true

  var src = audio_list.shift()

  my_audio.src = src

  my_audio.play()
  my_audio.addEventListener("ended", playEndedHandler, false)


  document.getElementById('audio_div').appendChild(my_audio)

  my_audio.loop = false

  function playEndedHandler() {
    src = audio_list.shift()
    my_audio.src = src
    my_audio.play()
  }
}
