from datetime import datetime, timedelta

now = datetime.now()

twoDays = now + timedelta(days=2)

treeWeeksAgo = now - timedelta(weeks=3)

print(f'Daqui a dois dias:{twoDays.date()}')

print(f"Tree weeks ago: {treeWeeksAgo.date()}")