def fun(s):
    # return True if s is a valid email, else return False
    try:
        username,domain = s.split("@")
        website,extention = domain.split(".")
        if(len(extention)==0 or len(extention)>3 or not extention.isalpha()):
            return False
        if(not website.isalnum()):
            return False
        username=username.replace("_","")
        username=username.replace("-","")
        if(not username.isalnum()):
            return False
        
        return True
    except:
        pass
            

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
