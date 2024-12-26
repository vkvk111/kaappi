
const express = require('express');
const path = require('path');
const bodyParser = require("body-parser");
const fs = require("fs");
const cookieParser = require('cookie-parser');
const { exec } = require('child_process');
const QRCode = require('qrcode');
const socketio = require('socket.io');
const { create } = require('domain');


const app = express();

app.set('view engine', 'ejs');

app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(__dirname)); //security issue
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());


//security variables
//changes after order is placed
let randomNumber = Math.max(parseInt(Math.random()*100)-1, 0);

const ip = "192.168.1.113" //change to your ip address
//global state variables
let motorEnabled = false;
let state = 0;
let queue = [];
let totalOrders = 0;


//status object
let status = {randomnumber: randomNumber, state: state, motorEnabled: motorEnabled, queue: queue, totalOrders: totalOrders}; //other data here to be displayed on the main page //qrcode




const server = app.listen(80, () =>{
    console.log("Started on port 80\nhttp://" + ip + "/scanned");
})

const io = socketio(server);

io.on('connection', (socket) => {
    console.log('New connection');
    socket.emit("status", status);
})

app.get("/", (req,res) => {
    res.sendFile(path.join(__dirname,"/public/home.html"));
})

app.get("/admin", (req,res) => {
    res.sendFile(__dirname+"/admin/adminhome.html");
})

app.get("/admin/manualControl", (req,res) => {
    res.sendFile(path.join(__dirname,"/admin/manualControl.html"));
})

app.post("/moveUp", (req, res) => {
    console.log("moveUp");
    let steps = req.body.steps;
    let speed = 400;
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 1 1 ' + steps + ' ' + speed , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.post("/moveDown", (req, res) => {
    console.log("moveDown");
    let steps = req.body.steps;
    let speed = 400;
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 1 2 ' + steps + ' ' + speed , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.post("/zero", (req, res) => {
    console.log("zero");
        const dirname = __dirname.split("server")[0];
        exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 1 0' , (err, stdout, stderr) => {
            if (err) {
                // node couldn't execute the command
                console.log(err);
                return;
            }

            // the *entire* stdout and stderr (buffered)
            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        });
        res.send("OK");
        res.end();
    })

app.post("/solenoid", (req, res) => {
    console.log("solenoid");
    let solenoid = req.body.solenoid;
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 2 ' + solenoid , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.post("/disableMotor", (req, res) => {
    console.log("disableMotor");
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 1 3' , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.post("/enableMotor", (req, res) => {
    console.log("enableMotor");
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 1 4' , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.post("/testProtocol", (req, res) => {
    console.log("testProtocol");
    const dirname = __dirname.split("server")[0];
    exec('python ' + path.join(dirname,'/Vending_machine/command.py') + ' 3 0' , (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            console.log(err);
            return;
        }

        // the *entire* stdout and stderr (buffered)
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    res.send("OK");
    res.end();
})

app.get("/qrcode", (req,res) => {
    //generate qrcode with random number and save it to public folder
    let url = "http://" + ip + "/scanned";

    QRCode.toFile(path.join(__dirname,"public/qrcode.png"), url, {
        color: {
            dark: '#123',  // Blue dots
            light: '#0000' // Transparent background
        }
    }, function (err) {
        if (err) throw err
    })
    res.sendFile(path.join(__dirname,"/public/qrcode.html"));
})

app.post("/secretCode", (req,res) => {
    res.json(randomNumber);
})


app.get("/scanned", (req,res) => {
    res.sendFile(path.join(__dirname,"/public/order.html"));
    console.log("scanned");
    createOrder();
})


function createOrder(){
    //create order
    let order = {
        orderNumber: randomNumber,
        state: 0,
        date: new Date()
    }
    //add order to queue
    queue.push(order);
    //update status
    status.queue = queue;
    //update random number
    randomNumber = Math.max(parseInt(Math.random()*100)-1, 0);
    //update status
    status.randomnumber = randomNumber;
    //increase total orders
    totalOrders++;
    //update status
    status.totalOrders = totalOrders;
    //emit status to all clients
    io.sockets.emit("status", status);
}
