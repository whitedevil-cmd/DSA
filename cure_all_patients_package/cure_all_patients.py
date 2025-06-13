def cure_all_patients(vaccines, patients):
    vaccines.sort()
    patients.sort()
    if len(vaccines) == len(patients):
        for i in range(len(vaccines)):
            if vaccines[i] <= patients[i]:
                return "No"
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    vaccines = list(map(int, input("Enter vaccine values: ").strip().split()))
    patients = list(map(int, input("Enter patient's values: ").strip().split()))
    print(cure_all_patients(vaccines, patients))
