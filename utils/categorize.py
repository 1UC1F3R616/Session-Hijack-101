f = open('mass_dump.txt', 'r') # user mass dump goes here
f_read = f.read()


Education = ['Education']
Entertainment = ['Entertainment']
Malicious = ['Malicious']
Shopping_and_Self = ['Shopping_and_Self']
Social_Networking = ['Social_Networking']
Travel_and_Tourism = ['Travel_and_Tourism']
Others = ['Others']

categories = [Education, Entertainment, Malicious, Shopping_and_Self, Social_Networking, Social_Networking, Travel_and_Tourism, Others]

education = open('./clean_categories/education_read', 'r')
education_read = education.read()
education.close()

entertainment = open('./clean_categories/entertainment_read', 'r')
entertainment_read = entertainment.read()
entertainment.close()

malicious = open('./clean_categories/malicious_read', 'r')
malicious_read = malicious.read()
malicious.close()

others = open('./clean_categories/others_read', 'r')
others_read = others.read()
others.close()

shopping = open('./clean_categories/shopping_read', 'r')
shopping_read = shopping.read()
shopping.close()

social = open('./clean_categories/social_read', 'r')
social_read = social.read()
social.close()

tandt = open('./clean_categories/tandt_read', 'r')
tandt_read = tandt.read()
tandt.close()


# num_lines = sum(1 for line in open('myfile.txt'))
import re

regex = r"[a-zA-Z0-9-]*\.*[a-zA-Z0-9]+\.(museum|travel|govuk|ltduk|moduk|netuk|nhsuk|orguk|plcuk|schuk|store|acuk|aero|arpa|asia|couk|coop|firm|info|jobs|meuk|mobi|name|nato|post|biz|cat|com|edu|gov|int|mil|net|nom|org|pro|tel|web|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cw|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|fx|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nt|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|ss|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zr|zw)"


test_str = f_read


matches = re.finditer(regex, test_str, re.MULTILINE)

sites = set()
for matchNum, match in enumerate(matches, start=1):
    print(match.group())
    sites.add(match.group())
    if len(sites)>100:
        break
    elif len(sites)%10 == 0:
        print(len(sites))
    

sites = list(sites)

for website in sites:
    if website in education_read:
        Education.append(website)
    if website in entertainment_read:
        Entertainment.append(website)
    if website in malicious_read:
        Malicious.append(website)
    if website in others_read:
        Shopping_and_Self.append(website)
    if website in shopping_read:
        Social_Networking.append(website)
    if website in social_read:
        Travel_and_Tourism.append(website)
    if website in tandt_read:
        Others.append(website)

print(sites)

print(Education)
print(Entertainment)
print(Malicious)
print(Shopping_and_Self)
print(Social_Networking)
print(Travel_and_Tourism)
print(Others)

interests = dict()
for category in categories:
        interests[category[0]] = len(category)-1

maxi = -1
interest = []
for k, v in interests.items():
    if v>0 and v>maxi:
        interest = k
        maxi = v

print('User has interest in {}'.format(str(interest)))
