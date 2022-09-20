import os

SERVICES = ["account-management-service",
            "alerts-service",
            "analyzer-service",
            "asset-manager",
            "assets-graph-service",
            "bitbucket-app",
            "crypto-service",
            "feature-flags-service",
            "github-app",
            "gitlab-app",
            "jenkins-app",
            "jenkins-state-manager",
            "jobs-service",
            "notifications-service",
            "ppe-engine",
            "scanners-agent-service",
            "scanners-policy-service",
            "scanners-results-analyzation-service",
            "scanners-service",
            "scm-apps-manager",
            "scm-integrations",
            "secrets-service",
            "web-api",
            "web-api-service",
            "workflows-service"]

for service in SERVICES:
    repo_name = f"cidersecurity/{service}"
    commands = [f"terraform import 'module.ecr[\"{service}\"].aws_ecr_repository.this' {repo_name}",
                f"terraform import 'module.ecr[\"{service}\"].aws_ecr_repository_policy.ecr_policy[0]' {repo_name}"]
    for c in commands:
        os.system(c)
