$(document).ready(function(){

	//clicking search icon changes view to main map view
    $('.glyphicon-search').click(function() {
        window.location = "SafeStay.html";
    });

    //hitting enter key will hit search icon
    $("#enter-city").keyup(function(event){
    if(event.keyCode == 13){
        $(".glyphicon-search").click();
    }
});

});
