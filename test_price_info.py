import price_info as pInfo

def test_total_cost_shopping():
    pList = {'apple' : 1, 'banana' : 2, 'coconut' : 3}
    qList = {'apple' : 2, 'banana' : 4, 'coconut' : 6}

    result = pInfo.total_cost_shopping(pList, qList)

    assert (result == 28)

def test_cost_of_fruit():
    check = 0
    pList = {'apple' : 1, 'banana' : 2, 'coconut' : 3}
    qList = {'apple' : 2, 'banana' : 4, 'coconut' : 6}
    cost_list = {'apple' : 2, 'banana' : 8, 'coconut' : 18}
    
    for key in pList.keys():
        if check == 0:
            if key in qList:
                cost = pList[key]*qList[key]
                if cost != cost_list[key]:
                    check = 1
    assert (check == 0)

#hello