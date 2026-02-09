class FrequencyTracker:               #exONnb

    def __init__(self):
        self.num_freq = {}                           
        self.freq_count = {}

    def add(self, number: int) -> None:
        old_freq = self.num_freq.get(number, 0)
        new_freq = old_freq + 1

        self.num_freq[number] = new_freq
        if old_freq > 0:
            self.freq_count[old_freq] -= 1
        self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.num_freq:
            return

        old_freq = self.num_freq[number]
        new_freq = old_freq - 1
        self.freq_count[old_freq] -= 1

        if new_freq == 0:
            del self.num_freq[number]
        else:
            self.num_freq[number] = new_freq
            self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
