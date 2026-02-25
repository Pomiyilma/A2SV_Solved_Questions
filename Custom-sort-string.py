class Solution:
    def customSortString(self, order: str, s: str) -> str:    #exONnb
        s_counts = Counter(s)
        string_builder = []

        for i in range(0, len(order)):
            if order[i] in s_counts:
                string_builder.append(order[i] * s_counts[order[i]])
                del s_counts[order[i]]

        for char, count in s_counts.items():
            string_builder.append(char * count)

        return "".join(string_builder)
