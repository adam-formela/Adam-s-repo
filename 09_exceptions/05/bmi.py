def calculate_bmi(weight, height):
    return round(weight / height ** 2, 2)

def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi < 25:
        return "norma"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"

def get_bmi_value(w, h):
    bmi_result = calculate_bmi(w, h)
    bmi_status = get_state(bmi_result)
    return bmi_status

if __name__ == "__main__":
    # --- reszta skrypu
    # pyta uzytkownika
    result = get_bmi_value(56, 1.6)
    print('Twoje BMI ->', result)