var btn = document.getElementById('redirection')
var downloadFile = 'files/downloadfiles/test.zip'
btn.addEventListener("click", function(){
    window.open(downloadFile, '_blank');
  
    //il est la le truc a la con okASJd li
    window.location.href = "thanksfordownload.html";
})