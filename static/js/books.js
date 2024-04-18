function appendBookItem(bookData) {
    // Create a new div element for the book item
    let bookItemDiv = document.createElement('div');
    bookItemDiv.classList.add('books-by-category-item');

    // Create the HTML structure for the book item
    bookItemDiv.innerHTML = `
    <a href="/book?id=${encodeURIComponent(bookData.id)}">
        <ul class="all3thingsAgain">
            <li class="books-by-category-item-img-border">
                <img src="${bookData.photo_uri}" alt="${bookData.id}">
            </li>
            <li class="books-by-category-item-name">${bookData.title}</li>
            <li class="books-by-category-item-author">${bookData.author}</li>
        </ul>
    `;
    return bookItemDiv;
}

function fetchBooksByCategoryAndString(ids, queryString) {
    // Make an AJAX POST request with the selected category IDs
    fetch("/books", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            category_ids: ids,
            query: queryString
        })
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json(); // Assuming response is JSON
        })
        .then(data => {
            const bookContainer = document.querySelector('.books-by-category');
            bookContainer.innerHTML = ''; // Clear previous content

            data.forEach(book => {
                const bookCard = appendBookItem(book);
                bookContainer.appendChild(bookCard);
            });
        })
        .catch(error => {
            console.error("There was a problem with the fetch operation:", error);
        });
}

const updateSelectedBooks = function (event) {
    event.preventDefault(); // Prevent the default form submission

    let form = document.getElementById('form');
    let checkboxes = form.querySelectorAll('.category-genre-chekbox');
    let checkedIndices = [];
    checkboxes.forEach(function (checkbox, index) {
        if (checkbox.checked) {
            checkedIndices.push(index + 1);
        }
    });
    fetchBooksByCategoryAndString(checkedIndices, '')
}

document.querySelectorAll('.category-genre-chekbox').forEach((box) => {
    box.addEventListener("change", updateSelectedBooks)
});

search = document.querySelector('.input-find-book-name')
search.addEventListener("submit", (event) => {
    event.preventDefault()

    let queryInput = document.querySelector('.input-text-book-name')
    let form = document.getElementById('form');
    let checkboxes = form.querySelectorAll('.category-genre-chekbox');
    let checkedIndices = [];
    checkboxes.forEach(function (checkbox, index) {
        if (checkbox.checked) {
            checkedIndices.push(index + 1);
        }
    });

    fetchBooksByCategoryAndString(checkedIndices, queryInput.value.trim())
})

fetchBooksByCategoryAndString([], '')