s = 'azcbobobegghakl'

longest = ''
tempstr = ''
for i in range(len(s)-1):
  tempstr += s[i]

  if i+1 == len(s)-1 and len(tempstr) >= len(longest):
    if s[i] < s[i+1]:
      tempstr += s[len(s)-1]
      longest = tempstr
      break;
  
  if s[i] > s[i+1]:
    if len(tempstr) > len(longest):
      longest = tempstr
    tempstr = '';
    
if len(longest) == 0:
  longest = tempstr
print('Longest substring in alphabetical order is:', longest)