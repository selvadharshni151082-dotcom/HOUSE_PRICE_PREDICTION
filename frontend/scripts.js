// Get the form
const form = document.getElementById("predictionForm");


// Get the price display element
const priceElement = document.getElementById("price");


// When the form is submitted
form.addEventListener("submit", async function(event) {

    // Prevent page refresh
    event.preventDefault();


    // Get area
    const area = Number(
        document.getElementById("area").value
    );


    // Get bedrooms
    const bedrooms = Number(
        document.getElementById("bedrooms").value
    );


    // Get bathrooms
    const bathrooms = Number(
        document.getElementById("bathrooms").value
    );


    // Get stories
    const stories = Number(
        document.getElementById("stories").value
    );


    // Get parking
    const parking = Number(
        document.getElementById("parking").value
    );


    // Create house data object
    const houseData = {

        area: area,

        bedrooms: bedrooms,

        bathrooms: bathrooms,

        stories: stories,

        parking: parking
    };


    try {

        // Send data to FastAPI
        const response = await fetch(
            "/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(houseData)
            }
        );


        // Convert response to JSON
        const result = await response.json();


        // Display predicted price
        priceElement.textContent =
            "₹ " +
            result.predicted_price.toLocaleString("en-IN");


    } catch (error) {

        // Display error
        console.error(error);

        priceElement.textContent =
            "Error connecting to server";

    }

});