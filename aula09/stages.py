from datetime import date

STAGES = ["novo"]

def model_leads(name, company, email):
    """modelar e estruturar um lead como um funcionario"""
    return{"name": name,
           "company": company,
           "email": email,
           "stage": "novo",
           "created": date.today().isoformat()
}