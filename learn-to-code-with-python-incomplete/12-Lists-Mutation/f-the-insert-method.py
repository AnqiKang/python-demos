# insert(index, value) : Insert object before index.
plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caesar")
print(plays)

plays.insert(0, "Romeo & Juliet")
print(plays)

# if inserted index out or range, just add elements at end, no error
plays.insert(10, "A midsummer Night's Dream")
print(plays)

