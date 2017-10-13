function doAjaxPost(form_id, btn, url){
  $(btn).click(function(){
    var data =$(function() {formData2Json(form_id)});
    alert(JSON.stringify(data))
    $(form_id).attr('action', url);
    $.ajax({
      url: url,
      method: "POST",
      dataType: "json",
      data: JSON.stringify(data),//.serialize()),
      contentType: 'application/json;charset=UTF-8'
}).done(function( msg ) {
  alert( "Data Saved: " + msg );
});
  })
}

  /* ajax call GET*/
  function doGet(btn, url){
       $(btn).click(function(e){
           e.preventDefault();
           $.get(url).done(function(data){
            console.log(data)
           })
         })
        }

/* redirect to page */
function doRedirect(form_id, btn, url){
     $(btn).click(function(e){
       $(form_id).attr('action', url)
         })
       }

/* Convert form data to JSON */
function formData2Json(form_id){
       var formArray = $(form_id).serializeArray();
       console.log(formArray)
               $('input[disabled]').each( function() {
                   //formInput = formInput + '&' + $(this).attr('name') + '=' + $(this).val();
                   formArray.push($(clickid).val());
               });
         var jsonObj = {};
         $.each(formArray,
             function(i, v) {
                 jsonObj[v.name] = v.value;
             });
             return jsonObj;
}
