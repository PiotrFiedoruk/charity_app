function show_id(event)
{
    var ids = get_checked_chexboxes();
    var params = new URLSearchParams();
    ids.forEach(id => params.append("type_ids", id))
    var address = '/get_institutions_by_type?'+ params.toString();
    console.log(address);
    // create list of organisations
    fetch(address)
        .then(response => response.json())
        .then(data => data.forEach(element => {
            console.log('hello');
            var divnew = document.createElement("div");
            divnew.className = "form-group form-group--checkbox"
            divnew.innerHTML =
                '<label>'+
                    '<input type="radio" name="organization" value="old"/>'+
                    '<span class="checkbox radio"></span>'+
                    '<span class="description">'+
                  '<div class="title">' + element[1] + '</div>'+
                  '<div class="subtitle">'+
                    element[3] +
                  '</div>' +
                '</span>' +
                '</label>' +
            ''
            var parentDiv = document.getElementById("step-3");
            var childDiv4 = document.getElementById("step3buttons");
            parentDiv.insertBefore(divnew, childDiv4)
        }))

}
function get_checked_chexboxes()
{
    var markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
    var ids = [];
    markedCheckbox.forEach(box => ids.push(box.value));
    console.log(ids);
    return ids;
}


$( document ).ready(function() {
    var li_buttons = $('.checkboxy');
    li_buttons.click(show_id);
});


function categories()
{
    //get elements:
var checkboxes = document.querySelectorAll('input[name="categories"]:checked');
    for (var checkbox of checkboxes) {
        console.log(checkbox.value);

  }
}
categories()

function summary(){
    var gift = document.querySelector(".checkboxy:checked");
    console.log(gifts);
    var giftBags = document.querySelectorAll('input[name="bags"]');
    console.log(giftBags);
    var address = document.querySelectorAll('input[name="address"]');
    console.log(address);
    var data = document.querySelectorAll('input[name="data"]');
    console.log(data);
    var time = document.querySelectorAll('input[name="time"]');
    console.log(time);
    var moreInfo = document.querySelectorAll('input[name="more_info"]');
    console.log(moreInfo);


}