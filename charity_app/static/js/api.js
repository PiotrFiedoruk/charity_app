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
                  '<div class="title" id="org_title">' + element[1] + '</div>'+
                  '<div class="org_subtitle">'+
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
    // get info
    var gift = document.querySelector(".checkboxy:checked")
    console.log(gift);
    var organisation = document.querySelector("#org_title").value
    console.log(organisation);
    var giftBags = document.querySelector("#bags").value
    console.log(giftBags);
    var address = document.querySelector("#address").value
    console.log(address);
    var city = document.querySelector("#city").value
    console.log(city);
    var postcode = document.querySelector("#postcode").value
    console.log(postcode);
    var phone = document.querySelector("#phone").value
    console.log(phone);
    var data = document.getElementsByTagName('data').value
    console.log(data);
    var time = document.querySelectorAll('input[name="time"]').value
    console.log(time);
    var moreInfo = document.querySelectorAll('input[name="more_info"]').value
    console.log(moreInfo);
    // display info

        // document.querySelector(".summary--text").innerHTML = gift + giftBags
        // document.querySelector(".summary--text").innerHTML = organisation
        // document.querySelector("#sum_address ul li:first-child").innerHTML = address
        // document.querySelector("#sum_address ul li:nth-child(2)").innerHTML = city
        // document.querySelector("#sum_address ul li:nth-child(3)").innerHTML = postcode
        // document.querySelector("#sum_date").innerText = data + time

        var summaryList = document.createElement("ul")
        var summaryAddress = document.createElement("li")
        summaryAddress.innerHTML = address
        var summaryCity = document.createElement("li")
        summaryCity.innerHTML = city
        var summaryPostcode = document.createElement("li")
        summaryPostcode.innerHTML = postcode
        var summaryPhone = document.createElement("li")
        summaryPhone.innerHTML = phone
        summaryList.appendChild(summaryAddress)
        summaryList.appendChild(summaryCity)
        summaryList.appendChild(summaryPostcode)
        summaryList.appendChild(summaryPhone)

        var summaryDiv = document.querySelector("#sum_address");
        summaryDiv.appendChild(summaryList)


        



}
document.querySelector(".btn.next-step ");addEventListener("click", ev => {
    summary()
})