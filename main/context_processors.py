APP_NAME = "Ao Eleven"
STUDENT_NAME = "Andi Hakim Himawan"

def global_context(request):
    return {
        "app_name": APP_NAME,
        "student_name": STUDENT_NAME,
    }
