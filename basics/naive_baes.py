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
    words = set()
    for word in re.split('\\W+', doc):
        if 2 < len(word) < 20:
            words.add(word.lower())
    return words


class DocumentClassifier:
    def __init__(self, get_features):
        # број на парови атрибут/категорија (feature/category)
        self.feature_counts_per_category = {}
        # број на документи во секоја категорија
        self.category_counts = {}
        # функција за добивање на атрибутите (зборовите) во документот
        self.get_features = get_features

    def increment_feature_counts_per_category(self, current_feature, current_category):
        """Зголемување на бројот на парови атрибут/категорија

        :param current_feature: даден атрибут
        :param current_category: дадена категорија
        :return: None
        """
        self.feature_counts_per_category.setdefault(current_feature, {})
        self.feature_counts_per_category[current_feature].setdefault(current_category, 0)
        self.feature_counts_per_category[current_feature][current_category] += 1

    def increment_category_counts(self, cat):
        """Зголемување на бројот на предмети (документи) во категорија

        :param cat: категорија
        :return: None
        """
        self.category_counts.setdefault(cat, 0)
        self.category_counts[cat] += 1

    def get_feature_counts_per_category(self, current_feature, current_category):
        """Добивање на бројот колку пати одреден атрибут се има појавено во
        одредена категорија

        :param current_feature: атрибут
        :param current_category: категорија
        :return: None
        """
        if current_feature in self.feature_counts_per_category \
                and current_category in self.feature_counts_per_category[current_feature]:
            return float(self.feature_counts_per_category[current_feature][current_category])
        return 0.0

    def get_category_count(self, current_category):
        """Добивање на бројот на предмети (документи) во категорија

        :param current_category: категорија
        :return: број на предмети (документи)
        """
        if current_category in self.category_counts:
            return float(self.category_counts[current_category])
        return 0

    def get_total_count(self):
        """Добивање на вкупниот број на предмети"""
        return sum(self.category_counts.values())

    def categories(self):
        """Добивање на листа на сите категории"""
        return self.category_counts.keys()

    def train(self, item, current_category):
        """Тренирање на класификаторот. Новиот предмет (документ)

        :param item: нов предмет (документ)
        :param current_category: категорија
        :return: None
        """
        # Се земаат атрибутите (зборовите) во предметот (документот)
        features = self.get_features(item)
        # Се зголемува бројот на секој атрибут во оваа категорија
        for current_feature in features:
            self.increment_feature_counts_per_category(current_feature, current_category)

        # Се зголемува бројот на предмети (документи) во оваа категорија
        self.increment_category_counts(current_category)

    def get_feature_per_category_probability(self, current_feature, current_category):
        """Веројатноста е вкупниот број на пати кога даден атрибут f (збор) се појавил во
        дадена категорија поделено со вкупниот број на предмети (документи) во категоријата

        :param current_feature: атрибут
        :param current_category: карактеристика
        :return: веројатност на појавување
        """
        if self.get_category_count(current_category) == 0:
            return 0
        return self.get_feature_counts_per_category(current_feature, current_category) \
               / self.get_category_count(current_category)

    def weighted_probability(self, current_feature, current_category, prf, weight=1.0, ap=0.5):
        """Пресметка на тежински усогласената веројатност

        :param current_feature: атрибут
        :param current_category: категорија
        :param prf: функција за пресметување на основната веројатност
        :param weight: тежина
        :param ap: претпоставена веројатност
        :return: тежински усогласена веројатност
        """
        # Пресметај ја основната веројатност
        basic_prob = prf(current_feature, current_category)
        # Изброј колку пати се има појавено овој атрибут (збор) во сите категории
        totals = sum([self.get_feature_counts_per_category(current_feature, currentCategory) for currentCategory in
                      self.categories()])
        # Пресметај ја тежински усредената веројатност
        bp = ((weight * ap) + (totals * basic_prob)) / (weight + totals)
        return bp


class NaiveBayes(DocumentClassifier):
    def __init__(self, get_features):
        super().__init__(get_features)
        self.thresholds = {}

    def set_threshold(self, current_category, threshold):
        """Поставување на праг на одлучување за категорија

        :param current_category: категорија
        :param threshold: праг на одлучување
        :return: None
        """
        self.thresholds[current_category] = threshold

    def get_threshold(self, current_category):
        """Добивање на прагот на одлучување за дадена класа

        :param current_category: категорија
        :return: праг на одлучување за дадената категорија
        """
        if current_category not in self.thresholds:
            return 1.0
        return self.thresholds[current_category]

    def calculate_document_probability_in_class(self, item, current_category):
        """Ја враќа веројатноста на документот да е од класата current_category
        (current_category е однапред позната)

        :param item: документ
        :param current_category: категорија
        :return:
        """
        # земи ги зборовите од документот item
        features = self.get_features(item)
        # помножи ги веројатностите на сите зборови
        p = 1
        for current_feature in features:
            p *= self.weighted_probability(current_feature, current_category,
                                           self.get_feature_per_category_probability)

        return p

    def get_category_probability_for_document(self, item, current_category):
        """Ја враќа веројатноста на класата ако е познат документот

        :param item: документ
        :param current_category: категорија
        :return: веројатност за документот во категорија
        """
        cat_prob = self.get_category_count(current_category) / self.get_total_count()
        calculate_document_probability_in_class = self.calculate_document_probability_in_class(item, current_category)
        # Bayes Theorem
        return calculate_document_probability_in_class * cat_prob / (1.0 / self.get_total_count())

    def classify_document(self, item, default=None):
        """Класифицирање на документ

        :param item: документ
        :param default: подразбирана (default) класа
        :return:
        """
        probs = {}
        # најди ја категоријата (класата) со најголема веројатност
        max = 0.0
        for cat in self.categories():
            probs[cat] = self.get_category_probability_for_document(item, cat)
            if probs[cat] > max:
                max = probs[cat]
                best = cat

        # провери дали веројатноста е поголема од threshold*next best (следна најдобра)
        for cat in probs:
            if cat == best:
                continue
            if probs[cat] * self.get_threshold(best) > probs[best]: return default

        return best