def countPlace(a, k):
    wifi_places = 1
    house_wifi = 0
    num_of_houses = len(a)

    while num_of_houses > house_wifi:
        wifi_places += 1
        house_wifi = (2 * k + 1) * wifi_places

    return wifi_places


print(countPlace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 , 19, 20], 2))
