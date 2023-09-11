
def isAnagram(s: str, t: str) -> bool:
    s = sorted(list(s))
    t = sorted(list(t))
    if s == t:
        return True
    return False

if __name__ == "__main__":
    print(isAnagram("car", "rat"))
    print()