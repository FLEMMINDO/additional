def findRestaurant(list1, list2):
    ans = {}
    for i in list1:
        if i in list2 and list1.index(i)+list2.index(i) in ans.keys():
            ans[list1.index(i)+list2.index(i)].append(i)
        elif i in list2:
            ans[list1.index(i)+list2.index(i)] = []
            ans[list1.index(i) + list2.index(i)].append(i)
    return ans[min(ans.keys())]



print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))