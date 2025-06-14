from slist import Slist

def my_predicate(x):
    return x%2 == 0

def plus_one(x):
    return x + 1

def get_default_slist():
    x = Slist()
    to_append = [2, 3, -10, -20, 2, 2]
    for data in to_append:
        x.append(data)
    return x, to_append

def test_empty_slist():
    x = Slist()
    assert x.length()                   == 0
    assert x.find(10)                   == -1
    assert x.get(0)                     is None
    assert x.get_last()                 is None
    assert x.remove(0)                  is None
    assert x.find_custom(my_predicate)  is None
    assert x.copy().head                is None

    x.concat(Slist())
    assert x.head                       is None and x.length() == 0

    x.foreach(plus_one)
    assert x.head is None and x.length() == 0

    x.append(1)
    assert x.get(0) == 1
    x.remove(0)

    x.prepend(1)
    assert x.get(0) == 1
    x.remove(0)



def test_length():
    slist, arr = get_default_slist()
    result = len(arr)
    expected = slist.length()
    assert result == expected

    slist = Slist()
    result = slist.length()
    expected = 0
    assert result == expected


def test_get():
    slist, arr = get_default_slist()
    result = [slist.get(i) for i in range(len(arr))]
    expected = arr
    assert result == expected

def test_prepend():
    slist, arr = get_default_slist()
    slist.prepend(100)
    arr.insert(0, 100)

    result = [slist.get(i) for i in range(len(arr))]
    expected = arr
    assert result == expected

def test_apppend():
    slist, arr = get_default_slist()
    slist.append(100)
    arr.append(100)

    result = [slist.get(i) for i in range(len(arr))]
    expected = arr
    assert result == expected

def test_remove():
    slist, arr = get_default_slist()
    result = slist.remove(3)
    expected = arr[3]
    assert result == expected

    result_list = [slist.get(i) for i in range(slist.length())]
    expected_list = [arr[i] for i in range(len(arr)) if i != 3]
    assert result_list == expected_list

def test_get_last():
    slist, arr = get_default_slist()
    result = slist.get_last()
    expected = arr[-1]
    assert result == expected

def test_find():
    slist, arr = get_default_slist()    # [2, 3, -10, -20, 2, 2]
    result = slist.find(2)
    expected = 0
    assert result == expected

def test_remove_first():
    slist, arr = get_default_slist()    # [2, 3, -10, -20, 2, 2]
    slist.remove_first(2)
    result_list = [slist.get(i) for i in range(slist.length())]
    expected_list = arr[1:]
    assert result_list == expected_list

def test_remove_all():
    slist, arr = get_default_slist()  # [2, 3, -10, -20, 2, 2]
    slist.remove_all(2)
    result_list = [slist.get(i) for i in range(slist.length())]
    expected_list = [x for x in arr if x != 2]
    assert result_list == expected_list

def test_copy():
    slist, arr = get_default_slist()
    copied = slist.copy()
    result = [copied.get(i) for i in range(copied.length())]
    expected = [slist.get(i) for i in range(slist.length())]
    assert result == expected

def test_concat():
    slist1, arr1 = get_default_slist()
    slist2, arr2 = get_default_slist()
    slist1.concat(slist2)
    result = [slist1.get(i) for i in range(slist1.length())]
    expected = arr1 + arr2
    assert result == expected

def test_foreach():
    slist, arr = get_default_slist()
    slist.foreach(plus_one)
    expected = [x + 1 for x in arr]
    result = [slist.get(i) for i in range(slist.length())]
    assert result == expected

def test_find_custom():
    def predicate(x):
        return x%2 == 0
    slist, arr = get_default_slist()    # [2, 3, -10, -20, 2, 2]
    expected = (2, 0)
    result = slist.find_custom(predicate)
    assert result == expected
