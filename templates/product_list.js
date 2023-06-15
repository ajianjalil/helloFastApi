document.addEventListener("DOMContentLoaded", function () {
    fetch("/items")
        .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Error: " + response.status);
            }
        })
        .then(function (data) {
            console.log("DATA recieved:", data);
            // var items = data.list;
            var listContainer = document.querySelector("#items-list");
            // console.log(items);
            data.forEach(function (item) {

                html_element = elementFromHtml(`
                <div class="item">
                    <img class="thumbnail" src="path/to/thumbnail.jpg" alt="Item Thumbnail">
                    <span class="name">Item Name</span>
                    <span class="price">$99.99</span>
                </div>
                `);

                const thumbnail = html_element.querySelector('.thumbnail');
                thumbnail.src = item.url;

                // Change the 'alt' attribute of the image
                thumbnail.alt = 'New Item Thumbnail';

                // Change the text content of the name span
                const nameSpan = html_element.querySelector('.name');
                nameSpan.textContent = item.title

                // Change the text content of the price span
                const priceSpan = html_element.querySelector('.price');
                priceSpan.textContent = item.price

                console.log(item.price);
                listContainer.appendChild(html_element);
            });
        })
        .catch(function (error) {
            console.error(error);
        });


});


function elementFromHtml(html) {
    const template = document.createElement('template');
    template.innerHTML = html.trim();
    return template.content.firstElementChild;
}