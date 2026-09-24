const form = document.getElementById("predictionForm");

const priceElement = document.getElementById("price");


form.addEventListener("submit", async function(event) {

    // Stop page from refreshing
    event.preventDefault();


    // Get values from HTML inputs
    const area = Number(
        document.getElementById("area").value
    );

    const bedrooms = Number(
        document.getElementById("bedrooms").value
    );

    const bathrooms = Number(
        document.getElementById("bathrooms").value
    );

    const stories = Number(
        document.getElementById("stories").value
    );

    const parking = Number(
        document.getElementById("parking").value
    );


    // Create data object
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
            "http://127.0.0.1:8000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(houseData)
            }
        );


        // Convert response into JSON
        const result = await response.json();


        // Display predicted price
        priceElement.textContent =
            "₹ " + result.predicted_price.toLocaleString("en-IN");


    } catch (error) {

        console.error(error);

        priceElement.textContent =
            "Error connecting to server";

    }

});