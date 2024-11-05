resource null_resource names {
  triggers = {
    trigger = value
  }

  provisioner "local-exec" {
    command = "command"
  }
}
