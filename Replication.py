def PatternMatching(Pattern, Genome):
    positions = []
    lengthPattern = len(Pattern)
    for i in range((len(Genome) - lengthPattern) + 1):
        temp = Genome[i:i+lengthPattern]
        if Pattern in temp:
            positions.append(i)
    return positions

def Complement(Pattern):
    n = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    
    complementPattern = ""
    for char in Pattern:
        complementPattern += n[char]
    return complementPattern

def Reverse(Pattern):
    reversedPattern = ""
    for char in reversed(Pattern):
        reversedPattern += char
    return reversedPattern
    

def ReverseComplement(Pattern):
    complement = Complement(Pattern)
    reverseComplement = Reverse(complement)
    return reverseComplement

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count = count+1
    return count

def mostFrequent(Text, length):
    frequency = {}
    for i in range(len(Text) - length + 1):
        pair = Text[i:i+length]
        if pair in frequency:
            frequency[pair] += 1
        else:
            frequency[pair] = 1
    more_frequency = max(frequency, key=frequency.get)
    return more_frequency, frequency[more_frequency]
  
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    more_freq = max(freq.values())
    for key in freq:
        if freq[key] == more_freq:
            words.append(key)
    return words
    
def FrequencyMap(Text, k):
    freq = {}
    for i in range(len(Text) - k + 1):
        pair = Text[i:i+k]
        if pair in freq:
            freq[pair] += 1
        else:
            freq[pair] = 1

    return freq

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(Genome[0:n//2], symbol)
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

def SkewArray(Genome):
    skew = [0]
    count = 0
    for i in Genome:
        if(i == 'G'):
            count += 1
        elif(i == 'C'):
            count -= 1
        skew.append(count)
    return skew
    
def MinimumSkew(Genome):
    positions = []
    skew_array = SkewArray(Genome)
    minPositions = []
    actualMin = 0
    for i in range(len(skew_array)):
        if(skew_array[i] < actualMin):
            actualMin = skew_array[i]
            minPositions = []
        if(skew_array[i] <= actualMin):
            minPositions.append(i)

    for i in minPositions:
        positions.append(i)
        
    return positions

def HammingDistance(p, q):
    mismatchs = 0
    for d, g in zip(p, q)):
        if(d != g):
            mismatchs += 1
    return mismatchs
    
def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    lenPattern = len(Pattern)
    lenText = len(Text)
    for i in range(lenText-lenPattern+1):
        if(HammingDistance(Text[i:i+lenPattern], Pattern) <= d):
            positions.append(i)
    return positions