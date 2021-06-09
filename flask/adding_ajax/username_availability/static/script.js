$("h1").hover(function () {
    // change the text color of all elements with class 'xyz' to blue
    $(".xyz").css("color", "blue");
},
    function () {
        // change the text color of all elements with class 'xyz' to black
        $(".xyz").css("color", "black");
    });

$(document).ready(function(){
    $('#emailInput').keyup(function(){
        var data = $("#regForm").serialize()
        console.log("***********",typeof data, data, "*****************")
        $.ajax({
            method: "POST",
            url: "/isemailindb",
            data: data
        })
        .done(function(res){
            $('#userNameMsg').html(res)
        })
    })
})

$(document).ready(function(){
    $('#nameInput').keyup(function(){
        var suggestion = $('#searchForm').serialize()
        console.log("***********",typeof suggestion, suggestion, "*****************")
        $.ajax({
            method: "GET",
            url: "/usersearch",
            data: suggestion
        })
        .done(function(res){
            $('#suggestions').html(res)
        })
    })
})


