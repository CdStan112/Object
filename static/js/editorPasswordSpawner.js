document.addEventListener("DOMContentLoaded", function () {
    const name = document.getElementById("nameEditor");
    const surname = document.getElementById("surnameEditor");
    const mail = document.getElementById("mailEditor");
    const number = document.getElementById("numberEditor");
    const passwordInput = document.getElementById("passwordEditor");
    const passwordRepeatInput = document.getElementById("passwordRepeatEditor");
    const passwordToggle2 = document.getElementById("passwordToggle");
    var container = document.getElementById("insert");

    var divElement = document.createElement("div");
    divElement.textContent = "Большой фрагмент HTML-кода";


    passwordToggle2.addEventListener("click", function (event) {

        if (passwordInput.value === "" || passwordRepeatInput.value === "" || passwordInput.value !== passwordRepeatInput.value) {
            passwordInput.style.border = '2px solid red';
            passwordRepeatInput.style.border = '2px solid red';
        } else {
            passwordInput.style.border = '2px solid green';
            passwordRepeatInput.style.border = '2px solid green';

            if (name.validity.valid && surname.validity.valid && mail.validity.valid && number.validity.valid && passwordInput.validity.valid && passwordRepeatInput.validity.valid) {
                container.appendChild(divElement);
            }
        }
    });
});
