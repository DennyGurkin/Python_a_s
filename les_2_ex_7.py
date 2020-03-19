#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

#Ссылка  на блок - схему:
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ex_2_les_7.drawio#R5Vlbb9sgFP41lrZJrXxNnMdct4dNm1Tt0r7RmNpeneASktj79QMMxoSkTZXGblUpwXC4GM53vsMBW954UXzGIE%2B%2BoQhmlmtHheVNLNd1fNe12M%2BOykrSd7xKEOM0Eo2U4Cr9B4XQFtJ1GsGV1pAglJE014VztFzCOdFkAGO01ZvdoUx%2Faw5iaAiu5iAzpb%2FTiCSVNHT7Sv4FpnEi3%2Bz0BlXNAsjGYiWrBERo2xB5U8sbY4RIlVsUY5gx5Um9VP1mB2rriWG4JMd0%2BJWGm83N1f365vrhu7u6D3%2BOexcCnRUp5YJhRNcvigiTBMVoCbKpko4wWi8jyEa1aUm1%2BYpQToUOFf6FhJQCTLAmiIoSsshELSxS8od1vwxE6bpRMynEyLxQikI1Tza5g8sXohVa4zl8ZM1OrXxqtRAtIMEl7YdhBki60ccHwnziul3d9QdK6ZtdW5i6FwqcS2n6tj4EATiGRPRSONFMYxpKxNF7BpJiwhuQrcUSLKq4wYSlI9ui6g37Mk%2FTEU%2BnJvxZRqnFYN4mKYFXOeC63FJ26yCK10FMYPE4JKaqpcrcHZWJ4lYRzZFNkgbJQvswOJpan6tD%2Fx2yQbjjyjofaRe0whq3ZdZ4%2B1nD05ErOMJSahq2oM%2BujVDHnrMs1T7IMpihGIMFBSmHOKXzg3i37oeq6IJl%2FpE0652LZr13SLN26ON57dInMOhzy3jCcrZJFB3D9i3f9bq2%2FMFbsXyqYVw2OrHidbNOdeOlMzCmf%2BTGFJ7IrJMA7RsEADUBOOd6GZ376BbTXMxzevUrY4jXOUMc0228Uoq8oKmfasLHbQ7BLmjnPpF4XULpNIBUsD7l7TRfp1zf%2Bb1deKS3c%2Fyz2Erg6bbi99u1ldDwo6kMuKf87MpqHSny5eHVBoaJyWg8gQWglrMThwtpHYG7nbhZ%2F1g3e7aTrtPtxc%2Fb4qYjLx7PHYrwrkOMQdlokDPOrQ5Tt96LpZsPg6Z5PNleUl2ZUzWDl90LzOspFQnxnDtyzGhpXrdhYdUn%2Bv8AROOP%2FDnjP9u05q4jqSAIuo6kOj1mP2f7fUmq%2Bsfuo6ceyE%2FDxjfoIO%2Bd6F432n%2F7ZLBDSu4Q57cCuvewRrLiYsWhGrL9084LVdkYRUrYq2Z8CtU%2BG%2B6ZiJDzLZmlDk9nu1szS4eN%2B%2BZ%2B4x66GjCQ99BUMm4Mpd29XV5qE86q56xasa4F7YxFYbHnB2ODV3pTF%2ByGCZ3f1DnmBQ%2B302ED5YlEk2K3x%2BW0%2BD2hN2gvzKJF9emu2iXVB1Bv%2Bh8%3D

a = int(input("Введите любое натуральное число: "))
b = 0
for i in range(1, a + 1):
    b += i
c = a * (a + 1) // 2

print("В качестве доказательства приводится равенство обоих сторон уравнения:\n11+2+...+n =", b, "\nn(n+1)/2 =", c)
