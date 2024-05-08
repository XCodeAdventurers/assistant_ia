
from api.models import Person


def context(request):
    try:
        person = Person.get_auth_person(request.user)
        role = person.get_role()
    except Exception as e:
        print(e)
        role = None
    return {
        "is_account_plan_business": role == 'account_plan_business',
        "is_account_plan_personal":  role == 'account_plan_personal'
    }