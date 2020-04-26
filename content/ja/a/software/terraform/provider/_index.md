---
title: "Providers"
linkTitle: "Providers"
description: >
  https://www.terraform.io/docs/providers/
date: 2020-04-26T23:19:47+09:00
simple_list: true
weight: 400
---

## HTTP

https://www.terraform.io/docs/providers/http/

### http Data Source

https://www.terraform.io/docs/providers/http/data_source.html

SYNOPSIS:

```HCL
data "http" "example" {
  url = "https://checkpoint-api.hashicorp.com/v1/check/terraform"

  # Optional request headers
  request_headers = {
    "Accept" = "application/json"
  }
}
```

curlで取ってくるようなデータはこれを使えばいい。

参考:

- [TerraformでJSONを扱う方法 - Qiita](https://qiita.com/tshohe/items/81e46e516ef4559dd32d)
- [Getting my own Public IP : Terraform](https://www.reddit.com/r/Terraform/comments/9g62ox/getting_my_own_public_ip/)

## Random

https://www.terraform.io/docs/providers/random/

乱数値の生成などで使える。  
生成した値はtfstateに保存され、生成時のパラメータが変わらない限り都度、生成することはない。

Resources:

- [random_id](https://www.terraform.io/docs/providers/random/r/id.html)
- :

## Template

https://www.terraform.io/docs/providers/template/

Example:

```HCL
# Template for initial configuration bash script
data "template_file" "init" {
  template = "${file("init.tpl")}"

  vars {
    consul_address = "${aws_instance.consul.private_ip}"
  }
}

# Create a web server
resource "aws_instance" "web" {
  # ...

  user_data = "${data.template_file.init.rendered}"
}
```

## Child Pages（他のProviders）