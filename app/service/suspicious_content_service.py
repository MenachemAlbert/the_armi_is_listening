
def contains_suspicious_content(sentences, suspicious_content):
    for i, sentence in enumerate(sentences):
        if suspicious_content in sentence:
            if i != 0:
                sentences[0], sentences[i] = sentences[i], sentences[0]
            return True
    return False
