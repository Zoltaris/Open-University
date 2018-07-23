# Convert hours
# Input: an hour
hour = 70
complete = False
reduced = False

while complete == False:
    if hour >= 0:
        if hour <= 11:
            string = 'am'
            complete = True
    if hour < 24:    
        if hour >= 12:
            hour = hour - 12
            string = 'pm'
            complete = True
    if hour >= 24:
        reduced = True
        hour = hour - 24
            

print(hour, string)
if (reduced == True):
    print('The time was reduced to a time in a single day,')
    print('as it was larger than 24 hours.')
