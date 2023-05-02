// Get the "Contact Us" link element
var contactLink = document.getElementById("contact-link");

// Add a click event listener to the link
contactLink.addEventListener("click", function(event) {
  // Prevent the link from navigating to a new page
  event.preventDefault();

  // Create a new window with the contact details
  var contactWindow = window.open("", "Contact Us", "width=400,height=300");

  // Set the HTML content of the new window
  contactWindow.document.write("<h2>Contact Us</h2>");
  contactWindow.document.write("<p>Phone: 123-456-7890</p>");
  contactWindow.document.write("<p>Email: info@example.com</p>");
});
