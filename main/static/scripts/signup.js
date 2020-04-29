function validateForm(formId)
    {
        var empt = document.forms["svalidation"]["suser"].value;
        if (empt==null || empt=="")
        {
            alert("Name is empty");
            return false;
        }
        var empt = document.forms["svalidation"]["semail"].value;
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

console.log("signup")