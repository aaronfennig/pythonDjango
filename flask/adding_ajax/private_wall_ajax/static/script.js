$("h1").hover(function () {
    // change the text color of all elements with class 'xyz' to blue
    $(".xyz").css("color", "blue");
},
    function () {
        // change the text color of all elements with class 'xyz' to black
        $(".xyz").css("color", "black");
    });

$(document).ready(function(){
    $('.msgForm').submit(function(e){
        e.stopPropagation();
        e.preventDefault();
        var newMessage = $('.msgForm').serialize()
        console.log("*****************", typeof newMessage, newMessage, "********************")
        $.ajax({
            method: "POST",
            url: "/postmessage",
            data: newMessage
        })
        $(".messageInput").val("")
    })
})

$(document).ready(function(){
    $('.delMsg').submit(function(e){
        e.preventDefault();
        $.ajax({
            method: "GET",
            url: "/deletemessage/<messageID>"
        })
        .done(function(res){
            $('#test').html(res)
        })
    })
})