p1 = [(-1, 1), (10, 0)]
p2 = [(2, 3), (1, 2), (5, 1)]


def multiply(p1, p2):
    result = []
    for term_1 in p1:
        for term_2 in p2:
            new_cof = term_1[0] * term_2[0]
            new_pow = term_1[1] + term_2[1]
            new_term = (new_cof, new_pow)
            result.append(new_term)
    return result


print(multiply(p1, p2))


def addition_cach1(p1, p2):
    """
    cách khác là tạo set chứa số mũ trong kết quả rồi với mỗi 1 số mũ đấy nếu nó
    tồn tại ở p1 và p2 thì cộng conf chỉ tồn tại ở 1 cái thì add vào 
    set-pow() --> list --> sort [4,3,2,1] số mũ có rồi thì chỉ duyệt từng
    đa thức để cộng dồn vào [(0,4),(0,3)(0,2)(0,1)] 
    --> tạo 1 inđex 4 vị trí 0, 3 vị trí 1...(nâng cao)
    -->dùng hàm for :
    for term in p1 + p2:
        for re_term in result :
            if term[1] == re_term[1]
                re_term[0] += term[0]
    """
    result_add = []
    for term1 in p1:
        find = False
        for term2 in p2:
            if term1[1] == term2[1]:
                new_cof = term1[0] + term2[0]
                find = True
        if not find:
            new_cof = term1[0]
        new_term = [new_cof, term1[1]]
        result_add.append(new_term)

    for term2 in p2:
        find_p2 = False
        for term1 in p1:
            if term2[1] == term1[1]:
                find_p2 = True
                break
        if not find_p2:
            result_add.append(term2)
    return result_add


print(addition_cach1(p1, p2))


def adition_cach2(p1, p2):
    """
    p1 = [(-1, 1), (10, 0)]
    p2 = [(2, 3), (1, 2), (5, 1)]
    """
    sort_lst = []
    for term in p1 + p2:
        if [0, term[1]] not in sort_lst:
            new_term_4_sort = [0, term[1]]
            sort_lst.append(new_term_4_sort)
    for new_term_4_sort in sort_lst:
        for term in p1 + p2:
            if new_term_4_sort[1] == term[1]:
                new_term_4_sort[0] += term[0]
    return sort_lst


print(adition_cach2(p1, p2))
