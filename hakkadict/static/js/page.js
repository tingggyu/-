//var $temp_input;

(function () {
  'use strict';

  // 拖拉特殊符號小鍵盤
  $(".keyboard").draggable({ handle: ".draggable-header" });

  // 辭典搜尋選項變更特殊符號小鍵盤
  $("input[name='settingRadioOptions']").on('click', function() {
    $(".keyboard").fadeIn();
    if ($(this).val() == 2) {
      $(".keyboard").fadeOut();
    }
  });

  // 放大圖片取得動態替換圖檔
  $('#imgModal').on('show.bs.modal', function(e) {
    var imgName = $(e.relatedTarget).data('img-name');
    $(e.currentTarget).find('.content > img').attr('src', 'http://127.0.0.1:8000/static/images/result/' + imgName);
  });
})();

// 輸入特殊符號小鍵盤
function keyinto(input){
  if ($(".keyword") != undefined) {
    var temp_inputVal = $(".keyword").val();
    temp_inputVal = temp_inputVal + input;
    $(".keyword").val(temp_inputVal).focus();
  }
}

