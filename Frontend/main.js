function validate()
{
    var username=document.getElementById("username").value;
    var password=document.getElementById("pswd").value;

    if(username=="admin" && password=="123")
    {
        alert("Login succesfully");
        location.href="home.html";

    }
    else
    {
        alert("Login failed");
    }

}