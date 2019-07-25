$("document").ready(function(){
    alert("This is really funny");
   //Initialize the cart liabrary
   CartJS.init({{ cart | json }});


});

$(document).ready(function(){
    alert("The page just loaded in jsmain.js")
});
