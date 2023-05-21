
document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = {
    name: document.querySelector('input[name="name"]').value,
    email: document.querySelector('input[name="email"]').value,
    phone: document.querySelector('input[name="phone"]').value
    };

    const requestOptions = {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
    };

    fetch("/request_a_call_back", requestOptions)
    .then(response => response.json())
    .then(data => {
        console.log("Response:", data);
        alert("adder customer successfully")
        document.getElementById("form").reset();
        // Handle the response as needed
    })
    .catch(error => {
        console.error("Error:", error);
        // Handle errors
    });
});
