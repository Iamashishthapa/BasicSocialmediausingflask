function validateForm(formId)
    {
        var empt = document.forms["newpost"]["title"].value;
        if (empt==null || empt=="")
        {
            alert("Name is empty");
            return false;
        }
        var empt = document.forms["newpost"]["content"].value;
        if (empt==null || empt=="")
        {
            alert("Email is empty");
            return false;
        }
        var empt = document.forms["svalidation"]["spw"].value;
        if (empt==null || empt=="")
        {
            alert("Password is empty");
            return false;
        }
    }

console.log("newpost")

