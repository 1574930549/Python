
def load_data_set():
    """
    加载示例数据集
    返回:
        数据集：事务列表。每个事务都包含若干项。
    """
    data_set = [[11,12,13],[11,14],[14,15],[11,12,14],[11,12,16,14,13],[12,16,13],[12,13,16]]
    return data_set


def create_C1(data_set):
    """
    通过扫描数据集创建频繁候选1项集C1。
    参数：
    数据集：事务的列表。每个事务都包含若干项。
    返回：
    C1：包含所有频繁候选1项集的集合
    """
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


def is_apriori(Ck_item, Lksub1):
    """
    判断频繁候选k项集是否满足先验性质。
    参数：
        Ck_item:Ck中的一个常见候选k项集，包含所有频繁的候选k项集。
        Lksub1: :Lk-1，包含所有频繁候选（k-1）-项集的集合。
    返回:
        True: 满足先验属性。
        False: 不满足先验属性。
    """
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


def create_Ck(Lksub1, k):
    """
    通过Lk-1自己的连接操作创建包含所有频繁候选k项集的Ck集。
    参数:
        Lksub1: Lk-1，包含所有频繁候选（k-1）-项集的集合。
        k: 频繁项集的项号。
    返回:
        Ck: 包含所有频繁候选k项集的集合
    """
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    """
    通过从Ck执行删除策略来生成Lk。
    参数:
        data_set: 交易记录列表。每个事务都包含若干项。
        Ck: 包含所有频繁候选k项集的集合。
        min_support: 最小support。
        support_data: 一个字典。键是frequentitemset，值是support。
    返回:
        Lk: 包含所有频繁k项集的集合。
    """
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


def generate_L(data_set, k, min_support):
    """
    生成所有频繁项集。
    参数:
        data_set: 事务列表。每个事务都包含若干项。
        k: 所有频繁项集的最大项数。
        min_support: 最小support。
    返回:
        L: Lk的列表。
        support_data: 一个字典。键是frequentitemset，值是support。
    """
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):
    """
    从频繁项集生成大规则。
    参数:
        L: Lk的列表。
        support_data: 一个字典。键是frequentitemset，值是support。
        min_conf: 最小的 confidence.
    返回:
        big_rule_list: 包含所有大规则的列表。每个大规则都表示为一个3元组。
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=3, min_support=0.2)
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.7)
    for Lk in L:
        print("="*50)
        print ("频繁 " + str(len(list(Lk)[0])) + "-项集\t\t\t\t支持度")
        print( "="*50)
        for freq_set in Lk:
            print (freq_set, support_data[freq_set])
    print()
    print ("大规则")
    for item in big_rules_list:
        print (item[0], "=>", item[1], "conf: ", item[2])