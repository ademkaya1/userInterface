def solution():
    S = "yappbozz"

    occurrences = [0] * 26


    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)

            best_res = occurrences[i]
            print(best_res)

            print(min(ord(best_char)))

solution()

# solution("hello")
# S = 'hppdzz'
# occurrences = [0] * 26
#
# for i in range(len(S)):
#     occurrences[ord(S[i]) - ord('a')] += 1
#
# print(occurrences)
# print("değer")
#
# best_char = 'a'
# best_res = 0
#
# for i in range(1, 26):
#     if occurrences[i] >= best_res:
#         best_char = chr(ord('a') + i)
#         best =
#         best_res = occurrences[i]
#
#         for j in range(1, 26):
#             if (occurrences[j]) == occurrences[i]:
#                 print(min(ord(best_char))
# a = ord(best_char)
# print(best_char)

# if ord(best_char)<best_res:
#     print(best_res)
# print(best_char)
# print(best_char)

# occurrences = [0] * 26
# print(occurrences)
# for i in range(len(S)):
#         occurrences[ord(S[i]) - ord('a')] += 1
