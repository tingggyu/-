const userInput = document.getElementById('my_input');
const Inputbtn = document.getElementById('search_button');
// 監聽輸入框的鍵盤事件
let isEditing = false;
var resultdata;
userInput.addEventListener('input', function() {
    isEditing = true;
});

userInput.addEventListener('keyup', function(event) {
    if (event.keyCode === 13 && !isEditing) {
        const inputContent = userInput.value;
        if (inputContent) {
            post_solr();
        }
    }
    isEditing = false;  // Reset the editing state
});


Inputbtn.addEventListener('click', function() {
    const inputContent = userInput.value;
    if (inputContent) {
        post_solr();
    }
});


function post_solr() {
    $.ajax({
        url: "/solr_search/",
        type: "POST",
        dataType: "json",
        data:{
          "keyword":document.getElementById('my_input').value
        },
        success: function(data){
            console.log(data);
          resultdata = data;
          temp='';
          for(var i=0 ; i<data.length ;i++ )  {
            temp +=' <div class="card bg-warning bg-gradient bg-opacity-10 my-3">';
            temp +=' <div class="card-body">';
            temp +='<h5 class="card-title"><a href="#" title="檔案名稱（不含附檔名）">'
            temp +=data[i]['file_name'];
            temp +='</a></h5>';
            temp +='<p>';
            temp +=data[i]['file_content'];            
            temp +='</p></div></div>';
          } 
          updatePagination(1);
        }
    });
}


function updatePagination(currentPage){
  temp="";          
  var totalPages = Math.ceil(resultdata.length/5);
  temp = '';
  temp +=' <ul class="pagination flex-wrap justify-content-center">';
  if(currentPage== 1){
      temp +=' <li class="page-item disabled">';
  }
  else{
      temp +=' <li class="page-item">';
  }
  temp +='<a class="page-link" onclick="updatePagination('
  temp +=currentPage-1;

  temp += ')" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a>';
  temp +=' </li>';
  var sart_page = currentPage-4;
  var  max_page = currentPage+5;
  if(sart_page<=0){
      sart_page=1;
      max_page = 10
  }
  for(var i=sart_page; i <= max_page;i++){
      if(i>totalPages){
          break;
      }
      if(i == currentPage){
          temp+=' <li class="page-item active">';
      }
      else{
          temp+='  <li class="page-item">';
      }
      temp +='<a class="page-link" onclick="updatePagination('
      temp +=i;
      temp += ')">';
      temp+=i;
      temp+='</a></li>';
  }
  if(currentPage == totalPages){
      temp +=' <li class="page-item disabled">';
  }
  else{
      temp +=' <li class="page-item">';
  }
  temp+= '<a class="page-link" onclick="updatePagination(';
  temp +=currentPage+1;
  temp += ')" aria-label="Next"><span aria-hidden="true">&raquo;</span></a>';
  temp+=' </li> </ul>'
  $('#Pagination1').html(temp);
  temp='';
  for(var i=(currentPage-1)*5  ; i<resultdata.length && i< currentPage*5;i++ )  {
    temp +=' <div class="card bg-warning bg-gradient bg-opacity-10 my-3">';
    temp +=' <div class="card-body">';
    temp +='<h5 class="card-title"><a href="#" title="檔案名稱（不含附檔名）"';
    temp += 'onclick="download_resource(\'' + resultdata[i]['file_path'] + '\')">';  
    temp +=resultdata[i]['file_name'];
    temp +='</a></h5>';
    temp +='<p>';
    temp +=resultdata[i]['file_content'];            
    temp +='</p></div></div>';
  } 
  $('#result').html(temp);
}