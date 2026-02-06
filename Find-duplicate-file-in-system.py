from collections import defaultdict

class Solution:
    def findDuplicate(self, paths):                      #exONnb
        content_map = defaultdict(list)

        for entry in paths:
            parts = entry.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name, rest = file_info.split("(")
                content = rest[:-1]

                full_path = directory + "/" + name
                content_map[content].append(full_path)

        return [files for files in content_map.values() if len(files) > 1]
