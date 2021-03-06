$(function() {
    $("#login-button .glyphicon").hide();
});

function loginWithVIDChain () {
    $("#login-button .glyphicon").show();

    var callback  = "http://localhost:8080/university_backend/student_profile.html";
    var requester = 1; // ID from MYSQL table to identify the requester and set the callback
    var userInfo  = ["name", "email", "phone", "photo"];

    var data = {
        "callback": callback,
        "requester": requester,
        "userinfo": userInfo
    };

    $.ajax({
        type: "POST",
        url: "http://localhost:8080/vidchain/login1.php",
        processData: false,
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: onLoginSucceed
    });
}

function onLoginSucceed (data) {
    if (data.id) {
        eModal.iframe(
            {
                
                title:'ViDChain Sign in',
                url: "http://localhost:8080/vidchain/login2.php?p="+data.id,
                size:"lg"
            }
        );
        $("#login-button .glyphicon").hide();
    } else {
        console.error('Error');
    }
}



