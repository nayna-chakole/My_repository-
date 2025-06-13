import pandas as pd
import string
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

df = pd.read_csv("career_paths.csv")
df['text'] = df['Career'] + ": " + df['Description']

def clean(text):
    return text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

def jaccard_similarity(str1, str2):
    set1 = set(clean(str1).split())
    set2 = set(clean(str2).split())
    return len(set1 & set2) / len(set1 | set2)

user_input = input("Paste your resume summary or skills: ")
clean_user_input = clean(user_input)
user_words = set(clean_user_input.split())

user_embedding = model.encode([user_input])
career_embeddings = model.encode(df['text'].tolist())

cosine_scores = cosine_similarity(user_embedding, career_embeddings)[0]
df['Match %'] = (cosine_scores * 100).round(2)


for i in range(len(df)):
    if clean(df.loc[i, 'Description']) == clean_user_input:
        df.loc[i, 'Match %'] = 100.0

df['Jaccard'] = df['Description'].apply(lambda x: jaccard_similarity(x, user_input))

df['Final Score'] = (df['Match %'] * 0.8 + df['Jaccard'] * 100 * 0.2).round(2)

top = df.sort_values(by='Final Score', ascending=False).iloc[0]
top_description = clean(top['Description'])
top_words = set(top_description.split())

missing_skills = list(top_words - user_words)

course_db = {
    "python": ["Python for Everybody – Coursera", "Advanced Python – Udemy"],
    "sql": ["SQL for Data Science – Coursera"],
    "ml": ["Machine Learning by Andrew Ng – Coursera"],
    "tensorflow": ["Intro to TensorFlow – Coursera"],
    "react": ["React Basics – Codecademy"],
    "html": ["HTML Crash Course – freeCodeCamp"],
    "css": ["CSS Flexbox and Grid – Coursera"],
    "docker": ["Docker for Beginners – Udemy"]
}

recommended_courses = []
for skill in missing_skills:
    for key in course_db:
        if key in skill:
            recommended_courses.extend(course_db[key])

print("\n******Top Career Match****** :")
print(f"Career: {top['Career']}")
print(f"Final Match Score: {top['Final Score']}%")
print(f"Description: {top['Description']}")

if missing_skills:
    print(f"\n Missing Skills: {', '.join(missing_skills)}")
    print("\n Recommended Courses to Improve:")
    for course in recommended_courses[:5]:
        print(f" {course}")
else:
    print("\n You match this career perfectly. No missing skills!")
