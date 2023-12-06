import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', family='Times New Roman', size='15.5')
matplotlib.rc('pdf', fonttype=42)
matplotlib.rcParams['savefig.transparent'] = True


def count_zero_length_answers(answers):
    return sum(len(answer) == 0 for answer in answers)


df = pd.read_json("./data.json")
who = pd.read_csv("./who.csv")
who = who[who['Country'] == 'Bangladesh']
who['Date_reported'] = pd.to_datetime(who['Date_reported'])

df = df[df['date'] >= min(who['Date_reported'])]
who = who[who['Date_reported'] <= max(df['date'])]

who['New_cases'] -= who['New_cases'].min()
who['New_cases'] /= who['New_cases'].max()

df = df.groupby('date')

unanswered = df['answers'].apply(count_zero_length_answers)
unanswered -= unanswered.min()
unanswered /= unanswered.max()
unanswered.plot(label='No. of Unanswered Questions')

questions = df.size()
questions -= questions.min()
questions /= questions.max()
questions.plot(label='No. of Questions')

plt.plot(who['Date_reported'], who['New_cases'], label='Confirmed Cases of COVID-19')
plt.xlabel("Date")
plt.ylabel("")
plt.legend(loc='upper right')
plt.savefig('Unanswered.pdf', bbox_inches='tight', pad_inches=0)
