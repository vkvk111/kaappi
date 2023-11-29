
const express = require('express');
const path = require('path');
const bodyParser = require("body-parser");
const fs = require("fs");
const cookieParser = require('cookie-parser');
const { exec } = require('child_process');



const app = express();

app.set('view engine', 'ejs');

app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(__dirname)); //security issue
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

const server = app.listen(27015, () =>{
    console.log("Started on port 80")
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

    let steps = req.body.steps;
    let speed = 500;
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

    let steps = req.body.steps;
    let speed = 500;
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