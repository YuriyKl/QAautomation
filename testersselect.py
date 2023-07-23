# #!/usr/bin/python3

# testers = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10]
testers = ["Roma", "Vlad", "Artem", "Vova","Pavlo", "Dasha","Andriy", "Bogdan", "Tymophiy", "Oleg","Dima","Oleksiy"]
# test_design_writers = [2, 3, 5,9]
test_design_writers = ["Roma", "Vlad", "Artem", "Vova", "Pavlo", "Dasha", "Andriy", "Bogdan", "Tymophiy", "Oleg"]
# scripters = [3, 4, 5, 6, 7, 8,9,10]
scripters = ["Roma", "Vlad", "Vova", "Bogdan", "Tymophiy", "Dima", "Oleksiy"]
# reviewers = [1, 2, 3, 5,6 9, 10]
reviewers = ["Roma", "Vlad", "Dima","Oleksiy"]
# out_of_office_today = [4, 5, 6, 8]
out_of_office_today = ["Dasha", "Tymophiy", "Dima", "Oleg","Vlad", "Roma",'Pavlo']


testers2 = testers.copy()
testers2.sort()
test_design_writers2 = test_design_writers.copy()
test_design_writers2.sort()
scripters2 = scripters.copy()
scripters2.sort()
reviewers2 = reviewers.copy()
reviewers2.sort()
out_of_office_today2 = out_of_office_today.copy()
out_of_office_today2.sort()

print(f"list of test disign writers are {test_design_writers2}")
print(f"list of testers which can wright scripts {scripters2}")
print(f"list of testers which performing code review {reviewers2}")
print(f"list of testers which are OOO today {out_of_office_today2}")
print(f"list of testers are {testers2}")

scripters_set = set(scripters2)-set(test_design_writers2)
scripters_only = list(scripters_set)
scripters_only.sort()
print(f"list of scrypters are {scripters_only}")

testers_in_office_set = set(testers2)-set(out_of_office_today2)
testers_in_office = list(testers_in_office_set)
testers_in_office.sort()
print(f"list of testers in office are {testers_in_office}")

script_review_qa = list(set(scripters2)&set(reviewers2)&testers_in_office_set)
script_review_qa.sort()
print(script_review_qa)




