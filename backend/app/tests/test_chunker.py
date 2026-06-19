from app.utils.text_splitter import split_text


text = """
Consistent hashing distributes keys.
Virtual nodes improve balancing.
Replication improves durability.
Caching reduces latency.
""" * 100

chunks = split_text(text)
