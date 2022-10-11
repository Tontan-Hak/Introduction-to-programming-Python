# Splitting a string
text = """ 
Active learning is a process that has student learning at its centre. Active learning focuses on how students learn, not just on what they learn. Students are encouraged to ‘think hard’,
rather than passively receive information from the teacher. Research shows us that it is not possible to transmit understanding to students by simply telling them what they
need to know. Instead, teachers need to make sure that they challenge their students’ thinking. With active learning, students play an important part in their own learning process.
They build knowledge and understanding in response to opportunities provided by their teacher.
"""
print(len(text.split()))

# Counting the words
Text = """
Active learning is a process that has student learning at its centre. Active learning focuses on how students learn, not just on what they learn. Students are encouraged to ‘think hard’, rather than passively receive information from the teacher. Research shows us that it is not possible to transmit understanding to students by simply telling them what they need to know. Instead, teachers need to make sure that they challenge their students’ thinking. With active learning, students play an important part in their own learning process. They build knowledge and understanding in response to opportunities provided by their teacher.
"""
print(Text.split())
word_count = {}
for word in Text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1 
print(word_count)