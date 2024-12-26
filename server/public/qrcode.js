
const socket = io.connect('/');

socket.on('status', (data) => {
    console.log(data);
    updateStatus(data);
});

start();
function start() {
    fetch("/secretCode", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    }).then(res => {
        return res.json();

    }).then(data => {
        console.log(data);
        
    });
}

function updateStatus(status) {
    //document.getElementById("status").innerHTML = "";
    let number = status.randomnumber;
    let state = status.state;
    let motorEnabled = status.motorEnabled;
    let queue = status.queue;
    let totalOrders = status.totalOrders;

    let randomp = document.getElementById("random");
    randomp.innerHTML = number;

    let motorEnabledp = document.getElementById("motorEnabled");
    motorEnabledp.innerHTML = motorEnabled;
    motorEnabledp.style.backgroundColor = motorEnabled ? "green" : "red";

    let totalOrdersp = document.getElementById("totalOrders");
    totalOrdersp.innerHTML = totalOrders;
}