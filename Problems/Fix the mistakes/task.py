for word in input().split():
    # finish the code here
    if word.lower().startswith(("https://", "http://", "www.")):
        print(word)
