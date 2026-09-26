let express = require('express');
let router = express.Router();
let {users}=require('../models/users')
router.get("/viewemployees", async (req, res) => {
    let result=await users.find();
    res.send(result);
});
//open postman choose get method
//localhost:3000/hr/viewemployees

router.delete("/deleteemployee/:id", async (req, res) => {
    let deleterec = await users.findByIdAndDelete(req.params.id);
    if (deleterec) {
        res.send("employee deleted");
    }
});

router.post("/assign-task", (req, res) => {
    res.send("assign task route called");
});
module.exports = router;