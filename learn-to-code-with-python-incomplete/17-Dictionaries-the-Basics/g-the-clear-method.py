# clear() : removes all key-value pairs from Dict. But the object still exist. It just becomes an empty dict
websites = {
    "Wikipedia":"Http://www.wikipedia.org",
    "Google":"Http://www.google.com",
    "Netflix":"Http://www.netflix.com"
}
print(websites)
websites.clear()
print(websites)


# del: totally remove this object in memory
del websites

