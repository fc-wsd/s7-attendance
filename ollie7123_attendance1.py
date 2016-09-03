students = ['이서준', '고병남', '김재국']
attended_at = ['2016-08-30 21:10:01', '2016-08-31 20:08:12', '2016-08-31 21:00:01']
attendances = {}

def attend(students, attended_at):
   for i in range(len(students)):
       attendances[students[i]] = attended_at[i]

attend(students, attended_at)
print(attendances)

