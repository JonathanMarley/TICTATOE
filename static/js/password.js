function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var showPasswordIcon = document.querySelector(".show-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordIcon.src = "./img/ojo1.png";
    } else {
        passwordInput.type = "password";
        showPasswordIcon.src = "../img/ojo.png";
    }
}


function togglePasswordVisibility2() {
    var passwordInput = document.getElementById("confirmarContrasena");
    var showPasswordIcon = document.querySelector(".show-password2");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        showPasswordIcon.src = "../img/ojo1.png";
    } else {
        passwordInput.type = "password";
        showPasswordIcon.src = "../img/ojo.png";
    }
}
