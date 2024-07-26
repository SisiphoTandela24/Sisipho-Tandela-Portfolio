var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(tabname) {
    for (var tablink of tablinks) {
        tablink.classList.remove("active-link");
    }
    for (var tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}

function sendEmail() {
    emailjs.sendForm("sisipho.tandela@capaciti.org.za", "sisipho.tandela@capaciti.org.za", "#contact-form")
      .then(function(response) {
        console.log("Email sent successfully!", response);
      })
      .fail(function(error) {
        console.log("Error sending email:", error);
      });
  }

