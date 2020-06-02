def alternatingSums(a):
    result = []
    weight_team1 = 0
    weight_team2 = 0

    for index in range(len(a)):
        if index % 2 == 0 :
            weight_team1 += a[index]
        else:
            weight_team2 += a[index]
    result.append(weight_team1)
    result.append(weight_team2)

    return result


print(alternatingSums([50, 60, 60, 45, 70]))