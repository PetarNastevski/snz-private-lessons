import math
import re


def get_words(doc):
    """Поделба на документот на зборови. Стрингот се дели на зборови според
    празните места и интерпукциските знаци

    :param doc: документ
    :type doc: str
    :return: множество со зборовите кои се појавуваат во дадениот документ
    :rtype: set(str)
    """
    # подели го документот на зборови и конвертирај ги во мали букви
    # па потоа стави ги во резултатот ако нивната должина е >2 и <20
    words = list()
    for word in re.split('\\W+', doc):
        if 2 < len(word) < 20:
            words.append(word.lower())
    return words


def get_vocabulary(documents):
    """Враќа множество од сите зборови кои се појавуваат во документите.

    :param documents: листа со документи
    :type documents: list(str)
    :return: множество зборови
    :rtype: set(str)
    """
    vocab = set()
    for doc_text in documents:
        words = get_words(doc_text)
        words_set = set(words)
        vocab.update(words_set)
    return sorted(vocab)


def cosine(v1, v2):
    """Ја враќа косинусната сличност помеѓу два вектори v1 и v2.

    :param v1: вектор1
    :type v1: list(float)
    :param v2: вектор2
    :type v2: list(float)
    :return: сличност помеѓу вектор и вектор2
    :rtype: float
    """
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / math.sqrt(sumxx * sumyy)


def pearson(v1, v2):
    """ Го враќа коефициентот на Пирсонова корелација помеѓу два вектори v1 и v2.

    :param v1: вектор1
     :type v1: list(float)
    :param v2: вектор2
    :type v2: list(float)
    :return: сличност помеѓу вектор и вектор2
    :rtype: float
    """
    sum1 = 0
    sum2 = 0
    sum1Sq = 0
    sum2Sq = 0
    pSum = 0
    n = len(v1)
    for i in range(n):
        x1 = v1[i]
        x2 = v2[i]
        sum1 += x1
        sum1Sq += x1 ** 2
        sum2 += x2
        sum2Sq += x2 ** 2
        pSum += x1 * x2
    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sum1Sq - sum1 ** 2 / n) * (sum2Sq - sum2 ** 2 / n))
    if den == 0: return 0
    r = num / den
    return r


def calculate_document_frequencies(documents):
    """Враќа речник со број на појавување на зборовите.

    :param documents: листа со документи
    :type documents: list(str)
    :return: речник со број на појавување на зборовите
    :rtype: dict(str, int)
    """
    df = {}
    documents_words = []
    for doc_text in documents:
        words = get_words(doc_text)
        documents_words.append(words)
        words_set = set(words)
        for word in words_set:
            df.setdefault(word, 0)
            df[word] += 1
    return df


def calc_vector(cur_tf_idf, vocab):
    """Пресметува tf-idf вектор за даден документ од дадениот вокабулар.

    :param cur_tf_idf: речник со tf-idf тежини
    :type cur_tf_idf: dict(str, float)
    :param vocab: множество од сите зборови кои се појавуваат во барем еден документ
    :type vocab: set(str)
    :return: tf-idf вектор за дадениот документ
    """
    vec = []
    for word in vocab:
        tf_idf = cur_tf_idf.get(word, 0)
        vec.append(tf_idf)
    return vec


def process_document(doc, df, N, vocab):
    """Пресметува tf-idf за даден документ.

    :param doc: документ
    :type doc: str
    :param df: речник со фреквенции на зборовите во дадениот документ
    :type df: dict(str, int)
    :param N: вкупен број на документи
    :param vocab: множество од сите зборови кои се појавуваат во барем еден документ
    :type vocab: set(str)
    :return: tf-idf вектор за дадениот документ
    """
    if isinstance(doc, str):
        words = get_words(doc)
    else:
        words = doc
    idf = {}
    for word, cdf in df.items():
        idf[word] = math.log(N / cdf)
    f = {}  # колку пати се јавува секој збор во овој документ
    for word in words:
        f.setdefault(word, 0)
        f[word] += 1
    max_f = max(f.values())  # колку пати се појавува најчестиот збор во овој документ
    tf_idf = {}
    for word, cnt in f.items():
        ctf = cnt * 1.0 / max_f
        tf_idf[word] = ctf * idf.get(word, 0)
    vec = calc_vector(tf_idf, vocab)
    return vec


def rank_documents(doc, documents, sim_func=cosine):
    """Враќа најслични документи со дадениот документ.

    :param doc: документ
    :type doc: str
    :param documents: листа со документи
    :type documents: list(str)
    :param sim_func: функција за сличност
    :return: листа со најслични документи
    """
    df = calculate_document_frequencies(documents)
    N = len(documents)
    vocab = get_vocabulary(documents)
    doc_vectors = []
    for document in documents:
        vec = process_document(document, df, N, vocab)
        doc_vectors.append(vec)
    query_vec = process_document(doc, df, N, vocab)
    similarities = []
    for i, doc_vec in enumerate(doc_vectors):
        dist = sim_func(query_vec, doc_vec)
        similarities.append((dist, i))
    similarities.sort(reverse=True)
    return similarities


def create_dataset(documents, labels):
    """Формира податочно множество со tf-idf тежини и класи, соодветно за класификација со дрва на одлука.

    :param documents: листа со документи
    :type documents: list(str)
    :param labels: листа со класи
    :type labels: list
    :return: податочно множество со tf-idf тежини и класи, речник со френвенции на појавување на зборовите,
            број на документи во множеството, вокабулар од даденото множество на аборови
    :rtype: list(list), dict(str, int), int, set(word)
    """
    dataset = []
    doc_vectors = []
    df = calculate_document_frequencies(documents)
    N = len(documents)
    vocab = get_vocabulary(documents)
    for document in documents:
        vec = process_document(document, df, N, vocab)
        doc_vectors.append(vec)
    for doc_vec, label in zip(doc_vectors, labels):
        doc_vec.append(label)
        dataset.append(doc_vec)
    return dataset, df, N, vocab
