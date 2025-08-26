import spacy
import string

nlp = spacy.load("en_core_web_sm")

text = """
My name is Sanskruti Deshmukh, a final-year Information Technology Engineering student from Kopargaon.
I study at Sanjivani College of Engineering and have a deep interest in AIMl, IoT, and cybersecurity.
I have worked on several projects including a Smart Health Monitoring System and an Inventory Management System using the MERN stack.

"""

doc = nlp(text)

filtered_tokens = [token.text.lower() for token in doc if not token.is_stop and token.text not in string.punctuation]

lemmatized = [token.lemma_ for token in doc if not token.is_stop and token.text not in string.punctuation]

print("Filtered Tokens:", filtered_tokens)
print("==========================================================")

print("Lemmatized Tokens:", lemmatized)