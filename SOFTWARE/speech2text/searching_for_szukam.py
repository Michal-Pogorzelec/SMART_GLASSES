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


def kmp_search(S, frag='szukam'):

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
