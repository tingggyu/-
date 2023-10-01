const inputElement = document.getElementById('textInput');

// 监听输入框的变化事件
inputElement.addEventListener('input', function () {
  const inputValue = inputElement.value; // 获取输入框的内容
  sendDataToBackend(inputValue); // 将内容发送到后台
});

// 向后台发送数据的函数，你可以根据你的需求自行实现
function sendDataToBackend(data) {
  // 使用 XMLHttpRequest、Fetch API 或其他适当的方式发送数据到后台
  // 这里只是一个简单的示例
  fetch('/name_search', {
    method: 'POST',
    body: JSON.stringify({ data: data }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(responseData => {
    // 在这里处理后台返回的数据
    console.log(responseData);
  })
  .catch(error => {
    console.error('发送数据时出错：', error);
  });
}