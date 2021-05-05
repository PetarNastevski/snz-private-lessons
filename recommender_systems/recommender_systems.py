from math import sqrt


def sim_distance(prefs, person1, person2):
    """
    Враќа мерка за сличност базирана на растојание помеѓу person1 и person2
    :param prefs: речник со оцени од корисници
    :param person1: име на корисник1
    :param person2: име на корисник2
    :return: сличност помеѓу корисник1 и корисник2
    """
    # Се прави листа на заеднички предмети
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    # Ако немаат заеднички рејтинзи, врати 0
    if len(si) == 0:
        return 0
    # Собери ги квадратите на сите разлики
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, p1, p2):
    """
    Го враќа коефициентот на Пирсонова корелација помеѓу p1 и p2 (личност1 и личност 2).
    Вредностите се помеѓу -1 и 1
    :param prefs: речник со оцени од корисници
    :param p1: име на корисник1
    :param p2: име на корисник2
    :return: сличност помеѓу корисник1 и корисник2
    """
    # Се креира речник во кој ќе се чуваат предметите кои се оценети од двајцата
    # Во речникот ни се важни само клучевите за да ги чуваме имињата на филмовите
    # кои се заеднички, а вредностите не ни се важни
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # Се пресметува бројот на предмети оценети од двајцата
    n = len(si)

    # Ако немаат заеднички предмети, врати корелација 0
    if n == 0:
        return 0

    # Собери ги сите оцени за секоја личност посебно
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Собери ги квадратите од сите оцени за секоја личност посебно
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Собери ги производите од оцените на двете личности
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Пресметај го коефициентот на корелација
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    """
    Ги враќа најсличните n корисници за даден корисник.
    :param prefs: речник со оцени од корисници
    :param person: име на корисник
    :param n: број на слични корисници
    :param similarity: метрика за сличност
    :return: листа со најслични n корисници
    """
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    # Се сортира листата во растечки редослед
    scores.sort()
    # Се превртува за најсличните (со најголема вредност) да бидат први
    scores.reverse()
    return scores[0:n]


def get_recommendations(prefs, person, similarity=sim_pearson):
    """
    Ги враќа препораките за даден корисник со користење на тежински просек
    со оцените од другите корисници
    :param prefs: речник со оцени од корисници
    :param person: име на корисник
    :param similarity: метрика за сличност
    :return: препораки за даден корисник
    """
    totals = {}
    simSums = {}
    for other in prefs:
        # За да не се споредува со самиот себе
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # не се земаат предвид резултати <= 0
        if sim <= 0:
            continue
        for item in prefs[other]:
            # за тековниот корисник ги земаме само филмовите што ги нема гледано
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # Сума на сличности
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # Креирање на нормализирана листа со рејтинзи
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Сортирање на листата во растечки редослед. Превртување на листата за најголемите вредности да бидат први
    rankings.sort(reverse=True)

    return rankings


def get_recommendations_item_based(inverted_prefs, person):
    """
    Ги враќа препораките за даден корисник со користење на тежински просек
    со оцените од предметите
    :param inverted_prefs: инвертиран речник со оцени од корисници, item-based
    :param person: име на корисник
    :return: препораки за даден корисник
    """
    similarity_per_item = {}
    person_items = [item for item, values in inverted_prefs.items() if person in values.keys()]
    for item in person_items:
        similar_items = top_matches(inverted_prefs, item, n=None)
        my_rating = inverted_prefs[item][person]
        for similarity, item in similar_items:
            if person in inverted_prefs[item] or similarity <= 0:
                continue
            similarity_per_item.setdefault(item, [])
            similarity_per_item[item].append(similarity * my_rating)

    # Креирање на нормализирана листа со рејтинзи
    similarity_per_item_avg = [(sum(similarity_per_item[item]) / len(similarity_per_item[item]), item) for item in
                               similarity_per_item]
    similarity_per_item_avg.sort(reverse=True)

    return similarity_per_item_avg


def transform_prefs(prefs):
    """
    Ги трансформира рејтинзите така што клучеви ќе бидат филмовите,
    а вредност ќе биде листа со рејтинзи од секој корисник
    :param prefs: речник со оцени од корисници
    :return: инвертиран речник со оцени од корисници
    """
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Замени ги местата на корисникот и предметот
            result[item][person] = prefs[person][item]
    return result