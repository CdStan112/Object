function createBookCard(book) {
    const bookCard = document.createElement('div');
    bookCard.classList.add('one-book');

    const bookImgDiv = document.createElement('div');
    bookImgDiv.classList.add('book-img');
    const bookImg = document.createElement('img');
    bookImg.src = book.photo_uri;
    bookImg.alt = book.title;
    bookImgDiv.appendChild(bookImg);
    bookCard.appendChild(bookImgDiv);

    const bookInfoDiv = document.createElement('div');
    bookInfoDiv.classList.add('book-info');
    const bookInfoText = document.createElement('p');
    bookInfoText.classList.add('book-info-func');
    bookInfoText.textContent = book.info;
    bookInfoDiv.appendChild(bookInfoText);
    bookCard.appendChild(bookInfoDiv);

    return bookCard;
}

document.getElementById("form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect the checked categories
    let selectedCategories = [];
    let checkboxes = document.getElementsByName("category");
    checkboxes.forEach(function (checkbox) {
        if (checkbox.checked) {
            selectedCategories.push(parseInt(checkbox.value)); // Convert to integer if needed
        }
    });

    // Make an AJAX POST request with the selected category IDs
    fetch("/books", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({category_ids: selectedCategories})
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json(); // Assuming response is JSON
        })
        .then(data => {
            const bookContainer = document.getElementById('books');
            bookContainer.innerHTML = ''; // Clear previous content

            data.forEach(book => {
                const bookCard = createBookCard(book);
                bookContainer.appendChild(bookCard);
            });
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
        });
});

// Fetch categories from the server and dynamically generate checkboxes
fetch("/get_categories")
    .then(response => response.json())
    .then(categories => {
        const form = document.getElementById("check");
        Object.keys(categories).forEach(key => {
            const id = key;
            const name = categories[key];
            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.name = "category";
            checkbox.value = id;
            const label = document.createElement("label");
            label.textContent = name;
            form.appendChild(checkbox);
            form.appendChild(label);
            form.appendChild(document.createElement("br"));
        });
    })
    .catch(error => console.error('Error fetching categories:', error));