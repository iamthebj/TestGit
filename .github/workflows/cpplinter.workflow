workflow "C++ Lint" {
  on = "pull_request"
  resolves = ["lint-action"]
}

action "lint-action" {
  uses = "CyberZHG@github-action-python-lint@master"
}
