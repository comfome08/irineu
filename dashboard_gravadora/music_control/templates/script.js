document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.querySelector(".sidebar");
    var currentWidth = "20%"; // Defina a largura inicial aqui

    document.querySelector(".fa-solid.fa-bars").onclick = function() {
        //aumentar
        if (currentWidth === "5%") {
            sidebar.style.width = "20%";
            currentWidth = "20%";

            var spansNaSidebar2 = document.querySelectorAll(".sidebar span");
            spansNaSidebar2.forEach(function(span){
                span.style.display = "block";
            });
        //diminuir
        } else if (currentWidth === "20%") {
            sidebar.style.width = "5%";
            currentWidth = "5%";

            var spansNaSidebar = document.querySelectorAll(".sidebar span");
            spansNaSidebar.forEach(function(span) {
                span.style.display = "none";
            });

            var login_img = document.getElementById("login_img");
            login_img.style.padding= "5px";

        }
    };
});
