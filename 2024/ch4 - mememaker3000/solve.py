a = 'boy_friend0.jpg'
b = 'FLARE On'
c = 'Security Expert'
d = 'Malware'


a0c = [
    'When you find a buffer overflow in legacy code',
    'Reverse Engineer',
    'When you decompile the obfuscated code and it makes perfect sense',
    'Me after a week of reverse engineering',
    'When your decompiler crashes',
    "It's not a bug, it'a a feature",
    "Security 'Expert'",
    'AI',
    "That's great, but can you hack it?",
    'When your code compiles for the first time',
    "If it ain't broke, break it",
    "Reading someone else's code",
    'EDR',
    'This is fine',
    'FLARE On',
    "It's always DNS",
    'strings.exe',
    "Don't click on that.",
    'When you find the perfect 0-day exploit',
    'Security through obscurity',
    'Instant Coffee',
    'H@x0r',
    'Malware',
    '$1,000,000',
    'IDA Pro',
    'Security Expert',
  ]



  # var f = d[3] + 'h' + a[10] + b[2] + a[3] + c[5] + c[c.length - 1] + '5' + a[3] + '4' + a[3] + c[2] + c[4] + c[3] + '3' + d[2] + a[3] + 'j4' + a0c[1][2] + d[4] + '5' + c[2] + d[5] + '1' + c[11] + '7' + a0c[21][1] + b.replace(' ', '-') + a[11] + a0c[4].substring(12, 15)
result = (
    d[3] + 'h' + a[10] + b[2] + a[3] + c[5] + c[len(c) - 1] + '5' + a[3] + '4' + a[3] + c[2] + c[4] + c[3] + '3' +
    d[2] + a[3] + 'j4' + a0c[1][2] + d[4] + '5' + c[2] + d[5] + '1' + c[11] + '7' + a0c[21][1] + b.replace(' ', '-') +
    a[11] + a0c[4][12:15]
)

print(result.lower())