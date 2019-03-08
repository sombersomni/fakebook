$(document).ready(function() {
    $(document).on('submit', '#register-form', function(e) {
        e.preventDefault();
        const form = $(this).serialize();
        $.post('/registration', form).done(data => {
            alert("Thank you for registering " + data);
        })
    });

    $(document).on('submit', '#login-form', function(e) {
        e.preventDefault();
        const form = $(this).serialize();
        $.post('/login/check', form).done(response => {
           if(response == "error") {
               alert("Couldn't Login");
           } else {
               console.log("Logged in : " + response);
               window.location.href = "/";
    
           }
        })
    });

    $(document).on('submit', '#post-form', function(e) {
        e.preventDefault();
        const form = $(this).serialize();
        $.post('/postactivity', form).done(response => {
           if(response == "success") {
               window.location.reload();
           } else {
                console.log("couldn't add your post")
           }
        })
    });

    $(document).on('submit', '#settings-form', function(e) {
        e.preventDefault();
        const form = $(this).serialize();
        $.post('/update/settings', form).done(response => {
            console.log(response);
        })
    })

    $(document).on("click", "#logout-link", function(e) {
        e.preventDefault();
        $.get("/logout").done(response => {
            if(response == "success") {
                window.location.href = "/login"
            }
        })
    })
});