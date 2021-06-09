$("h1").hover(function () {
    // change the text color of all elements with class 'xyz' to blue
    $(".xyz").css("color", "blue");
},
    function () {
        // change the text color of all elements with class 'xyz' to black
        $(".xyz").css("color", "black");
    });