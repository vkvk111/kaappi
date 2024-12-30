

function order() {
    let number = prompt("Enter secret number:");
    console.log(number);

    // send post req to server
    fetch('/order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number: number }),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if(data.success) {
                console.log("Order successful!");
                document.getElementById("Order").style.display = "none";
                let afterOrder = document.getElementById("afterOrder");
                afterOrder.style.display = "block";

                let orderNumber = document.getElementById("orderNumber");
                orderNumber.innerText = data.totalOrders;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}