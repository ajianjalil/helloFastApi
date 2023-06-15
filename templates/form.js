document.getElementById("item-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Get form values
    var title = document.getElementById("title").value;
    var rating = parseInt(document.getElementById("rating").value);
    var url = document.getElementById("url").value;
    var price = parseInt(document.getElementById("price").value);
    var customer_id = parseInt(document.getElementById("customer_id").value);
  
    // Create JSON object
    var item = {
      title: title,
      rating: rating,
      url: url,
      time_updated: null,
      id: null,
      price: price,
      time_created: null,
      customer_id: customer_id
    };
  
    // Log the JSON object
    console.log(item);
  
    // Send the JSON object to the server
    // You can use fetch or AJAX to send the data to your API endpoint
    // Example using fetch:
    fetch("/add-item/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(item)
    })
    .then(function(response) {
      if (response.ok) {
        console.log("Item added successfully!");
        // Perform any necessary actions on successful response
      } else {
        throw new Error("Error: " + response.status);
      }
    })
    .catch(function(error) {
      console.error(error);
      // Handle the error appropriately
    });
  });
  