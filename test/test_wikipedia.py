def tell_about(topic):
    import wikipedia as wp

    try:

        res = wp.summary(topic, sentences=2)
        return res
    except Exception as e:
        print("error:", e)
        return False


print(tell_about("dogs"))


def wiki_test(topic):
    import wikipedia as wp

    topic = topic.replace("wikipedia", "").lower()
    try:
        res = wp.summary(topic, sentences=1)
        return res
    except Exception as e:
        print("error:", e)
        return False


print(wiki_test("search what is the country philippines in wikipedia?"))
print(wiki_test("in wikipedia define what is a woman?"))
print(wiki_test("can i be happy? in wikipedia"))  # test absurd
