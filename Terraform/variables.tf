variable "resource_group_name" {
  type        = string
  description = "required"
  default = "udacity-devops-p2"
}

variable "location" {
  type        = string
  description = "required"
  default = "East US"
}

variable "app_service_plan_name" {
  type = string
  description = "required"
  default = "asp-udacity-devops-p2"
}

variable "service_plan_sku" {
  type = string
  description = "required"
  default = "F1"
}

variable "web_app_name" {
  type = string
  description = "required"
  default = "wa-udacity-devops-p2"
}