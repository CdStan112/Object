document.addEventListener("DOMContentLoaded", function() {
    var savePasswordLink = document.getElementById("savePasswordLink");
    var table = document.querySelector(".editor-table-user-profile");
    var footer = document.querySelector(".editor-footer");

    savePasswordLink.addEventListener("click", function(event) {
        event.preventDefault(); // Предотвращаем переход по ссылке

        // Удаление добавленных строк пароля
        var passwordRow = table.querySelector("#passwordRow");
        var repeatPasswordRow = table.querySelector("#repeatPasswordRow");


        if (passwordRow && repeatPasswordRow) {
            table.removeChild(passwordRow);
            table.removeChild(repeatPasswordRow);
        }

        // Отправка запроса на сервер
        // Здесь вы можете добавить код для отправки данных на сервер

        // Скрытие футера
        footer.classList.add("editor-footer-hidden");
    });
});