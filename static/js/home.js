
function valide() {
  let name = $("#fname").val()
  let email = $("#email").val()
  let number = $("#number").val()
  let dics = $("#dics").val()

  if (name == "") {

    swal({
      title: "Error ",
      text: "Enter you Name😊",
      icon: "success",
      button: "done",
    })
  }
  else if (email == "") {

    swal({
      title: "Error ",
      text: "Enter you Email😒",
      icon: "success",
      button: "done",
    })
  }
  else if (email.indexOf('@') <= 0) {

    swal({
      title: "Error ",
      text: "Invalid Email 😑",
      icon: "success",
      button: "done",
    })
  }
  else if (email.charAt(email.length - 4) != '.') {
    swal({
      title: "Error ",
      text: "Invalid Email 😑",
      icon: "success",
      button: "done",
    })
  }

  else if (number == "") {

    swal({
      title: "Error ",
      text: "Enter you Number 😒",
      icon: "success",
      button: "done",
    })
  }
  else if (number.length != 10) {

    swal({
      title: "Error ",
      text: "Invalide Number 😑",
      icon: "success",
      button: "done",
    })
  }
  else {

    $.ajax({
      type: "post",
      url: "/contact-us",
      data: {
        h_name: name,
        h_email: email,
        h_number: number,
        mss: dics,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
      }, success: function (res) {
        swal({
          title: "Wellcome ",
          text: "Form Submited successfully",
          icon: "success",
          button: "done",
        })
      }

    })
  }
}

