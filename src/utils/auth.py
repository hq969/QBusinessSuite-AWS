def check_access(role, resource):
    if role == "Admin": return True
    return resource in ["Salesforce", "Redshift"]
