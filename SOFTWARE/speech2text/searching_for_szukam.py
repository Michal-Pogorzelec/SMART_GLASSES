import time

def kmp_table(w):

    pos = 1
    cnd = 0
    T = [[0] for i in range(len(w)+1)]
    T[0] = -1

    while pos < len(w):

        if w[pos] == w[cnd]:
            T[pos] = T[cnd]

        else:
            T[pos] = cnd
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = T[cnd]

        pos += 1
        cnd += 1

    T[pos] = cnd

    return T


def kmp_search(S: str, frag: str='szukam') -> str:

    comp = 0
    m = 0 #(the position of the current character in S)
    i = 0 #(the position of the current character in W)
    nP = 0 #(number of positions)
    T = kmp_table(frag)
    word=[]

    while m < len(S):

        if frag[i] == S[m]:
            m += 1
            i += 1

            if i == len(frag):

                j=1

                if m+j < len(S):
                    while S[m+j] != ' ':
                        word.append(S[m+j])
                        j+=1

                        if m+j >= len(S):
                            break

                nP += 1

                if T[len(frag)] != -1:
                    i = T[i]

        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    word = ''.join(word)

    return word


def search_fun(S: str) -> str:
    words = S.split()
    print(words)
    for i, word in enumerate(words):
        if word == "szukam":
            try:
                return words[i+1]
            except IndexError as e:
                print(e)


if __name__ == "__main__":
    start = time.perf_counter()
    print(kmp_search("krążę właśnie po pokoju i szukam krzesła żeby usiąść"))
    stop = time.perf_counter()
    print(f"Czas: {stop-start}")
    start2 = time.perf_counter()
    print(search_fun("krążę właśnie po pokoju i szukam krzesła żeby usiąść"))
    stop2 = time.perf_counter()
    print(f"Czas2: {stop2-start2}")

