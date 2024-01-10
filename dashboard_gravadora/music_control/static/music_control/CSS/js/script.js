$(document).ready(function() {
    var sidebar = $(".sidebar");
    var currentWidth = "20%"; // Defina a largura inicial aqui

    $(".fa-solid.fa-bars").click(function() {
        // aumentar
        if (currentWidth === "5%") {
            sidebar.width("20%");
            currentWidth = "20%";

            $(".sidebar span").css("display", "block");
        // diminuir
        } else if (currentWidth === "20%") {
            sidebar.width("5%");
            currentWidth = "5%";

            $(".sidebar span").css("display", "none");

            $("#login_img").css("padding", "5px");
        }
    });

    $("#spotifyLink").click(function() {
        $("#minhaDiv").load("novoConteudo.html");
        alert(123)

});


});
