from operator import attrgetter
from collections import Counter

from toolz import pipe

from app.db.psql.repository.sentences_repository import get_all_hostage_sentences, get_all_explosive_sentences


def get_most_common():
    return pipe(
        list(map(attrgetter('sentence'), get_all_hostage_sentences())) +
        list(map(attrgetter('sentence'), get_all_explosive_sentences())),
        lambda x: [word for word in "".join(x).replace(".", " ").split(" ")],
        lambda x: (max(Counter(x).most_common(), key=lambda t: t[1])))
