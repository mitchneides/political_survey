# function takes 2 lists and compares their values at indexes
# returns comparison list


def compare_two_score_lists(user_list, party_list):
    comparison_list = []
    for c, value in enumerate(user_list):
        if int(value) == int(party_list[c]):
            comparison_list.append(1)
        elif int(value) > 0 and int(party_list[c]) > 0 or int(value) < 0 and int(party_list[c]) < 0:
            comparison_list.append(0.5)
        else:
            comparison_list.append(0)
    sum_of_list = 0
    for num in comparison_list:
        sum_of_list += num
    return sum_of_list


def sort_tuple(tup):
    lst = len(tup)
    for i in range(0, lst):

        for j in range(0, lst - i - 1):
            if tup[j][1] < tup[j + 1][1]:
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

