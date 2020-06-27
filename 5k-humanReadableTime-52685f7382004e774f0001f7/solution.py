def make_readable(seconds):
    hh = int(seconds / 3600)
    mm = int((seconds - (hh * 3600)) / 60)
    ss = seconds - (hh * 3600 + mm * 60)
    return f'{hh:02d}:{mm:02d}:{ss:02d}'

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))