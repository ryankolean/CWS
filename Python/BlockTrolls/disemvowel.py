def disemvowel(string):
    return string.translate(string.maketrans('', '', 'aeiouAEIOU'))