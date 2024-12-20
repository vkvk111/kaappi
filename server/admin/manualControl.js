

var input = document.getElementById("consoleForm");


var previousInputs = [];
var commandIndex = -1;

// Execute a function when the user presses a key on the keyboard
input.addEventListener("keydown", function(event) {
    // If the user presses the "Enter" key on the keyboard

    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        sendCommand(input);
    }else if(event.key === "ArrowUp"){
        if(previousInputs.length > 0){
            commandIndex++;
            if(commandIndex >= previousInputs.length){
                commandIndex = 0;
            }
            input.command.value = previousInputs[commandIndex];
        }
    }else if(event.key === "ArrowDown"){
        if(previousInputs.length > 0){
            commandIndex--;
            if(commandIndex < 0){
                commandIndex = previousInputs.length-1;
            }
            input.command.value = previousInputs[commandIndex];
        }
    }
});

function moveUp(steps){
    if(steps > 0 && steps < 2000) {
        let data = {steps: steps};
        fetch("/moveUp", {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            },
            redirect: "follow",
            referrerPolicy: "no-referrer",
            body: JSON.stringify(data),
        }).then(function (e) {
            console.log("SENT DATA");
        })

    }else{
        console.log("Error: No value set.");
    }
}

function moveDown(steps){
    if(steps > 0 && steps < 2000) {
        let data = {steps: steps};
        fetch("/moveDown", {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            },
            redirect: "follow",
            referrerPolicy: "no-referrer",
            body: JSON.stringify(data),
        }).then(function (e) {
            console.log("SENT DATA");
        })
}}

function zero(){
    fetch("/zero", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    }).then(function (e) {
        console.log("SENT DATA");
    })
}

function solenoid(n){
    let data = {solenoid: n};
    fetch("/solenoid", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
    }).then(function (e) {
        console.log("SENT DATA");
    })
}

function enableMotor(){
    fetch("/enableMotor", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    }).then(function (e) {
        console.log("SENT DATA");
    })
}

function disableMotor(){
    fetch("/disableMotor", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    }).then(function (e) {
        console.log("SENT DATA");
    })
}

function testProtocol(){
    fetch("/testProtocol", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    }).then(function (e) {
        console.log("SENT DATA");
    })
}

function sendCommand(commandForm){
    commandIndex = -1;
    switch (commandForm.command.value.trim()){
        case "":
            console.log("No input.");
            break;
        case "zero":
            zero();
            break;
        default:
            console.log("INVALID COMMAND");
    }
    previousInputs.unshift(commandForm.command.value);
    console.log(commandForm.command.value);
    commandForm.command.value = "";
}