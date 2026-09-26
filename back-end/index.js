let express=require('express');
let app=express();
let mongoose=require('mongoose');
let hrRoutes=require('./routes/hr_routes.js');
let empRoutes=require('./routes/emp_routes.js');
//indicating the server incoming json format data
app.use(express.json());

mongoose.connect("mongodb://localhost:27017/hrmanagement").then(()=>{console.log("db conect success")}).catch((err)=>{console.log(err)});

app.use("/api/hr", hrRoutes);
app.use("/api/emp", empRoutes);
//localhost:3000/register
app.post("/register", (req, res) => {
    res.send("register route called");
});
//localhost:3000/viewstudent
app.get("/viewstudent", (req, res) => {
    res.send("view student route called");
});
//run the server
app.listen(3000, () => {
    console.log("Server is running on port 3000");
});